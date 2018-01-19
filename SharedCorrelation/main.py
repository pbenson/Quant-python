import random
import matplotlib.pyplot as plt

n = 10
rho = 0.5
num_sims = 10000
beta = rho**0.5
alpha = (1 -rho)**0.5

# run simulation
histogram = [0] * (n+1)
trial_results = []
for _ in range(num_sims):
    M = random.gauss(0, 1)
    K = 0 # number of variables that are > 0
    for _ in range(n):
        R_i = beta * M + alpha * random.gauss(0, 1)
        if R_i > 0:
            K += 1
    histogram[K] += 1
    trial_results.append(K)

print(histogram)
plt.hist(trial_results, bins=n+1, normed=0, align='mid')
plt.title('Distribution of Defaults in ' + str(num_sims) + ' trials')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
