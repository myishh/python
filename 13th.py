import math

def move(x, y, step, angle = 0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx, ny

x = float(input('input x:\n'))
y = float(input('input y:\n'))
step = float(input('input step:\n'))
angle = float(input('input angle:\n'))

r = move(x, y, step, angle)
print(r)
