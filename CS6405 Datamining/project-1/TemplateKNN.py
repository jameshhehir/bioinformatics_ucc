
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def calculateDistance(dataSet, query_point):
    distance = np.square(dataSet - query_point)
    distance = np.sum(distance) # adds all values
    distance = np.sqrt(distance) 
    return distance

def distance_from_all_training(test_point):
    dist_array = np.array([])
    for train_point in train_features:
        dist = calculateDistance(test_point, train_point)
        dist_array = np.append(dist_array, dist)
    return dist_array


wine_test_df = pd.read_csv('wine-data-project-test.csv', sep = ',')
wine_train_df = pd.read_csv('wine-data-project-train.csv', sep = ',')

features_test = wine_test_df[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar','chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']]
test_features = features_test.to_numpy() 
features = wine_train_df[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar','chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']]
train_features = features.to_numpy() # converts feature set to numpy array

train_target = wine_train_df['Quality'].to_numpy() # converts target column to numpy array
test_target = wine_test_df['Quality'].to_numpy()


'''
######################################## EUCLIDEAN DISTANCE ##########################################################

def knn(train_features, train_target, test_features, k):


    predictions = np.array([])
    train_target = train_target.reshape(-1,1)
    for test_point in test_features: # iterating through every test data point 
        dist_array = distance_from_all_training(test_point).reshape(-1,1) # calculating distance from every training data instance
        neighbors = np.concatenate((dist_array, train_target), axis = 1) 
        neighbors_sorted = neighbors[neighbors[:, 0].argsort()] # sorts training points on the basis of distance
        k_neighbors = neighbors_sorted[:k] # selects k-nearest neighbors
        frequency = np.unique(k_neighbors[:, 1], return_counts=True)
        target_class = frequency[0][frequency[1].argmax()] # selects label with highest frequency
        predictions = np.append(predictions, target_class)

    return predictions

def accuracy(y_test, y_preds):
    correctClassifications = 0
    for i in range(len(y_test)):
        if int(y_test[i]) == int(y_preds[i]):
            correctClassifications += 1
    acc = correctClassifications/len(y_test)
    return acc

allResults = []
for k in range(3, 40, 2):
    test_predictions = knn(train_features, train_target, test_features, k)
    allResults.append(accuracy(test_target, test_predictions))
    acc = accuracy(test_target, test_predictions)
    print('Model accuracy ' , k , '=', acc*100)

sns.set_style("darkgrid")
plt.plot( list(range(3, 40, 2)), allResults)    
plt.show()


########################################### WEIGHTED KNN ##############################################################

def Weightedknn(train_features, train_target, test_features, k):
    predictions = np.array([])
    train_target = train_target.reshape(-1,1)
    for test_point in test_features: # iterating through every test data point 
        dist_array = distance_from_all_training(test_point).reshape(-1,1) # calculating distance 
        dist_array = np.square(dist_array[::-1]) #inverse square distance
        neighbors = np.concatenate((dist_array, train_target), axis = 1) 
        neighbors_sorted = neighbors[neighbors[:, 0].argsort()] # sorts training points on the basis of distance
        k_neighbors = neighbors_sorted[:k] # knn selected
        frequency = np.unique(k_neighbors[:, 1], return_counts=True)
        target_class = frequency[0][frequency[1].argmax()] # highest frequency
        predictions = np.append(predictions, target_class) 
    return predictions

def accuracy(y_test, y_preds):
    correctClassifications = 0
    for i in range(len(y_test)):
        if int(y_test[i]) == int(y_preds[i]):
            correctClassifications += 1
    acc = correctClassifications/len(y_test)
    return acc

allResults = []
for k in range(3, 40, 2):
    test_predictions = Weightedknn(train_features, train_target, test_features, k)
    allResults.append(accuracy(test_target, test_predictions))
    acc = accuracy(test_target, test_predictions)
    print('Model accuracy ' , k , '=', acc*100)

sns.set_style("darkgrid")
plt.plot( list(range(3, 40, 2)), allResults)    
plt.show()


######################################## MANHATTAN DISTANCE ###########################################################

def manhattanDistance(dataSet, query_point):
    return sum(abs(e1-e2) for e1, e2 in zip(dataSet,query_point))


def distance_from_all_training(test_point):
    dist_array = np.array([])
    for train_point in train_features:
        dist = manhattanDistance(test_point, train_point)
        dist_array = np.append(dist_array, dist)
    return dist_array





####################################### NORMALIZED MINMAX ########################################################

normalized_test_features = (test_features - np.min(test_features)) / (np.max(test_features) - np.min(test_features))
normalized_test_target = (test_target - np.min(test_target)) / (np.max(test_target) - np.min(test_target))
normalized_train_features = (train_features - np.min(train_features)) / (np.max(train_features) - np.min(train_features))
normalized_train_target = (train_target - np.min(train_target)) / (np.max(train_target) - np.min(train_target))


def Normalizedknn(normalized_train_features, normalized_train_target, normalized_test_features, k):

    predictions = np.array([])
    normalized_train_target = normalized_train_target.reshape(-1,1)
    for test_point in normalized_test_features: # iterating through every test data point 
        dist_array = distance_from_all_training(test_point).reshape(-1,1) # calculating distance from every training data instance
        neighbors = np.concatenate((dist_array, normalized_train_target), axis = 1) 
        neighbors_sorted = neighbors[neighbors[:, 0].argsort()] # sorts training points on the basis of distance
        k_neighbors = neighbors_sorted[:k] # selects k-nearest neighbors
        frequency = np.unique(k_neighbors[:, 1], return_counts=True)
        target_class = frequency[0][frequency[1].argmax()] # selects label with highest frequency
        predictions = np.append(predictions, target_class)

    return predictions

def accuracy(y_test, y_preds):
    correctClassifications = 0
    for i in range(len(y_test)):
        if int(y_test[i]) == int(y_preds[i]):
            correctClassifications += 1
    acc = correctClassifications/len(y_test)
    return acc

allResults = []
for k in range(3, 40, 2):
    test_predictions = Normalizedknn(normalized_train_features, normalized_train_target, normalized_test_features, k)
    allResults.append(accuracy(normalized_test_target, test_predictions))
    acc = accuracy(normalized_test_target, test_predictions)
    print('Model accuracy ' , k , '=', acc*100)

sns.set_style("darkgrid")
plt.plot( list(range(3, 40, 2)), allResults)    
plt.show()



############################################ Z-Score Implementation ###################################################

def standardScaler(feature_array):
    
    total_cols = feature_array.shape[0] # total number of columns 
    for i in range(total_cols): # iterating through each column
        feature_col = feature_array[:, i]
        mean = feature_col.mean() # mean stores mean value for the column
        std = feature_col.std() # std stores standard deviation value for the column
        feature_array[:, i] = (feature_array[:, i] - mean) / std # standard scaling of each element of the column
    return feature_array

train_features_scaled = standardScaler(train_features) 
test_features_scaled = standardScaler(test_features) 
train_target_scaled = standardScaler(train_target) 
test_target_scaled = standardScaler(test_target) 

def Scaledknn(train_features_scaled, train_target_scaled, test_features_scaled, k):

    predictions = np.array([])
    train_target_scaled = train_target_scaled.reshape(-1,1)
    for test_point in test_features_scaled: # iterating through every test data point 
        dist_array = distance_from_all_training(test_point).reshape(-1,1) # calculating distance from every training data instance
        neighbors = np.concatenate((dist_array, train_target_scaled), axis = 1) 
        neighbors_sorted = neighbors[neighbors[:, 0].argsort()] # sorts training points on the basis of distance
        k_neighbors = neighbors_sorted[:k] # selects k-nearest neighbors
        frequency = np.unique(k_neighbors[:, 1], return_counts=True)
        target_class = frequency[0][frequency[1].argmax()] # selects label with highest frequency
        predictions = np.append(predictions, target_class)

    return predictions

def accuracy(y_test, y_preds):
    correctClassifications = 0
    for i in range(len(y_test)):
        if int(y_test[i]) == int(y_preds[i]):
            correctClassifications += 1
    acc = correctClassifications/len(y_test)
    return acc

allResults = []
for k in range(3, 40, 2):
    test_predictions = Scaledknn(train_features_scaled, train_target_scaled, test_features_scaled, k)
    allResults.append(accuracy(test_target_scaled, test_predictions))
    acc = accuracy(test_target_scaled, test_predictions)
    print('Model accuracy ' , k , '=', acc*100)

sns.set_style("darkgrid")
plt.plot( list(range(3, 40, 2)), allResults)    
plt.show()

'''