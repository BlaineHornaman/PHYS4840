# University of Wyoming PHYS 4840 Final Project: Using RK4 to Model Circular Planetary Orbits Arond a Star
# Author: Blaine Hornaman

# Intro to code
## This code tackles the physics problem of modelling circular planetary orbits using the RK4 integration method (use case).
## The function of this code is to allow the user to input multiple variables:

### Mass of central star
### Number of planets in system
### Radius of each planet from the star
### Masses of the planets
### Inclination of planet's orbit 

## The code uses the gravitational force equation to fine the integrals of velocity and acceleration and uses that to find position values and then uses the RK4 integration method to help iterate those position values over time to make a 3D plot of the system the user has created.
## The code uses Python to do this, and I will be publishing both the code and this README to GitHub.
## This code was made using Linux, specifically Ubuntu.
## List of dependencies:

### numpy
### matplotlib.pyplot
### mpl_toolkits.mplot3d

# How to use the code
## Download the code from GitHub and open your choice of text editor.
## Either move the Python file I have provided to a different directory than your download directory, or use the download directory to run the file.
## You can run the file in a terminal using your preferred command to run the file, or if you have another preferred way to run the file, you can do that as well.
## If you have done these steps correctly, the code should then ask you to input the central star's mass, how many planets you want in your simulation, the masses you want your planets to be, and the radii that you want the planets to be from the central star.
## The units of each veriable are as follows:

### Mass of central star: kilograms
### Mass of planet(s): kilograms
### Radius of orbit of planet(s): meters
### Inclination of each planet's orbits: degrees

## You need to input each of these variables correctly or it will give you an error.
## If everything has been inputed correctly, a 3D plot should be generated showing you the solar system that was made with the variables you inputed.

## NOTE: This code allows you to input as many planets as you want for your solar system, but if you don't want to go through the headache of inputing a lot of variables, I suggest you only choose a small number for your number of planets in your solar system.

## ALSO NOTE: This code numbers each planet from 1 - however many planets you inputed, so if you have actual data you want to input this code, remember or write down which planet is which number in the code so you can input the right numbers in the right variables.

# An Example Using This Code (test case)
# The example I will use is for the solar system we live in if the orbits of the planets were circular (which is not the case)
## The Sun's mass in kilograms is about 2*10^30 kg, so that would be the value of the Sun's mass in the code.
## For the number of planets in the solar system variable, the number I would input is 8 (or if you want Pluto to be a planet), 9.
## Then, when prompted, I would input all of the masses, inclination, and radii from the Sun of each planet:

### Name of planet, Mass, Inclination, Radius from star
### Mercury: 3.30*10^23 kg, 7 degrees, 5.79*10^10 m
### Venus: 4.87*10^24 kg, 3.4 degrees, 1.08*10^11 m
### Earth: 5.97*10^24 kg, 0 degrees, 1.49*10^11 m
### Mars: 6.42*10^23 kg, 1.85 degrees, 2.28*10^11 m
### Jupiter: 1.90*10^27 kg, 1.31 degrees, 7.78*10^11 m
### Saturn: 5.68*10^26 kg, 2.48 degrees, 1.43*10^12 m
### Uranus: 8.68*10^25 kg, 0.77 degrees, 2.87*10^12 m
### Neptune: 1.02*10^26 kg, 1.77 degrees, 4.51*10^12 m

## After inputing all of the variables, it will take some time for Python to make the plot, but when the plot is made, it will be shown on the screen.
## The plot should have a dot in the center representing the Sun, with circular rings surrounding the Sun corresponding to each planet.