import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
import os

sys.path.insert(0, os.environ['MNTR_BB_ROOT_DIR'])
from src.AutMod import AutMod

def generate_trajectory(model, seed=None):
    """Generate a random trajectory"""
    if seed is not None:
        np.random.seed(seed)
    
    # Sample initial state
    x0 = np.array([
        np.random.uniform(*model.initial_set['x0']),
        np.random.uniform(*model.initial_set['x1'])
    ])
    
    # Generate trajectory
    trajectory = [x0]
    state = x0.copy()
    
    for t in range(model.T):
        # Sample disturbance
        eps = np.array([
            np.random.uniform(*model.disturbances['eps0']),
            np.random.uniform(*model.disturbances['eps1'])
        ])
        
        # Take step
        state = model.step(state, eps)
        trajectory.append(state.copy())
    
    return np.array(trajectory)

def plot_3d_trajectory(trajectory, title="AutMod Trajectory"):
    """Plot trajectory in 3D"""
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    time = np.arange(len(trajectory))
    x0 = trajectory[:, 0]
    x1 = trajectory[:, 1]
    
    ax.plot(x0, x1, time, 'b-', linewidth=1.5, alpha=0.7)
    ax.scatter(x0[0], x1[0], 0, c='green', s=100, label='Start')
    ax.scatter(x0[-1], x1[-1], time[-1], c='red', s=100, label='End')
    
    ax.set_xlabel('State x0', fontsize=12)
    ax.set_ylabel('State x1', fontsize=12)
    ax.set_zlabel('Time', fontsize=12)
    ax.set_title(title, fontsize=14)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('results/plots/trajectory_3d.png', dpi=300)
    plt.show()

if __name__ == '__main__':
    # Create model
    model = AutMod()
    
    # Generate and plot trajectory
    print("Generating trajectory...")
    trajectory = generate_trajectory(model, seed=42)
    
    print(f"Trajectory shape: {trajectory.shape}")
    print(f"Initial state: {trajectory[0]}")
    print(f"Final state: {trajectory[-1]}")
    
    plot_3d_trajectory(trajectory)