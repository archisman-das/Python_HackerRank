# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

# Read the complex number input as a string
z = complex(input())

# Calculate the modulus (magnitude)
r = abs(z)

# Calculate the phase (angle in radians)
theta = cmath.phase(z)

# Print the modulus and phase
print(r)
print(theta)