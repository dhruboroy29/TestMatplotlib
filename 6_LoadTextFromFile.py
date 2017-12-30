import matplotlib.pyplot as plt, csv, numpy as np

fig = plt.figure()

x = []
y = []

# Use csv import
with open('example.txt', 'r') as csvfile:
    # Read csv file
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x, y, label='Loaded from file using csv')

# Use numpy loadtxt
x, y = np.loadtxt('example2.txt', delimiter=',',
                  unpack=True)  # unpack=False gives ValueError: too many values to unpack (expected 2)

plt.plot(x, y, label='Loaded from file using numpy', color='r')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

fig.savefig('loadtextfromfile.eps', format='eps', dpi=1200)