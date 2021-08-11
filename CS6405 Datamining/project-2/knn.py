import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

#read in the data using pandas
df = pd.read_csv('dataset-sat.csv')

X = df.drop(columns=['ebglucose_solved'])
y = df['ebglucose_solved'].values


#split dataset into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, stratify=y)


# Create KNN classifier
knn = KNeighborsClassifier(n_neighbors = 3)

# Fit the classifier to the data
knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)

score = knn.score(X_test, y_test)


print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

print ("Accuracy:",score)

