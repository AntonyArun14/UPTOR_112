# #Line Plot:
#
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0, 10, 100)
# y = np.sin(x)
# #print(y)
# plt.plot(x, y, label = 'Sine wave', color  = 'red', linestyle = '-',linewidth = 2 )
#
# plt.xlabel('X-Axis')
# plt.ylabel('Y-Axis')
# plt.title('Line plot: Sine wave')
# plt.legend()
# plt.show()

# Scatter Plot:
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.random.rand(100)
# y = 2 * x + np.random.rand(100)
# #print(y)
# plt.scatter(x, y, color  = 'Green', marker='o', label = 'Random data')
#
# plt.xlabel('X-Axis')
# plt.ylabel('Y-Axis')
# plt.title('Scatter Plot: Random Data ')
# plt.legend()
# plt.show()

# Bar Chart:
# import matplotlib.pyplot as plt
# import numpy as np
#
# categories = ['Category A', 'Category B', 'Category C']
# values = [25, 40, 15]
#
# plt.bar(categories, values, color = 'orange', edgecolor ='black', label = 'Bar Chart')
#
# plt.xlabel('categories')
# plt.ylabel('values')
# plt.title('Bar Chart: Category comparison')
# plt.legend()
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
#
# # Generate data for a box plot
# data = [np.random.normal(0, 1, 100),np.random.normal(0, 1.5, 100), np.random.normal(0, 2, 100) ]
# plt.boxplot(data, tick_labels=['Group 1', 'Group 2', 'Group 3'], patch_artist=True, notch=True)
#
# # Add labels and title
# plt.xlabel('Groups')
# plt.ylabel('Values')
# plt.title('Box plot: Group comparison')
#
# # Show the plot
# plt.show()

