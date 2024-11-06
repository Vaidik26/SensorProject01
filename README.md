## Sensor Fault Detection Project

## Project Description

In electronics manufacturing, a wafer is a thin slice of semiconductor material, like crystalline silicon, used to fabricate integrated circuits and solar cells. Wafers act as substrates or foundations upon which microelectronic devices are built. During wafer fabrication, hundreds or even thousands of identical circuits are created for use in devices like computers, smartphones, and more.

This project aims to predict the quality of semiconductor wafers, classifying them as either "Good" or "Bad" based on sensor readings captured during the wafer fabrication process. Early detection of defective wafers can improve manufacturing efficiency, enhance product quality, and reduce waste.

## Problem Statement

Objective: Develop a machine learning model to classify semiconductor wafers as "Good" or "Bad" based on sensor data collected during the fabrication process.

## Data Details

Inputs (Features): 590 sensor readings (e.g., Sensor-1, Sensor-2, ... Sensor-590) per wafer. These readings capture environmental and process parameters.
Output (Target): "Good" (1) or "Bad" (-1), indicating the quality of the wafer.
Goal: To create a classification model that accurately predicts wafer quality based on sensor readings.
Project Goal

The main goal of this project is to develop a machine learning classification model that can help in:

Early detection of faulty wafers.
Improving yield in semiconductor manufacturing.
Reducing waste by identifying defects early in the production process.
Machine Learning Approach
Task Type: Supervised Learning
Model Type: Binary Classification Model
Features and Functionality
Data Preprocessing: Handles missing values, normalizes data, and extracts relevant features.
Model Training: Uses multiple classification algorithms to identify the best model for this task.
Evaluation Metrics: Analyzes model performance with metrics like accuracy, precision, recall, and F1-score.
Visualization: Provides insights into sensor readings and wafer quality distribution.
Technologies Used
Python: Core language for implementation.
Pandas: For data manipulation and analysis.
NumPy: For numerical computations.
Scikit-Learn: For building and evaluating machine learning models.
Matplotlib & Seaborn: For data visualization.

## Installation and Setup

## Clone the repository:
git clone https://github.com/yourusername/Sensor-Fault-Detection.git
cd Sensor-Fault-Detection

## Install the required packages:
bash
pip install -r requirements.txt

## Run the project:
python main.py

## Usage
Load Dataset: Ensure your sensor data is formatted correctly (590 features + target).
Train Model: Train the classification model with your data.
Predict: Use the trained model to classify new wafer data as "Good" or "Bad."

## Project Structure
data/: Directory for datasets.
src/: Main source code for data processing, model training, and evaluation.
models/: Saved models.
notebooks/: Jupyter notebooks for exploratory data analysis and prototyping.
README.md: Project documentation.

## License
This project is licensed under the MIT License.

## Contact
For questions or collaboration, feel free to reach out at vaidiky90@gmail.com.
