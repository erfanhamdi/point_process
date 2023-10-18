# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define the Strauss point process function
def strauss_pp(lam, alpha, beta, r, n):
    # Initialize empty list to store points
    points = []
    
    # Generate first point randomly
    x = np.random.uniform(0, 1)
    y = np.random.uniform(0, 1)
    points.append((x, y))
    
    # Generate subsequent points
    for i in range(1, n):
        # Generate candidate point
        x_cand = np.random.uniform(0, 1)
        y_cand = np.random.uniform(0, 1)
        
        # Calculate distance to existing points
        dists = [np.sqrt((x_cand - p[0])**2 + (y_cand - p[1])**2) for p in points]
        
        # Calculate probability of accepting candidate point
        p_accept = lam * (beta / (alpha + len(points)))**sum([1 for d in dists if d < r])
        
        # Accept or reject candidate point
        if np.random.uniform(0, 1) < p_accept:
            points.append((x_cand, y_cand))
    
    return points

# Set parameters
lam = 10
alpha = 1
beta = 1
r = 0.1
n = 1000

# Generate Strauss point process
points = strauss_pp(lam, alpha, beta, r, n)

# Plot points
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter([p[0] for p in points], [p[1] for p in points], s=5)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.show()
