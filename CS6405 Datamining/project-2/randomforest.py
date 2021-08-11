import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import metrics 

df = pd.read_csv('dataset-sat.csv')

X = df.drop(columns=['ebglucose_solved'])
y = df['ebglucose_solved'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

RFC=RandomForestClassifier(n_estimators=1000)

RFC.fit(X_train,y_train)

y_pred=RFC.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
