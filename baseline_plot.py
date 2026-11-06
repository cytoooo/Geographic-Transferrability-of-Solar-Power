import matplotlib.pyplot as plt

# 1. Define your results
models = ['RF', 'CatBoost', 'XGBoost', 'LR', 'Ridge', 'KNN', 'MLP']
accuracies = [93.46, 93.28, 93.25, 92.14, 92.10, 91.96, 86.46]

# 2. Set up the figure (using floats to prevent editor warnings)
plt.figure(figsize=(10.0, 6.0))

# 3. Create a basic bar chart
bars = plt.bar(models, accuracies, color='skyblue', edgecolor='black')

# 4. Add titles and labels
plt.title('Baseline Model Accuracy Comparison', fontsize=14, fontweight='bold')
plt.xlabel('Regression Model', fontsize=12)
plt.ylabel('Accuracy (%)', fontsize=12)

# Set the Y-axis to scale from 0 to 100
plt.ylim(0, 100)

# 5. Add the exact numbers on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1.5,
             f'{yval:.2f}%', ha='center', va='bottom', fontweight='bold')

# 6. Show the final plot
plt.tight_layout()
plt.show()