# Import libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
import joblib
from sklearn import datasets

# Get the dataset
dataset = datasets.load_iris()

# Split the dataset into features and labels
X = dataset.data
y = dataset.target

# Split the dataset into training (80%) and testing (20%) data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0, shuffle = True)

# Build the