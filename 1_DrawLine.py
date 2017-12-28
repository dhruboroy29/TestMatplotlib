import matplotlib.pyplot as plt

# Create new figure
fig = plt.figure()

x = [1, 2, 3]

y = [5, 7, 4]
y2 = [10, 14, 12]

plt.plot(x, y, label='First Line')
plt.plot(x, y2, label = 'Second Line')

plt.xlabel('x')
plt.ylabel('y')

plt.title('Simple Line\nTest')
plt.legend()

plt.show()

# Save as .eps
fig.savefig('lines.eps', format='eps', dpi=1200)