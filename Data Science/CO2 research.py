import sklearn
#import numpy
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
from sklearn.linear_model import LinearRegression

data = pd.read_csv("co2_mm_gl.csv")
# print(data.describe())
# print(data['average'].max())
# print(data.query("average == 416.49").index.tolist())
# print(data)
model = LinearRegression()
x = data[["decimal"]]
y = data[["average"]]
model.fit(x,y)
plt.title('График СО2')
plt.ylabel('Частиц СО2')
plt.xlabel('Годы')
plt.plot(data[["decimal"]],model.predict(x))
plt.grid()
plt.show()
print("Предсказание на 2030",model.predict([[2030]]))
print("Предсказание на 2050",model.predict([[2050]]))
print("Предсказание на 2236",model.predict([[2236]]))
print("физиологи не рекомендуют привышение 800 единиц")
print("")
print("Предсказание на 2564",model.predict([[2564]]))
print("Превышение 1400 единиц считается опасным для здоровья")
print("")
print("Точность модели",model.score(x,y),"процента")
print("Коэфициент",model.coef_)
# fig = plt.figure()   # Создание объекта Figure
# plt.title('График СО2')
# plt.ylabel('Частиц СО2')
# plt.xlabel('Время')
# plt.scatter(1.0, 1.0)   # scatter - метод для нанесения маркера в точке (1.0, 1.0)

# plt.show()

