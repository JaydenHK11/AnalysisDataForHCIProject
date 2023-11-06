import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义任务组和对应的CSV文件列表
task_groups = {
    "H-TASK1": ["h-task1-1.csv", "h-task1-2.csv", "h-task1-3.csv", "h-task1-4.csv", "h-task1-5.csv", "h-task1-6.csv", "h-task1-7.csv", "h-task1-8.csv", "h-task1-9.csv", "h-task1-10.csv"],
    "H-TASK2": ["h-task2-1.csv", "h-task2-2.csv", "h-task2-3.csv", "h-task2-4.csv", "h-task2-5.csv", "h-task2-6.csv", "h-task2-7.csv", "h-task2-8.csv", "h-task2-9.csv", "h-task2-10.csv"],
    "V-TASK1": ["v-task1-1.csv", "v-task1-2.csv", "v-task1-3.csv", "v-task1-4.csv", "v-task1-5.csv", "v-task1-6.csv", "v-task1-7.csv", "v-task1-8.csv", "v-task1-9.csv", "v-task1-10.csv"],
    "V-TASK2": ["v-task2-1.csv", "v-task2-2.csv", "v-task2-3.csv", "v-task2-4.csv", "v-task2-5.csv", "v-task2-6.csv", "v-task2-7.csv", "v-task2-8.csv", "v-task2-9.csv", "v-task2-10.csv"],
}

# 创建一个3D图形
fig = plt.figure(figsize=(15, 8))

# 循环读取每个任务组的CSV文件，并绘制3D散点图
for task_group, csv_files in task_groups.items():
    ax = fig.add_subplot(2, 2, list(task_groups.keys()).index(task_group) + 1, projection='3d')

    # 循环读取和绘制每个CSV文件的数据
    for csv_file in csv_files:
        # 从CSV文件中读取数据
        df = pd.read_csv(csv_file)

        # 提取X、Y和Z列的数据
        x = df['PositionX']
        y = df['PositionY']
        z = df['PositionZ']

        # 绘制三维散点图
        ax.scatter(x, y, z, label=csv_file)

    # 设置坐标轴标签
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # # 添加图例
    # ax.legend(loc='upper right')

    # 设置图形标题
    ax.set_title(f'3D Scatter Plot for {task_group}')

# 调整子图之间的间距
plt.tight_layout()

# 保存图形为PDF文件
plt.savefig('3DLine.pdf')

# 显示图形
plt.show()
