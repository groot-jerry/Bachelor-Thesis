import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import (
    accuracy_score, f1_score, precision_score, recall_score,
    roc_auc_score, roc_curve, auc, confusion_matrix,
    matthews_corrcoef, average_precision_score
)

# --------------------------
# PATHS AND MODEL LOADING
# --------------------------
model_path = r"E:\Tithi_Banik\Code\VGG19__Tithi_Model.h5"
image_dir = r"E:\Tithi_Banik\Classified_Datasets\Test_Images"
csv_path = r"E:\Tithi_Banik\Classified_Datasets\Test_Images_Labeled_CSV.csv"

# Load model
model = load_model(model_path)

# Load CSV
test_set = pd.read_csv(csv_path)
test_set["image_full_path"] = test_set["image_id"].apply(lambda x: os.path.join(image_dir, x))
labels = test_set["label"].values

# --------------------------
# IMAGE PREPROCESSING
# --------------------------
def preprocess_image(image_path, target_size=(224,224)):
    image = load_img(image_path, target_size=target_size)
    image = img_to_array(image) / 255.0
    return image

# Load and preprocess images
images = []
valid_labels = []
for i, img_path in enumerate(test_set["image_full_path"]):
    if os.path.exists(img_path):
        images.append(preprocess_image(img_path))
        valid_labels.append(labels[i])

images = np.array(images)
labels = np.array(valid_labels)
labels_one_hot = to_categorical(labels, num_classes=model.output_shape[1])

# --------------------------
# PREDICTIONS
# --------------------------
predictions = model.predict(images)
predicted_classes = np.argmax(predictions, axis=1)

# --------------------------
# METRICS CALCULATION
# --------------------------
accuracy = accuracy_score(labels, predicted_classes)
f1 = f1_score(labels, predicted_classes, average="weighted")
precision = precision_score(labels, predicted_classes, average="weighted")
recall = recall_score(labels, predicted_classes, average="weighted")
auc_roc = roc_auc_score(labels_one_hot, predictions, multi_class="ovr")
mcc = matthews_corrcoef(labels, predicted_classes)
map_score = average_precision_score(labels_one_hot, predictions, average="macro")

# Class-wise metrics calculation
classwise_metrics = []
classwise_accuracies = []
sensitivity_per_class = []
specificity_per_class = []
fpr_per_class = []

for i in np.unique(labels):
    binary_labels = (labels == i).astype(int)
    binary_predictions = (predicted_classes == i).astype(int)
    tn, fp, fn, tp = confusion_matrix(binary_labels, binary_predictions).ravel()
    
    sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0  
    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0  
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0  
    support = np.sum(binary_labels)  
    accuracy_per_class = accuracy_score(binary_labels, binary_predictions)

    classwise_metrics.append([i, support, sensitivity, specificity, fpr, accuracy_per_class])
    sensitivity_per_class.append(sensitivity)
    specificity_per_class.append(specificity)
    fpr_per_class.append(fpr)
    classwise_accuracies.append(accuracy_per_class)

# Compute overall averages
average_sensitivity = np.mean(sensitivity_per_class)
average_specificity = np.mean(specificity_per_class)
average_fpr = np.mean(fpr_per_class)
average_classwise_accuracy = np.mean(classwise_accuracies)

# Convert class-wise metrics to DataFrame
classwise_df = pd.DataFrame(
    classwise_metrics, 
    columns=["Class", "Support", "Sensitivity", "Specificity", "FPR", "Class Accuracy"]
)

# --------------------------
# PRINT METRICS
# --------------------------
print(f"Overall Accuracy: {accuracy:.4f}")
print(f"F1 Score: {f1:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall (Sensitivity): {recall:.4f}")
print(f"AUC-ROC: {auc_roc:.4f}")
print(f"Matthews Correlation Coefficient (MCC): {mcc:.4f}")
print(f"Mean Average Precision (MAP): {map_score:.4f}")
print(f"Average Accuracy: {average_classwise_accuracy:.4f}")
print(f"Average Sensitivity (Recall): {average_sensitivity:.4f}")
print(f"Average Specificity: {average_specificity:.4f}")
print(f"Average False Positive Rate (FPR): {average_fpr:.4f}")

# Print class-wise metrics as a table
print("\nClass-wise Metrics:")
print(classwise_df.to_string(index=False))

# --------------------------
# METRICS VISUALIZATION (Improved Bar Chart)
# --------------------------
metrics = {
    "Accuracy": accuracy,
    "F1 Score": f1,
    "Precision": precision,
    "Recall (Sensitivity)": recall,
    "Specificity": average_specificity,
    "FPR": average_fpr,
    "AUC-ROC": auc_roc,
    "MCC": mcc,
    "MAP": map_score,
    "Average Accuracy": average_classwise_accuracy,
}

colors = [
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728",
    "#9467bd", "#8c564b", "#e377c2", "#7f7f7f",
    "#bcbd22", "#17becf", "#ff69b4"
]

plt.figure(figsize=(12, 6))
bars = plt.bar(metrics.keys(), metrics.values(), color=colors, edgecolor='black')
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2.0, yval + 0.01, f"{yval:.2f}", ha='center', va='bottom', fontsize=9)

plt.xticks(rotation=45, ha='right', fontsize=10)
plt.title("Model Evaluation Metrics (Distinct Colors)")
plt.ylabel("Scores")
plt.ylim(0, 1.05)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()

# --------------------------
# ROC CURVE PLOT
# --------------------------
fpr, tpr, roc_auc = {}, {}, {}
for i in range(predictions.shape[1]):
    fpr[i], tpr[i], _ = roc_curve(labels_one_hot[:, i], predictions[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

plt.figure()
for i in range(predictions.shape[1]):
    plt.plot(fpr[i], tpr[i], label=f"Class {i} (AUC = {roc_auc[i]:.2f})")
plt.plot([0, 1], [0, 1], "k--", lw=2)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend(loc="lower right")
plt.show()

# --------------------------
# CONFUSION MATRIX
# --------------------------
conf_matrix = confusion_matrix(labels, predicted_classes)
plt.figure(figsize=(8, 5))
sns.heatmap(
    conf_matrix, annot=True, fmt="d", cmap="Blues",
    xticklabels=np.unique(labels), yticklabels=np.unique(labels)
)
plt.title("Confusion Matrix")
plt.xlabel("Predicted Labels")
plt.ylabel("True Labels")
plt.show()
