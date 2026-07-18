# Rice Leaf Disease Recognition Using Deep Learning Model and Explainable AI

##  Project Overview

This undergraduate thesis presents an intelligent deep learning-based system for the automatic recognition of rice leaf diseases using image classification techniques and Explainable Artificial Intelligence (XAI). The research aims to improve the accuracy, transparency, and interpretability of disease prediction, enabling users to understand the reasoning behind the model's decisions.

The proposed system leverages state-of-the-art convolutional neural networks (CNNs) for feature extraction and classification while incorporating explainability methods such as **Grad-CAM** to visualize the regions of rice leaves that influence the model's predictions.

---

##  Objectives

* Develop a deep learning model for automatic rice leaf disease recognition.
* Improve disease detection accuracy using transfer learning techniques.
* Apply Explainable AI (XAI) methods to interpret model predictions.
* Evaluate model performance using standard classification metrics.
* Provide an efficient and reliable solution for precision agriculture.

---

##  Features

* 🌾 Automatic rice leaf disease classification
* 🧠 Deep Learning-based image recognition
* 📊 Explainable AI (Grad-CAM) visualization
* 📈 Model performance evaluation
* 🔍 Image preprocessing and augmentation
* 📉 Training and validation performance visualization
* 📋 Confusion matrix and classification report generation

---

##  Technologies Used

### Programming Language

* Python

### Deep Learning Frameworks

* TensorFlow
* Keras

### Libraries

* OpenCV
* NumPy
* Pandas
* Matplotlib
* Scikit-learn

### Explainable AI

* Grad-CAM

### Development Environment

* Google Colab
* Jupyter Notebook
* Visual Studio Code

---

## 📂 Project Structure

```text
Rice-Leaf-Disease-Recognition/

├── dataset/
├── notebooks/
│   ├── data_preprocessing.ipynb
│   ├── model_training.ipynb
│   ├── evaluation.ipynb
│   └── gradcam_visualization.ipynb
│
├── models/
│
├── results/
│   ├── confusion_matrix.png
│   ├── accuracy_plot.png
│   ├── loss_plot.png
│   └── gradcam_results/
│
├── requirements.txt
├── README.md
└── thesis.pdf
```

---

##  Methodology

### 1. Data Collection

* Collect rice leaf images from publicly available datasets.
* Organize images by disease category.

### 2. Data Preprocessing

* Resize images.
* Normalize pixel values.
* Perform data augmentation.
* Split data into training, validation, and testing sets.

### 3. Model Development

* Train a deep learning model using transfer learning.
* Fine-tune the network for improved classification performance.

### 4. Model Evaluation

Evaluate the model using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

### 5. Explainable AI

Generate Grad-CAM heatmaps to highlight the image regions that contributed most to each prediction, improving model interpretability.

---

##  Model Performance

The trained model is evaluated using the following metrics:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* Training & Validation Loss
* Training & Validation Accuracy

---

##  Results

The project includes visualizations such as:

* Sample disease predictions
* Accuracy and loss curves
* Confusion matrix
* Grad-CAM heatmaps
* Model prediction examples

---

##  Learning Outcomes

This research provided practical experience in:

* Deep Learning
* Computer Vision
* Image Classification
* Transfer Learning
* Explainable Artificial Intelligence (XAI)
* Model Evaluation
* Data Preprocessing
* Python for Machine Learning
* Scientific Research and Experimentation

---

##  Future Improvements

* Deploy the model as a web or mobile application.
* Expand support for additional crop diseases.
* Integrate real-time field image analysis.
* Explore lightweight models for edge devices.
* Compare multiple XAI techniques (e.g., LIME and SHAP).
* Develop a cloud-based disease monitoring platform.

---

##  Author

**Junaed Hossain Jibon**

**Undergraduate Thesis**

Department of Computer Science and Engineering (CSE)

University of Asia Pacific

---

##  Supervisor

**Dr. Nasima Begum**

Associate Professor

Department of Computer Science and Engineering

University of Asia Pacific

---

##  License

This research was conducted as part of the Bachelor of Science in Computer Science and Engineering program at the **University of Asia Pacific**.

---

##  Acknowledgements

* University of Asia Pacific
* Department of Computer Science and Engineering
* Thesis Supervisor
* TensorFlow & Keras Community
* OpenCV Community
* Open Source Contributors
