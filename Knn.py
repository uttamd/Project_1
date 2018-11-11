from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn import datasets


iris = datasets.load_iris()
X_train, y_train = iris.data , iris.target
#X_train = X_train.reshape(-1,4)
#print(np.size(X_train), np.size(y_train))
model = KNeighborsClassifier(n_neighbors=1)
model.fit(X_train,y_train)
x_test = np.array(([1.2,2.2,10,4.4]))
print(model.predict(x_test))