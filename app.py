import math
import scipy.stats as stats
import matplotlib.pyplot as plt

# Step 1: Take input from the user
print("A/B Testing Analysis")

n_A = int(input("Enter the number of users in Group A: "))
conv_A = int(input("Enter the number of conversions in Group A: "))

n_B = int(input("Enter the number of users in Group B: "))
conv_B = int(input("Enter the number of conversions in Group B: "))

# Step 2: Calculate conversion rates
cr_A = conv_A / n_A
cr_B = conv_B / n_B

# Step 3: Perform Z-Test
p_pooled = (conv_A + conv_B) / (n_A + n_B)
std_error = math.sqrt(p_pooled * (1 - p_pooled) * (1/n_A + 1/n_B))
z_score = (cr_B - cr_A) / std_error
p_value = 1 - stats.norm.cdf(z_score)  # One-tailed test

# Step 4: Confidence Interval (95%)
margin_error = 1.96 * std_error
conf_low = (cr_B - cr_A) - margin_error
conf_high = (cr_B - cr_A) + margin_error

# Step 5: Print results
print("\n--- Results ---")
print(f"Conversion Rate of Group A: {cr_A:.2%}")
print(f"Conversion Rate of Group B: {cr_B:.2%}")
print(f"Z-Score: {z_score:.4f}")
print(f"P-Value: {p_value:.4f}")
print(f"95% Confidence Interval: [{conf_low:.4%}, {conf_high:.4%}]")

# Step 6: Conclusion
alpha = 0.05
if p_value < alpha:
    print("Conclusion: The difference is statistically significant. Group B performs better.")
else:
    print("Conclusion: The difference is not statistically significant. No strong evidence that Group B performs better.")

# Step 7: Plot the results
labels = ['Group A', 'Group B']
rates = [cr_A, cr_B]
colors = ['lightblue', 'lightgreen']

plt.bar(labels, rates, color=colors)
plt.ylabel('Conversion Rate')
plt.title('Comparison of Conversion Rates')
plt.ylim(0, max(cr_A, cr_B) + 0.1)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
