# INPUT
# Read grid dimensions, iteration limit, and complex-plane boundaries
# from config.txt

config = {}

file = open("config.txt", "r")
for line in file:
    parameter, value = line.strip().split("=")
    config[parameter] = float(value) if "." in value else int(value)
file.close()

width, height, max_iter = config["ancho"], config["alto"], config["max_iter"]

# PROCESS
# For every point in the grid:
#   1. map the pixel position to a point c on the complex plane
#   2. apply the escape-time rule (z = z*z + c) until it escapes
#      or the iteration limit is reached
#   3. write the resulting iteration count to the output file

output = open("mandelbrot.csv", "w")
output.write("row,column,iterations\n")

for row in range(height):
    for column in range(width):
        real = config["real_min"] + (column / width) * (config["real_max"] - config["real_min"])
        imag = config["imag_min"] + (row / height) * (config["imag_max"] - config["imag_min"])
        c = complex(real, imag)

        z = 0 + 0j
        iterations = 0

        while (abs(z) <= 2) and (iterations < max_iter):
            z = z * z + c
            iterations += 1

        # OUTPUT
        # Save one row per grid point: row, column, iterations
        output.write(f"{row},{column},{iterations}\n")

output.close()