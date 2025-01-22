import pandas as pd
file_path = "E:\\Python class\\Pathogenicity.csv"
data = pd.read_csv(file_path)
x = data.iloc[:,2:6].values
y = data.iloc[:,8].values
print(x)
print(y)

from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()
x[:,0] = lb.fit_transform(x[:,0])
print(x)
lb2 = LabelEncoder()
y = lb2.fit_transform(y)
print("\n The respected dependent variable are =", y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = (train_test_split(x, y, test_size=0.3, random_state=0))
print(x_train)
print(x_test)

from sklearn.preprocessing import MinMaxScaler
scale = MinMaxScaler()
x_train = scale.fit_transform(x_train)
x_test = scale.fit_transform(x_test)
print(x_train)
print(x_test)

from sklearn.svm import SVC
cl1 = SVC(kernel='linear' , random_state=0)
cl1.fit(x_train, y_train)
y_predict = cl1.predict(x_test)

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_predict)
print(cm)
acc = accuracy_score(y_test, y_predict)
print(acc)