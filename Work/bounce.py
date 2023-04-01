# A rubber ball is dropped from a height of 100m and each time it hits the ground, it bounces
# back to 3/5 the height it fell.
# Print a table showing the height of the first 10 bounces.

height = 100

for i in range(10):
    height = height * 3 / 5
    print(i+1, round(height, ndigits=4))
