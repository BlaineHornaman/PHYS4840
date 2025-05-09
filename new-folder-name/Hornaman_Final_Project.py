#!/usr/bin/python3.12
#####################################
#
# PHYS 4840 Final Project: Using RK4 to Model Circular Planetary Orbits Arond a Star
# Author: Blaine Hornaman
#
#####################################

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to calculate gravitational forces between celestial bodies
def gravitational_force(positions, masses, G = 6.67e-11):
    n = len(masses)
    forces = np.zeros_like(positions)
    
    for i in range(n):
        for j in range(n):
            if i != j:
                r_vector = positions[j] - positions[i]
                distance = np.linalg.norm(r_vector)
                force_magnitude = G * masses[i] * masses[j] / distance**2
                forces[i] += force_magnitude * r_vector / distance
                
    return forces

# RK4 function
def rk4_step(y, dt, masses):
    
    # Function to calculate the derivatives that are needed
    def derivatives(y, masses):
        n = len(masses)
        positions = y[:n]
        velocities = y[n:]
        forces = gravitational_force(positions, masses)
        dpdt = velocities
        dvdt = forces / masses[:, None]
        return np.concatenate([dpdt, dvdt])

    # k steps for RK4
    k1 = derivatives(y, masses)
    k2 = derivatives(y + 0.5 * dt * k1, masses)
    k3 = derivatives(y + 0.5 * dt * k2, masses)
    k4 = derivatives(y + dt * k3, masses)
    
    return y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

# Function to simualte planetary orbits using RK4
def simulate_orbits(positions, velocities, masses, dt, total_time):
    n_steps = int(total_time / dt)
    n_bodies = len(masses)
    trajectory = np.zeros((n_steps, n_bodies, 3))
    
    # Calculating the trajectories
    y = np.concatenate([positions, velocities])
    for step in range(n_steps):
        trajectory[step] = y[:n_bodies]
        y = rk4_step(y, dt, masses)
    
    return trajectory

# Function to calculate the orbital period using Kepler's 3rd Law
def calculate_orbital_period(distance, star_mass, G = 6.67e-11):
    return 2 * np.pi * np.sqrt(distance**3 / (G * star_mass))

# Function to input the inclination angle provided by the user
def add_inclination(position, inclination_angle):
    inclination_angle = np.radians(inclination_angle)
    
    rotation_matrix = np.array([
        [1, 0, 0],
        [0, np.cos(inclination_angle), -np.sin(inclination_angle)],
        [0, np.sin(inclination_angle), np.cos(inclination_angle)]
    ])
    
    return np.dot(rotation_matrix, position)

# Function to set up the system and visualize the planetary oorbits
def main():
   
    # User inputs masses
    star_mass = float(input("Enter the mass of the star (kg): "))
    n_planets = int(input("Enter the number of planets: "))
    masses = [star_mass]

    # Allow user to input distance to star, inclination, and mass depending on number of planets
    distances = []
    inclinations = []
    
    for i in range(n_planets):
        planet_mass = float(input(f"Enter the mass of planet {i+1} (kg): "))
        distance = float(input(f"Enter the distance of planet {i+1} from the star (meters): "))
        inclination = float(input(f"Enter inclination angle of planet {i+1} (degrees): "))
        
        masses.append(planet_mass)
        distances.append(distance)
        inclinations.append(inclination)

    masses = np.array(masses)

    # Setting up initial positions and velocities
    positions = [np.array([0.0, 0.0, 0.0])] 
    velocities = [np.array([0.0, 0.0, 0.0])] 

    # Finding and appending values of the orbit speed, position, and orbital period
    orbital_periods = []
    
    for i in range(n_planets):
        speed = np.sqrt(6.67e-11 * star_mass / distances[i])  
        
        position = np.array([distances[i], 0.0, 0.0])
        position = add_inclination(position, inclinations[i]) 
         
        positions.append(position)
        velocities.append(np.array([0.0, speed, 0.0]))
        orbital_periods.append(calculate_orbital_period(distances[i], star_mass))

    # Putting positions and velocities into arrays
    positions = np.array(positions)
    velocities = np.array(velocities)

    # Set simulation time to cover at least one full orbit for the farthest planet
    total_time = max(orbital_periods)
    
    # Setting a reasonable time step for relatively small computational time
    dt = total_time / 10000  

    # Simulate orbits
    trajectory = simulate_orbits(positions, velocities, masses, dt, total_time)

    # Plot the orbits
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    ax.set_title('3D Planetary Orbits Around a Star')

    n_steps = trajectory.shape[0]
    
    for body in range(len(masses)):
        orbit = trajectory[:, body, :]
        ax.plot(orbit[:, 0], orbit[:, 1], orbit[:, 2], label = f'Body {body}')

    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Z (m)')
    ax.legend()
    plt.savefig("Final_Project.png")

if __name__ == "__main__":
    main()