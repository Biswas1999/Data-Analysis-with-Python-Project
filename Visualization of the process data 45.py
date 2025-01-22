import pandas as pd
import matplotlib.pyplot as plt
file_path = "E:\\Python class\\Pathogenicity.csv"
data = pd.read_csv(file_path)

# Line chart: Comparison of expected accuracies for the first 10 data points
plt.figure(figsize=(10, 6))
plt.plot(data['PredictSNP expected accuracy'][:10], label='PredictSNP', marker='o')
plt.plot(data['MAPP expected accuracye'][:10], label='MAPP', marker='o')
plt.plot(data['PhD-SNP expected accuracy'][:10], label='PhD-SNP', marker='o')
plt.title('Expected Accuracy Comparison (First 10 Data Points)')
plt.xlabel('Data Point Index')
plt.ylabel('Expected Accuracy')
plt.legend()
plt.grid(True)
plt.show()

# Pie chart: Distribution of the first 10 'SIFT expected accuracy' categories
SIFT_expected_accuracy_counts = data['SIFT expected accuracy'][:10].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(SIFT_expected_accuracy_counts, labels=SIFT_expected_accuracy_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('SIFT expected accuracy Distribution (First 10 Data Points)')
plt.show()

# Histogram: Distribution of 'PredictSNP expected accuracy'
plt.figure(figsize=(8, 6))
plt.hist(data['PredictSNP expected accuracy'], bins=15, color='skyblue', edgecolor='black')
plt.title('Distribution of PredictSNP Expected Accuracy')
plt.xlabel('PredictSNP Expected Accuracy')
plt.ylabel('Frequency')
#plt.grid(True)
plt.show()

# Scatter plot: Correlation between 'PredictSNP expected accuracy' and 'SNAP expected accuracy'
plt.figure(figsize=(8, 6))
plt.scatter(data['PredictSNP expected accuracy'], data['SNAP expected accuracy'], alpha=0.7, color='red')
plt.title('Scatter Plot: PredictSNP vs SNAP Expected Accuracy')
plt.xlabel('PredictSNP Expected Accuracy')
plt.ylabel('SNAP Expected Accuracy')
#plt.grid(True)
plt.show()
