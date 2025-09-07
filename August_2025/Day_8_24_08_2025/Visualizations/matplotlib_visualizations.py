# import matplotlib.pyplot as plt
#
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
#
# plt.scatter(x,y,color ="red",label = "Sample Visualization")
# plt.xlabel("Input Data")
# plt.ylabel("Output Data")
# plt.legend()
# plt.show()
"""Below program is to do plo with different colors """
# import matplotlib.pyplot as plt
#
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
#
# plt.scatter(x,y,c=x,label = "Sample Visualization",cmap="magma") # viridis, rainbow, magma
# plt.xlabel("Input Data")
# plt.ylabel("Output Data")
# plt.colorbar()
# plt.legend()
# plt.show()

"""different visualization with different marker"""
# import matplotlib.pyplot as plt
#
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
#
# plt.plot(x,y,color="red",label = "Sample Visualization",marker = "o")
# plt.xlabel("Input Data")
# plt.ylabel("Output Data")
# plt.legend()
# plt.show()

"""different visualization with number and category"""
# import matplotlib.pyplot as plt
#
# x = ["csk","rcb","kkr","mi"]
# y = [5,1,3,5]
#
# plt.bar(x, y, label="sample visualization")
# plt.xlabel("input data")
# plt.ylabel("output data")
# plt.legend()
# plt.show()

"""different visualization with some usage(outlier detection)"""

import matplotlib.pyplot as plt

x = [1,2,3,4,5,5000,-1000]
plt.boxplot(x)
plt.xlabel("Input data")
plt.ylabel("Output data")
plt.legend()
plt.show()