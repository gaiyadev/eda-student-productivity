import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

path="/Users/mac/.cache/kagglehub/datasets/velvetcrystal/student-productivity-dataset/versions/1"
df = pd.read_csv(os.path.join(path, "Student_Productivity_Dataset.csv"))

# 1. Performance Category Distribution
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Performance_Category', order=['High', 'Medium', 'Low'], palette='viridis')
plt.title('Performance Category Distribution')
plt.savefig('performance_distribution.png')
plt.close()

# 2. Correlation Heatmap
numeric_cols = df.select_dtypes(include=['number']).columns
plt.figure(figsize=(12, 10))
sns.heatmap(df[numeric_cols].corr(), annot=False, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
plt.close()

# 3. Performance Category by Gender
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Gender', hue='Performance_Category', hue_order=['High', 'Medium', 'Low'], palette='viridis')
plt.title('Performance Category Distribution by Gender')
plt.savefig('performance_by_gender.png')
plt.close()

print("Plots generated successfully!")
