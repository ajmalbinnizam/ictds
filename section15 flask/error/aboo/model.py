import pickle
import pandas as pd
from sklearn.model_selection import train_test_split

data=pd.read_excel('iris.xls')
x=data.drop(['Classification'],axis=1)
y=data['Classification']
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=0.2)


from sklearn.tree import DecisionTreeClassifier
dt_model=DecisionTreeClassifier()
dt_model.fit(x_train,y_train)
#saving model to disk
pickle.dump(dt_model,open('model.pkl','wb'))
 
