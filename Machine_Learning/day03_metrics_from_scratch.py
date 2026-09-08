# Day 3: Machine Learning Metrics From Scratch
# --------------------------------------------
# Problem Statement:
# Given a list of true labels and predicted labels (binary classification),
# write functions to calculate Accuracy, Precision, Recall, and F1-Score WITHOUT using scikit-learn.

def calculate_metrics(y_true, y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError("Length of true and predicted labels must match.")
        
    TP = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 1 and yp == 1)
    TN = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 0 and yp == 0)
    FP = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 0 and yp == 1)
    FN = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 1 and yp == 0)
    
    accuracy = (TP + TN) / len(y_true) if len(y_true) > 0 else 0
    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    
    return {
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1-Score": f1_score
    }

# Test the function
if __name__ == "__main__":
    y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
    y_pred = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]
    
    metrics = calculate_metrics(y_true, y_pred)
    for metric, value in metrics.items():
        print(f"{metric}: {value:.2f}")
