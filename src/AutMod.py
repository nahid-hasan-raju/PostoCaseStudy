import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

# Configuration parameters
dt = 0.001  # time step
total_time = 10.0  # simulate for 10 seconds
x0 = 0.5  # starting x
y0 = 0.5  # starting y

# Logging settings
log_chance = 0.2  # 20% chance to log each step
noise_level = 0.05  # how much noise in measurements

# Safety limits
x_limit = 3.0
y_limit = 3.0
max_distance = 5.0


def simulate_system(x_start, y_start, time_total, time_step):
    """
    Run the simulation from starting point using discrete time steps
    Implements: x[i+1] = x[i] + dt*(-y[i] - 1.5*x[i] - 1.5*x[i]^2)
                y[i+1] = y[i] + dt*(3*x[i]^2 - y[i])
    Returns lists of time, x, and y values
    """
    # Set up storage for results
    times = [0]
    x_values = [x_start]
    y_values = [y_start]
    
    # Calculate number of steps
    num_steps = int(time_total / time_step)
    
    # Run simulation using discrete steps with index i
    for i in range(num_steps):
        # current values at step i
        x_i = x_values[i]
        y_i = y_values[i]
        
        #  values are getting too big
        if abs(x_i) > 100 or abs(y_i) > 100:
            print(f"Warning: Values too large at step {i}, stopping simulation")
            break
        
        # Calculate x[i+1] using the equation
        x_next = x_i + dt * (-y_i - 1.5*x_i - 1.5*x_i**2)
        
        # Calculate y[i+1] using the equation
        y_next = y_i + dt * (3*x_i**2 - y_i)
        
        x_values.append(x_next)
        y_values.append(y_next)
        times.append((i+1) * time_step)
    
    return times, x_values, y_values


def create_logs(times, x_vals, y_vals, probability):
    """
    randomly sampling from the trajectory
    Adds some noise to simulate measurement errors
    """
    logs = []
    
    for i in range(len(times)):
        # Randomly decide if we log this point= 20%
        if random.random() < probability:
            # Add some measurement noise
            x_noisy = x_vals[i] + random.gauss(0, noise_level)
            y_noisy = y_vals[i] + random.gauss(0, noise_level)
            
            log_entry = {
                'step': i,
                'time': times[i],
                'x': x_noisy,
                'y': y_noisy,
                'x_true': x_vals[i],
                'y_true': y_vals[i]
            }
            logs.append(log_entry)
    
    return logs


def check_safety(times, x_vals, y_vals):
    """
    Check if the trajectory violates any safety constraints
    """
    violations = []
    
    for i in range(len(times)):
        t = times[i]
        x = x_vals[i]
        y = y_vals[i]
        
        # Check x bounds
        if x < -x_limit or x > x_limit:
            violations.append(f"X violation at step {i} (t={t:.2f}s): x={x:.2f}")
        
        # Check y bounds
        if y < -y_limit or y > y_limit:
            violations.append(f"Y violation at step {i} (t={t:.2f}s): y={y:.2f}")
        
        # Check distance from origin
        dist = np.sqrt(x**2 + y**2)
        if dist > max_distance:
            violations.append(f"Distance violation at step {i} (t={t:.2f}s): dist={dist:.2f}")
    
    return violations


