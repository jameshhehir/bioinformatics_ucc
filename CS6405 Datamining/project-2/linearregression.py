from sklearn import linear_model
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn import metrics 

df = pd.read_csv('dataset-sat.csv')

X = df.drop(columns=['ebglucose_solved'])
y = df['ebglucose_solved'].values

lm = linear_model.LinearRegression()
model = lm.fit(X,y)

predictions = lm.predict(X)
print(predictions[0:5])

print(lm.score(X,y))