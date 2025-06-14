import matplotlib.pyplot as plt
from matplotlib import colormaps

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.RdYlBu, s=10)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')



#print(list(colormaps))
plt.show()