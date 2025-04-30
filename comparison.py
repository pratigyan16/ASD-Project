import numpy as np
import matplotlib.pyplot as plt

# Define the manual metric calculation functions
def accuracy(y_true, y_pred):
    correct = sum(y_true == y_pred)
    total = len(y_true)
    return correct / total

def precision(y_true, y_pred, positive_class=1):
    true_positive = sum((y_true == positive_class) & (y_pred == positive_class))
    predicted_positive = sum(y_pred == positive_class)
    return true_positive / predicted_positive if predicted_positive != 0 else 0

def recall(y_true, y_pred, positive_class=1):
    true_positive = sum((y_true == positive_class) & (y_pred == positive_class))
    actual_positive = sum(y_true == positive_class)
    return true_positive / actual_positive if actual_positive != 0 else 0

def f1_score(y_true, y_pred, positive_class=1):
    precision_val = precision(y_true, y_pred, positive_class)
    recall_val = recall(y_true, y_pred, positive_class)
    return 2 * (precision_val * recall_val) / (precision_val + recall_val) if (precision_val + recall_val) != 0 else 0

def confusion_matrix(y_true, y_pred, num_classes=2):
    cm = np.zeros((num_classes, num_classes), dtype=int)
    for true, pred in zip(y_true, y_pred):
        cm[true][pred] += 1
    return cm

# Sample predictions and true labels (replace with your actual data)
y_true = np.array([0, 1, 0, 1, 1, 0, 1])  # True labels
y_pred_tree = np.array([0, 1, 0, 0, 1, 0, 1])  # Decision Tree predictions
y_pred_nb = np.array([0, 1, 1, 1, 1, 0, 1])  # Naive Bayes predictions

# Calculate metrics for Decision Tree
accuracy_tree = accuracy(y_true, y_pred_tree)
precision_tree = precision(y_true, y_pred_tree)
recall_tree = recall(y_true, y_pred_tree)
f1_tree = f1_score(y_true, y_pred_tree)
cm_tree = confusion_matrix(y_true, y_pred_tree)

# Calculate metrics for Naive Bayes
accuracy_nb = accuracy(y_true, y_pred_nb)
precision_nb = precision(y_true, y_pred_nb)
recall_nb = recall(y_true, y_pred_nb)
f1_nb = f1_score(y_true, y_pred_nb)
cm_nb = confusion_matrix(y_true, y_pred_nb)

# Print the comparison
print(f"Decision Tree - Accuracy: {accuracy_tree}, Precision: {precision_tree}, Recall: {recall_tree}, F1-Score: {f1_tree}")
print(f"Naive Bayes - Accuracy: {accuracy_nb}, Precision: {precision_nb}, Recall: {recall_nb}, F1-Score: {f1_nb}")
print(f"Confusion Matrix - Decision Tree:\n{cm_tree}")
print(f"Confusion Matrix - Naive Bayes:\n{cm_nb}")

# Visualization of the comparison
metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
decision_tree_scores = [accuracy_tree, precision_tree, recall_tree, f1_tree]
naive_bayes_scores = [accuracy_nb, precision_nb, recall_nb, f1_nb]

x = np.arange(len(metrics))  # The label locations
width = 0.35  # The width of the bars

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, decision_tree_scores, width, label='Decision Tree')
rects2 = ax.bar(x + width/2, naive_bayes_scores, width, label='Naive Bayes')

ax.set_ylabel('Scores')
ax.set_title('Model Comparison: Decision Tree vs Naive Bayes')
ax.set_xticks(x)
ax.set_xticklabels(metrics)
ax.legend()

plt.tight_layout()
plt.show()
