import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas._config import display

data = pd.read_csv("titanic.csv")
print(data.columns)
plt.grid()
# suv = data.query("Survived== 1")
plt.xlabel("Сестры братья")
plt.ylabel("количество пассажиров")
new = data.loc[data["Survived"] == 1]


# print(new)
# plt.hist(data["Age"], label='Всего', bins=8)
# plt.hist(new["Age"], label='Выжило', bins=8)
# plt.legend()
# plt.show()


def count_suv_age(x):
    age_per = data.loc[data["Age"] == x]
    total = len(age_per)
    out_of = age_per.loc[data["Survived"] == 1]
    suv_pas = len(out_of)
    persent_of_Suv = round(suv_pas * 100 / total, 2)
    return persent_of_Suv
def count_suv_pclass(x):
    pclass_per = data.loc[data["Pclass"] == x]
    total = len(pclass_per)
    out_of = pclass_per.loc[data["Survived"] == 1]
    suv_pas = len(out_of)
    persent_of_Suv = round(suv_pas * 100 / total, 2)
    return persent_of_Suv
def count_suv_sex(x):  # male/female
    sex_per = data.loc[data["Sex"] == x]
    total = len(sex_per)
    out_of = sex_per.loc[data["Survived"] == 1]
    suv_pas = len(out_of)
    persent_of_Suv = round(suv_pas * 100 / total, 2)
    return persent_of_Suv
def result(x, y, z): # возраст, класс, пол
    return round((count_suv_age(x) + count_suv_pclass(y) + count_suv_sex(z)) / 3, 2)
print(result(19, 1, "male"))

#print(count_suv_sex('female'))
print(count_suv_age(30))