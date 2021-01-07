from collections import defaultdict
import pickle

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingClassifier, AdaBoostClassifier, RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn import model_selection
from sklearn.metrics import recall_score, accuracy_score, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC, NuSVC


def exportModel(model, name="model"):
    filename = f'{name}.sav'
    pickle.dump(model, open(filename, 'wb'))
    print(f"Model exported as: {filename}")


df = pd.read_csv("mushrooms_v2.csv")

print(df.head())
y = df["class"].to_frame()

# Encoding the variable

X = df.drop("class", axis=1)
attrDict = defaultdict(LabelEncoder)

yEncoder = LabelEncoder()
X = X.apply(lambda x: attrDict[x.name].fit_transform(x))

y = y.apply(lambda x: yEncoder.fit_transform(x))
le_name_mapping = dict(zip(yEncoder.classes_, yEncoder.transform(yEncoder.classes_)))

print(le_name_mapping)

# save the encoders to disk
filenameEnc = 'encoder.sav'
pickle.dump(attrDict, open(filenameEnc, 'wb'))
filenameYEnc = 'Yencoder.sav'
pickle.dump(yEncoder, open(filenameYEnc, 'wb'))

'''
# Inverse the encoded
fit.apply(lambda x: attrDict[x.name].inverse_transform(x))

# Using the dictionary to label future data
df.apply(lambda x: attrDict[x.name].transform(x))
'''

models = []
# models.append(('GNB', GaussianNB()))
# models.append(('RFC', RandomForestClassifier(n_estimators=500)))
# models.append(('ABC', AdaBoostClassifier(n_estimators=500)))
# models.append(('LDA', LinearDiscriminantAnalysis()))
# models.append(('QDA', QuadraticDiscriminantAnalysis()))
# models.append(('NSVC', NuSVC(probability=True)))
models.append(('GBC00', GradientBoostingClassifier(n_estimators=500, learning_rate=0.5)))
# models.append(('KNN', KNeighborsClassifier(3)))
# models.append(('CART', DecisionTreeClassifier()))
# models.append(('SVM', SVC(gamma="scale")))
# models.append(('MPL', MLPClassifier((150, 3), max_iter=500)))
results = []

names = []

for name, model in models:
    kfold = model_selection.StratifiedKFold(n_splits=10)
    cv_results = []
    maxx = 0
    for train_index, test_index in kfold.split(X, y):
        # print(train_index, test_index)
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]
        model.fit(X_train, y_train.values.ravel())
        y_pred = model.predict(X_test)
        recall = recall_score(y_test, y_pred)
        accuracy = accuracy_score(y_test, y_pred)
        cv_results.append(recall)
        print(f"{name} - Recall: {str(recall)}, Acc: {str(accuracy)}")
        if maxx < recall:
            maxx = recall
            exportModel(model, name)
            print(confusion_matrix(y_test, y_pred, [0,1]))
    cv_results = np.array(cv_results)
    results.append(cv_results)
    names.append(name)
    msg = "%s: Mean: %f (Std: %f) Max: %f" % (name, cv_results.mean(), cv_results.std(), cv_results.max())
    print(msg)
# boxplot algorithm comparison
fig = plt.figure()
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)

plt.show()

