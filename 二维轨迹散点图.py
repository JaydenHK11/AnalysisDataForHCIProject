import pandas as pd
import matplotlib.pyplot as plt

# 定义任务组和对应的CSV文件列表
task_groups = {
    "H-TASK1": ["h-task1-1.csv", "h-task1-2.csv", "h-task1-3.csv", "h-task1-4.csv", "h-task1-5.csv", "h-task1-6.csv", "h-task1-7.csv", "h-task1-8.csv", "h-task1-9.csv", "h-task1-10.csv"],
    "H-TASK2": ["h-task2-1.csv", "h-task2-2.csv", "h-task2-3.csv", "h-task2-4.csv", "h-task2-5.csv", "h-task2-6.csv", "h-task2-7.csv", "h-task2-8.csv", "h-task2-9.csv", "h-task2-10.csv"],
    "V-TASK1": ["v-task1-1.csv", "v-task1-2.csv", "v-task1-3.csv", "v-task1-4.csv", "v-task1-5.csv", "v-task1-6.csv", "v-task1-7.csv", "v-task1-8.csv", "v-task1-9.csv", "v-task1-10.csv"],
    "V-TASK2": ["v-task2-1.csv", "v-task2-2.csv", "v-task2-3.csv", "v-task2-4.csv", "h-task2-5.csv", "h-task2-6.csv", "h-task2-7.csv", "h-task2-8.csv", "h-task2-9.csv", "h-task2-10.csv"],
}

# 创建一个图形，包含四个子图（正方形）
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
fig.suptitle('Scatter Plots of X and Y for Task Groups', fontsize=16)

# 初始化X、Y轴的范围
x_min, x_max = -1, 1
y_min, y_max = 1, 3

# 循环读取每个任务组的CSV文件，并绘制X和Y的数据在相应的子图中
for i, (task_group, csv_files) in enumerate(task_groups.items()):
    row, col = i // 2, i % 2  # 确定子图的行和列
    ax = axes[row, col]

    for csv_file in csv_files:
        # 从CSV文件中读取数据
        df = pd.read_csv(csv_file)

        # 提取X和Y列的数据
        x = df['PositionX']
        y = df['PositionY']

        # 绘制X和Y的散点图，调整点的大小和透明度
        ax.scatter(x, y, s=10, alpha=0.5)

    # 设置子图的坐标轴标签
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    # 设置子图的X和Y轴范围
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

    # 去掉子图的图例
    ax.legend().set_visible(False)

    # 设置子图的标题
    ax.set_title(task_group)

# 调整子图之间的间距
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# 保存图形为PNG文件
plt.savefig('XYScatterPlots_NoLegend.png', dpi=300)

# 显示图形
plt.show()
