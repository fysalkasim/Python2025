import matplotlib
print(matplotlib.__version__)
import numpy as np
import matplotlib.pyplot as plt
# xpoint = np.array([0,334])
# ypoint = np.array([655,255])

# plt.plot(xpoint,ypoint)
# plt.show()

# xpoint = np.array([0,334])
# ypoint = np.array([655,255])

# plt.plot(xpoint,ypoint,"x")
# plt.show()

# xpoints = np.array([1, 2, 6, 8])
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(xpoints, ypoints)
# plt.show()

# ypoints = np.array([3, 8, 1, 10, 5, 7])
# plt.plot(ypoints)
# plt.show()

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, 'o--r', ms = 0.1)
plt.show()
