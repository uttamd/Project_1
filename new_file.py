from sklearn import datasets
from sklearn import svm
from  sklearn.metrics import accuracy_score
import  numpy as np


iris = datasets.load_iris()
X,y = iris.data[0:125,2], iris.target[0:125]
X =X.reshape(-1,1)
X_train ,y_train =X,y
model = svm.SVC(kernel='linear')
X_test , y_test = iris.data[125:,2],iris.target[125:]
X_test = X_test.reshape(-1,1)
model.fit(X_train,y_train)

y_predict_mod = model.predict(X_test)
print(accuracy_score(y_test,y_predict_mod))
