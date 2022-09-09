import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
from sklearn.metrics import accuracy_score, recall_score, roc_auc_score, f1_score,precision_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np
pd.set_option("display.max_columns" , 100)
pd.set_option("display.max_rows", 100)

#verinin okunması
contract = pd.read_csv("final_provider/contract.csv")
internet = pd.read_csv("final_provider/internet.csv")
personal = pd.read_csv("final_provider/personal.csv")
phone = pd.read_csv("final_provider/phone.csv")

#Gözlemler veriyi tanıma
# TODO: EKLEMELER YAPILABİLİR
contract["customerID"].nunique()
internet["customerID"].nunique()
personal["customerID"].nunique()
phone["customerID"].nunique()

#df merge işlemleri
df1 = pd.merge(contract,internet,on="customerID", how = "outer")
df2 = pd.merge(df1,personal,on="customerID", how = "outer")
df3 = pd.merge(df2,phone,on="customerID", how = "outer")
#df3["MultipleLines"].unique()

#veri ön işleme
#EKSİK DEĞER ANALİZİ
# TODO :alternatif çözümler üretebilirsin
def missing_values_table(dataframe, na_name=False):
    na_columns = [col for col in dataframe.columns if dataframe[col].isnull().sum() > 0]
    n_miss = dataframe[na_columns].isnull().sum().sort_values(ascending=False)
    ratio = (dataframe[na_columns].isnull().sum() / dataframe.shape[0] * 100).sort_values(ascending=False)
    missing_df = pd.concat([n_miss, np.round(ratio, 2)], axis=1, keys=['n_miss', 'ratio'])
    print(missing_df, end="\n")
    if na_name:
        return na_columns
missing_values_table(df3, True)
#yapılan merge işlemi sonucu görüldü ki bazı kullanıcıların internet bilgileri yok.
#ayrıca tekil olarak da MultipleLines değişkeninde %10 eksik değer var.

#bütün null değerleri bilinmiyor ile dolduralım

df3.fillna(value="bilinmiyor",inplace=True)
missing_values_table(df3, True)

#TotalCharges değişkeninde boş değerler gördük bunları inceleyelim.
df3['TotalCharges']=df3.TotalCharges.replace(" ",0)
df3['TotalCharges'] = pd.to_numeric(df3['TotalCharges'])
df3['TotalCharges'].value_counts()
#toplam 11 tane boş değişken varmış bunlara eksik değer mumalesi yapalım ve ortalama ile değiştirelim
df3['TotalCharges']=df3.TotalCharges.replace(0,df3['TotalCharges'].mean())

#AYKIRI DEĞER

# TODO:  ZAMAN KALIRSA BURAYI DA YAP

#churn değişkeni ekleme
df3.loc[(df3.EndDate != 'No'), 'churn'] = 1
df3.loc[(df3.EndDate == 'No'), 'churn'] = 0


#encoding işlemleri

#label encoding
df3["gender"] = LabelEncoder().fit_transform(df3["gender"])
df3["MultipleLines"] = LabelEncoder().fit_transform(df3["MultipleLines"])
df3["Partner"] = LabelEncoder().fit_transform(df3["Partner"])
df3["Dependents"]= LabelEncoder().fit_transform(df3["Dependents"])
df3["PaperlessBilling"]= LabelEncoder().fit_transform(df3["PaperlessBilling"])

#OHE
df3 = pd.get_dummies(df3, columns = ['Type',"PaymentMethod", 'InternetService', 'OnlineSecurity', 'OnlineBackup',
       'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies'])

#standartlaştırmalar
std_num_cols = ["MonthlyCharges","TotalCharges"]

"""scaler = StandardScaler()        #dışardan alınacak verinin standartlaştırılması zor olacağından bundan vazgeçtik 
df3[std_num_cols] = scaler.fit_transform(df3[std_num_cols])
"""
#model için veriyi hazırlamak

df3.columns
drop_list = ["churn","customerID","BeginDate","EndDate","Type_Month-to-month","PaymentMethod_Bank transfer (automatic)",
             "InternetService_bilinmiyor","OnlineSecurity_bilinmiyor","OnlineBackup_bilinmiyor","DeviceProtection_bilinmiyor",
             "TechSupport_bilinmiyor","StreamingTV_bilinmiyor","StreamingMovies_bilinmiyor"]
#eğer modeli eski haline getirmek istersen new_drop_list silinecek.
new_drop_list = [
    "gender","OnlineSecurity_No","SeniorCitizen","Dependents","OnlineSecurity_Yes","PaymentMethod_Mailed check","PaymentMethod_Electronic check",
    "PaymentMethod_Credit card (automatic)"
]

#train test olarak veriyi ayrıma

y = df3['churn']
X = df3.drop(drop_list, axis=1)
X = X.drop(new_drop_list, axis=1) #değişkenleri azaltmak için yaptım
y = y.astype('int')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=9 ) #denemek için random_state=11 argumanı girmedim

#model kurma
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)[:, 1]

#hata metrikleri


print('Logistic regression metrics')
print('Accuracy: {:.10f}'.format(accuracy_score(y_test, predictions)))
print('Precision: {:.2f}'.format(precision_score(y_test, predictions)))
print('Recall: {:.2f}'.format(recall_score(y_test, predictions)))
print('F1: {:.2f}'.format(f1_score(y_test, predictions)))
print('ROC_AUC: {:.2f}\n'.format(roc_auc_score(y_test, probabilities)))
#****************************************************************************************************
"""
#modeli save etmek

import pickle
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))

loaded_model = pickle.load(open(filename, 'rb'))
loaded_model.predict_proba(random_kullanıcı)



random_kullanıcı = X_test.sample(n=10, random_state=3)

random_kullanıcı = pd.DataFrame(random_kullanıcı)
random_kullanıcı.to_csv('random_kullanıcı.csv', index=False)

"""