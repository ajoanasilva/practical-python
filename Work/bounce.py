# bounce.py
#
# Exercise 1.5

initial_height = 100
bounce_back_ratio = 0.6
bounce = 1
bounce_cutoff = 10
previous_height = initial_height

while(bounce <= bounce_cutoff):
    height = round(previous_height * bounce_back_ratio, 4)
    print(bounce, height)
    bounce = bounce + 1
    previous_height = height