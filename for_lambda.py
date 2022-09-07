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
loaded_model = pickle.load(open("finalized_model.sav", 'rb'))
random_kullanıcı = pd.read_csv("random_kullanıcı.csv")

loaded_model.predict(random_kullanıcı[0:3])
loaded_model.predict_proba(random_kullanıcı)