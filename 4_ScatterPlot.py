import matplotlib.pyplot as plt

fig = plt.figure()

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 4, 2, 1, 4, 5, 2]
y2 = [12, 5, 67, 8, 2, 4, -12, -18]

plt.scatter(x, y, label='Points1', color='k', marker="o")
plt.scatter(x, y2, label='Points2', color='b', marker="*")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.legend()
plt.show()

fig.savefig('scatter_plot.eps', format='eps', dpi=1200)