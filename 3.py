#计算两个数组a和数组b之间的欧氏距离
#给定：a = np.array([1,2,3,4,5]),b = np.array([4,5,6,7,8])
import numpy as np
a=np.array([1,2,3,4,5])
b=np.array([4,5,6,7,8])
distance=np.sqrt(np.sum((b-a)**2))
print(distance)