import pandas as pd
from sklearn import model_selection
from sklearn.neighbors import KNeighborsClassifier

class MyClassifier:

    def predict(self,list1):
        names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
        df = pd.read_excel("iris.xls", names=names)
        print(df)
        print(df.groupby("class").size())
        # Split-out validation dataset
        array = df.values
        X = array[:, 0:4]
        Y = array[:, 4]
        print(X)
        validation_size = 0.20
        seed = 7
        X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size,random_state=seed)
        # Make predictions on validation dataset
        knn = KNeighborsClassifier()
        # train
        knn.fit(X_train, Y_train)
        X1=[list1]
        predictions = knn.predict(X1)
        # print('Predictin is ')
        # print(predictions)
        return  predictions