def plot_3d_trajectory(times, x_vals, y_vals):
    """
    Plot the trajectory in 3D with time on the z-axis
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot the path
    ax.plot(x_vals, y_vals, times, 'b-', linewidth=2)
    
    # Mark start and end
    ax.scatter([x_vals[0]], [y_vals[0]], [times[0]], 
              color='green', s=100, label='Start')
    ax.scatter([x_vals[-1]], [y_vals[-1]], [times[-1]], 
              color='red', s=100, label='End')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Time (seconds)')
    ax.set_title('AutMod System Trajectory')
    ax.legend()
    plt.show()


def plot_phase_portrait(x_vals, y_vals):
    """
    Plot x vs y (phase portrait)
    """
    plt.figure(figsize=(8, 8))
    plt.plot(x_vals, y_vals, 'b-', linewidth=1.5)
    plt.plot(x_vals[0], y_vals[0], 'go', markersize=10, label='Start')
    plt.plot(x_vals[-1], y_vals[-1], 'rx', markersize=10, label='End')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Phase Portrait')
    plt.grid(True)
    plt.legend()
    plt.show()


def plot_time_series(times, x_vals, y_vals):
    """
    Plot x and y over time
    """
    plt.figure(figsize=(10, 6))
    
    plt.subplot(2, 1, 1)
    plt.plot(times, x_vals, 'b-', linewidth=1.5)
    plt.ylabel('X')
    plt.title('State Variables Over Time')
    plt.grid(True)
    
    plt.subplot(2, 1, 2)
    plt.plot(times, y_vals, 'r-', linewidth=1.5)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Y')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()


def plot_logs_vs_true(times, x_vals, y_vals, logs):
    """
    Compare logged measurements with true values
    """
    # Extract log data
    log_times = [log['time'] for log in logs]
    log_x = [log['x'] for log in logs]
    log_y = [log['y'] for log in logs]
    
    plt.figure(figsize=(10, 6))
    
    plt.subplot(2, 1, 1)
    plt.plot(times, x_vals, 'b-', linewidth=2, alpha=0.7, label='True X')
    plt.scatter(log_times, log_x, c='red', s=10, label='Logged X')
    plt.ylabel('X')
    plt.title('Logged vs True Values')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(2, 1, 2)
    plt.plot(times, y_vals, 'g-', linewidth=2, alpha=0.7, label='True Y')
    plt.scatter(log_times, log_y, c='red', s=10, label='Logged Y')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()


# ============================================================================------------------=============
# MAIN Function

print("="*60)
print("AutMod System Simulation")
print("="*60)

# Basic simulation
print("\n1. Running simulation...")
print(f"   Starting at x[0]={x0}, y[0]={y0}")
print(f"   Time step dt: {dt}s, Total time: {total_time}s")

times, x_vals, y_vals = simulate_system(x0, y0, total_time, dt)

print(f"   Completed {len(times)} steps")
print(f"   Final position: x[{len(x_vals)-1}]={x_vals[-1]:.3f}, y[{len(y_vals)-1}]={y_vals[-1]:.3f}")

#  Generate logs
print("\n2. Generating logs...")
logs = create_logs(times, x_vals, y_vals, log_chance)
print(f"   Created {len(logs)} log entries")
# print(f"   That's {len(logs)/len(times)*100:.1f}% of all points")

# # Some example logs
# print("\n   Sample logs:")
# for i in range(min(5, len(logs))):
#     log = logs[i]
#     print(f"   Step {log['step']}: t={log['time']:.3f}s, x={log['x']:.3f}, y={log['y']:.3f}")

#  Safety monitoring
print("\n3. Checking safety constraints......")
violations = check_safety(times, x_vals, y_vals)

if len(violations) == 0:
    print("  No safety violations detected!")
else:
    print(f"  Found {len(violations)} violations:")
    for v in violations[:5]:  # show first 5
        print(f"   - {v}")
    if len(violations) > 5:
        print(f"   ..... and {len(violations)-5} more")

# Multiple trajectories
print("\n4. Generating multiple random trajectories....")
num_trajectories = 3

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['blue', 'red', 'green', 'orange', 'purple']

for traj_num in range(num_trajectories):
    # Random starting point
    x_start = random.uniform(-0.5, 0.5)
    y_start = random.uniform(-0.5, 0.5)
    
    print(f"   Trajectory {traj_num+1}: x[0]={x_start:.2f}, y[0]={y_start:.2f}")
    
    # Run simulation
    t, x, y = simulate_system(x_start, y_start, total_time, dt)
    
    # Plot in 3D
    ax.plot(x, y, t, color=colors[traj_num], linewidth=2, label=f'Traj {traj_num+1}')
    ax.scatter([x[0]], [y[0]], [t[0]], color=colors[traj_num], s=50)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Time (seconds)')
ax.set_title('Multiple Trajectories')
ax.legend()
plt.show()

# Show visualizations for main trajectory
print("\n5. Creating visualizations...")
print("   - 3D trajectory plot")
plot_3d_trajectory(times, x_vals, y_vals)

print("   - Phase portrait")
plot_phase_portrait(x_vals, y_vals)

print("   - Time series")
plot_time_series(times, x_vals, y_vals)

print("   - Logs comparison")
plot_logs_vs_true(times, x_vals, y_vals, logs)

print("\n" + "="*60)
print("All experiments complete!")
print("="*60)