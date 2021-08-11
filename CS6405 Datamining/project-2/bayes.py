import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn import metrics 
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv('dataset-sat.csv')

X = df.drop(columns=['ebglucose_solved'])
y = df['ebglucose_solved'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


gnb = GaussianNB()

gnb.fit(X_train, y_train)

y_pred = gnb.predict(X_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))