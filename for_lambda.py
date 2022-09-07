import pickle
import pandas as pd
"""
dışardan alınan parametreler list formatında fonksiyona girilecek:
list içinde sırasıyla :
            'PaperlessBilling' :                1-0
           'MonthlyCharges' :                   int
            TotalCharges',                      int
            Partner :                           1-0
           'MultipleLines':                     1-0
           'Type_One year'                      1-0
           'Type_Two year'                      1-0
           'InternetService_DSL'                1-0
           'InternetService_Fiber optic'        1-0
           'OnlineBackup_No',                   1-0
           'OnlineBackup_Yes'                   1-0
           'DeviceProtection_No'                1-0
           'DeviceProtection_Yes',              1-0
           'TechSupport_No'                     1-0
           'TechSupport_Yes'                    1-0
           'StreamingTV_No'                     1-0
           'StreamingTV_Yes'                    1-0
           'StreamingMovies_No'                 1-0
            'StreamingMovies_Yes'               1-0
          )

"""

coef = model.coef_
intercept = model.intercept_

coef_manuel = array([[ 0.4154125991466438,  3.24458514e-03, -3.45091543e-04,
        -1.36342089e-01,  2.83320714e-01, -9.79567872e-01,
        -1.39614017e+00, -3.35341165e-01,  8.27396051e-01,
         3.22839172e-01,  1.69215715e-01,  2.47975367e-01,
         2.44079520e-01,  4.87158783e-01,  4.89610411e-03,
         5.96070698e-02,  4.32447817e-01,  1.24782663e-01,
         3.67272224e-01][])
coef_list = []
for c in range(19):
    coef_list.append(coef[0][c])
    print(coef[0][c])

loaded_model = pickle.load(open("finalized_model.sav", 'rb'))
random_kullanıcı = pd.read_csv("random_kullanıcı.csv")
random_kullanıcı.to_excel("dddd.xlsx")

loaded_model.predict("0","50.0","2919.85","1","2","1","0","1","0","0","1","0","1","1","0","0","1","1","0")
loaded_model.predict(sample)
type(random_kullanıcı.iloc[0])

sample = dict(random_kullanıcı.iloc[1])