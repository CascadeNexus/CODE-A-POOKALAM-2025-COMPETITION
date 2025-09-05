import matplotlib.pyplot as plt
import numpy as np

# Prepare circular Attapookalam pattern using programming
fig, ax = plt.subplots(figsize=(8,8))
ax.set_aspect('equal')

# Number of flower petals
num_petals = 12
angle = np.linspace(0, 2 * np.pi, num_petals, endpoint=False)

# Main circle
circle = plt.Circle((0,0), 1, color='gold', fill=True, alpha=0.4)
ax.add_artist(circle)

# Petals in a circle
for i in range(num_petals):
    x = np.cos(angle[i])
    y = np.sin(angle[i])
    petal = plt.Circle((0.7 * x, 0.7 * y), 0.35, color='darkorange', fill=True, alpha=0.8)
    ax.add_artist(petal)
    # Inner dot for flower center
    dot = plt.Circle((0.85 * x, 0.85 * y), 0.07, color='crimson', fill=True, alpha=0.90)
    ax.add_artist(dot)

# Central dot
center_dot = plt.Circle((0,0), 0.13, color='greenyellow', fill=True)
ax.add_artist(center_dot)

ax.set_xlim(-1.3,1.3)
ax.set_ylim(-1.3,1.3)
plt.axis('off')
plt.savefig('attapookalam_code.png')
plt.close()
