import matplotlib.pyplot as plt

fig = plt.figure()

population_ages = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102, 110, 120, 121, 122, 130, 111, 115, 112, 80, 75, 65,
                   54, 44, 43, 42, 48]

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8) # Absence of rwidth makes histogram look continuous

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Histogram\nCheck it out')
plt.legend()
plt.show()

fig.savefig('histogram.eps', format='eps', dpi=1200)