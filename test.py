import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
 
# 创建三维图像对象
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
 
# 准备数据
x = [36.0735,37.145688,36.346147,35.483822,34.787892]
y = [99.0898,100.183896,98.776932,98.503538,101.024541]
z = [1.13468e+06,0.0,0.0,0.0,0.0]
 
# 绘制散点图
ax.scatter(x, y, z)
 
# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
 
# 显示图像
plt.show()