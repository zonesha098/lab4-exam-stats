import pandas as pd
from scipy.stats import skew, kurtosis

# Store exam scores of 10 students
scores = pd.Series(
    [78, 85, 92, 67, 88, None, 74, 95, None, 81],
    name="Exam Scores"
)

print("Original Exam Scores:")
print(scores)

# Display descriptive statistics
print("\n--- Descriptive Statistics ---")
print(scores.describe())

# Calculate skewness and kurtosis after dropping missing values
clean_scores = scores.dropna()

print("\n--- Distribution Shape ---")
print("Skewness:", skew(clean_scores))
print("Kurtosis:", kurtosis(clean_scores))

# Count missing values
print("\n--- Missing Values ---")
print("Number of missing scores:", scores.isnull().sum())

# Fill missing scores with the mean
mean_score = scores.mean()
completed_scores = scores.fillna(mean_score)

print("\nMean Score:", mean_score)

print("\n--- Completed Exam Scores ---")
print(completed_scores)