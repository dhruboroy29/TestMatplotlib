import matplotlib.pyplot as plt

fig = plt.figure()

plt.bar([1, 3, 5, 7, 9], [5, 2, 7, 8, 2], label="Population 1")
plt.bar([2, 4, 6, 8, 10], [8, 6, 2, 5, 6], label="Population 2", color='g')

plt.legend()
plt.xlabel('Bar Number')
plt.ylabel('Bar Height')
plt.title('Epic Bar\nGraph')

plt.show()

fig.savefig('barchart.eps', format='eps', dpi=1200)