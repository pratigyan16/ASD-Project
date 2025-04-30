import pandas as pd
import numpy as np
import random

# Load the cleaned dataset
df = pd.read_csv("../Data/toddler_asd_cleaned.csv")

# 👁️ Print column names to make sure we use the correct one
print("🧾 Column names in dataset:")
print(df.columns.tolist())

# 🎯 Replace with your actual target column name
# ✅ Try with 'Class_ASD_Traits' (usually the diagnosis column)
target_column = "Class_ASD_Traits"

# Split into features and target
X = df.drop(target_column, axis=1)
y = df[target_column]

# Manual train/test split
def train_test_split(X, y, test_size=0.2):
    indices = list(range(len(X)))
    random.shuffle(indices)
    split = int(len(X) * (1 - test_size))
    train_idx, test_idx = indices[:split], indices[split:]
    return X.iloc[train_idx], X.iloc[test_idx], y.iloc[train_idx], y.iloc[test_idx]

X_train, X_test, y_train, y_test = train_test_split(X, y)

# Node class to build the tree
class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

# Function to calculate Gini impurity
def gini(y):
    classes = np.unique(y)
    impurity = 1
    for cls in classes:
        p = np.sum(y == cls) / len(y)
        impurity -= p ** 2
    return impurity

# Function to split dataset
def split_dataset(X, y, feature, threshold):
    left = X[feature] < threshold
    return X[left], X[~left], y[left], y[~left]

# Find best feature and threshold to split
def best_split(X, y):
    best_gini = 1
    best_feature = None
    best_threshold = None

    for feature in X.columns:
        thresholds = X[feature].unique()
        for threshold in thresholds:
            X_left, X_right, y_left, y_right = split_dataset(X, y, feature, threshold)
            if len(y_left) == 0 or len(y_right) == 0:
                continue
            g = (len(y_left)/len(y)) * gini(y_left) + (len(y_right)/len(y)) * gini(y_right)
            if g < best_gini:
                best_gini = g
                best_feature = feature
                best_threshold = threshold
    return best_feature, best_threshold

# Recursively build decision tree
def build_tree(X, y, depth=0, max_depth=5):
    if len(np.unique(y)) == 1:
        return Node(value=np.unique(y)[0])
    if len(y) == 0 or depth >= max_depth:
        return Node(value=np.bincount(y).argmax())

    feature, threshold = best_split(X, y)
    if feature is None:
        return Node(value=np.bincount(y).argmax())

    X_left, X_right, y_left, y_right = split_dataset(X, y, feature, threshold)
    left = build_tree(X_left, y_left, depth + 1, max_depth)
    right = build_tree(X_right, y_right, depth + 1, max_depth)
    return Node(feature, threshold, left, right)

# Predict a single sample
def predict(sample, tree):
    if tree.value is not None:
        return tree.value
    if sample[tree.feature] < tree.threshold:
        return predict(sample, tree.left)
    else:
        return predict(sample, tree.right)

# Build and train the decision tree
tree = build_tree(X_train, y_train.to_numpy())

# Test the tree on test data
predictions = [predict(row, tree) for _, row in X_test.iterrows()]
accuracy = np.mean(predictions == y_test.to_numpy())

# ✅ Output the result
print(f"\n🎯 Decision Tree Accuracy: {accuracy:.2f}")
