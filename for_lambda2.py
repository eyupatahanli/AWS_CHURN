coef_list = [0.4154125991466438,
 0.0032445851411571774,
 -0.00034509154330878024,
 -0.1363420894441172,
 0.28332071415827775,
 -0.9795678719868339,
 -1.3961401674811593,
 -0.335341164572412,
 0.8273960513740926,
 0.3228391718742535,
 0.16921571477583672,
 0.24797536662666084,
 0.24407952002843666,
 0.48715878269919416,
 0.004896104106474454,
 0.059607069815376626,
 0.43244781687196326,
 0.12478266271529356,
 0.36727222396470316] #local de kurulan modelin formüle edilmesi için gereken katsayılar.
intercept = -2.00956887  #localde kurulan modelin sabit değeri
import numpy as np
def logistic(x):
    """
    log. reg. modelinin ikinci aşamadaki (1/1+e^(-x) formülünün fonksiyonu
    :param x:
    :return:
    """
    return 1.0 / (1 + np.exp(-x))

def model(sample):
    """
    log. reg. modelinin birinci aşamadaki yi=b0+B1*xi formülünün fonksiyonu
    :param sample:
    :return:
    """
    s1 = 0
    for j in range(19):  # kullanıcının datasındaki her bir değişken için
        s1 += sample[j] * coef_list[j]
    y_sapka = s1 + intercept
    print(logistic(y_sapka))
    if logistic(y_sapka) > 0.5:
        print("churn")
    else:
        print("not_churn")



