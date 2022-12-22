import numpy as np
from sklearn.linear_model import LinearRegression

#Database
# x = Data, y = Target
x = [[1],[3],[5],[7],[9],[11],[13],[15],[17],[19]]
y = [2, 6, 10, 14, 18,22,26,30,34,38] # hasil kali 2 dari nilai x

regr = LinearRegression().fit(x,y)
regr.score(x, y)

#Data uji
predict = np.array([[10]])

#Menampilkan data prediksi
print ("Prediksi")
print ("Input = ", predict)
print ("Output = ", regr.predict(predict))
