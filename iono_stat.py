import pandas as pd
import numpy as np
from scipy.stats import norm, binom, poisson, bernoulli, ttest_ind, chi2_contingency
import matplotlib.pyplot as plt

# Load the ionopause dataset
df = pd.read_csv("ionopause.csv")

# Calculate the mean, median, and mode of the dataset
mean = df.mean()
median = df.median()
mode = df.mode().iloc[0]  # Mode can be multiple values, so selecting the first one

# Calculate the variance and standard deviation of the dataset
variance = df.var()
standard_deviation = df.std()

# Plot the normal distribution of the dataset
plt.plot(df, norm.pdf(df, mean, standard_deviation))
plt.show()

# Calculate the binomial distribution of the dataset
p = 0.5
k = 5
n = len(df)
binomial_distribution = binom.pmf(k, n, p)

# Plot the binomial distribution of the dataset
plt.plot(np.arange(n), binom.pmf(np.arange(n), n, p))
plt.show()

# Calculate the poisson discrete distribution of the dataset
lambda_ = 10
poisson_distribution = poisson.pmf(np.arange(n), lambda_)

# Plot the poisson discrete distribution of the dataset
plt.plot(np.arange(n), poisson_distribution)
plt.show()

# Calculate the bernoulli distribution of the dataset
p = 0.5
bernoulli_distribution = bernoulli.pmf(np.arange(n), p)

# Plot the bernoulli distribution of the dataset
plt.plot(np.arange(n), bernoulli_distribution)
plt.show()

# Calculate the p-value of the dataset
t_statistic, p_value = ttest_ind(df, np.random.randn(n))

# Print the p-value
print(p_value)

# Calculate the correlation matrix of the dataset
correlation_matrix = df.corr()

# Print the correlation matrix
print(correlation_matrix)

# Perform Pearson's chi-square test of the dataset
chi_square_statistic, p_value, _, _ = chi2_contingency(df)

# Print the p-value
print(p_value)
