import pandas as pd
import numpy as np
import pickle
data=pd.read_excel("iris-8.xls")
x=np.array(data.iloc[:,0:4]) 
y=np.array(data.iloc[:,4:])
from sklearn.preprocessing import LabelEncoder
lb=LabelEncoder()
y=lb.fit_transform(y)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=32)
from sklearn.linear_model import LogisticRegression
regr=LogisticRegression()
md=regr.fit(x_train,y_train)
pickle.dump(regr,open('iris.pkl','wb'))
