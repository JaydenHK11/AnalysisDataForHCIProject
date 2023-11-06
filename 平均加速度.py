import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 定义任务组和对应的CSV文件列表
task_groups = {
    "H-TASK1": ["h-task1-1.csv", "h-task1-2.csv", "h-task1-3.csv", "h-task1-4.csv", "h-task1-5.csv", "h-task1-6.csv", "h-task1-7.csv", "h-task1-8.csv", "h-task1-9.csv", "h-task1-10.csv"],
    "H-TASK2": ["h-task2-1.csv", "h-task2-2.csv", "h-task2-3.csv", "h-task2-4.csv", "h-task2-5.csv", "h-task2-6.csv", "h-task2-7.csv", "h-task2-8.csv", "h-task2-9.csv", "h-task2-10.csv"],
    "V-TASK1": ["v-task1-1.csv", "v-task1-2.csv", "v-task1-3.csv", "v-task1-4.csv", "v-task1-5.csv", "v-task1-6.csv", "v-task1-7.csv", "v-task1-8.csv", "v-task1-9.csv", "v-task1-10.csv"],
    "V-TASK2": ["v-task2-1.csv", "v-task2-2.csv", "v-task2-3.csv", "v-task2-4.csv", "v-task2-5.csv", "v-task2-6.csv", "v-task2-7.csv", "v-task2-8.csv", "v-task2-9.csv", "v-task2-10.csv"],
}

# 存储每个组的平均加速度和误差
avg_accelerations = {'H-TASK1': [], 'H-TASK2': [], 'V-TASK1': [], 'V-TASK2': []}
acceleration_errors = {'H-TASK1': [], 'H-TASK2': [], 'V-TASK1': [], 'V-TASK2': []}

# 循环读取每个任务组的CSV文件，并计算平均加速度和误差
for task_group, csv_files in task_groups.items():
    x_accelerations = []  # 存储每个CSV文件的X方向加速度
    y_accelerations = []  # 存储每个CSV文件的Y方向加速度
    z_accelerations = []  # 存储每个CSV文件的Z方向加速度

    for csv_file in csv_files:
        # 从CSV文件中读取数据
        df = pd.read_csv(csv_file)

        # 提取X、Y和Z列的数据
        x = df['PositionX']
        y = df['PositionY']
        z = df['PositionZ']

        # 计算X、Y和Z方向上的加速度，不再除以100
        x_acceleration = np.mean(np.diff(x))
        y_acceleration = np.mean(np.diff(y))
        z_acceleration = np.mean(np.diff(z))

        # 存储加速度数据
        x_accelerations.append(x_acceleration)
        y_accelerations.append(y_acceleration)
        z_accelerations.append(z_acceleration)

    # 计算平均加速度和误差
    avg_x_acceleration = np.mean(x_accelerations)
    avg_y_acceleration = np.mean(y_accelerations)
    avg_z_acceleration = np.mean(z_accelerations)

    # 计算误差（标准差）
    error_x_acceleration = np.std(x_accelerations)
    error_y_acceleration = np.std(y_accelerations)
    error_z_acceleration = np.std(z_accelerations)

    # 存储平均加速度数据（单位为 "cm/s²"）
    avg_accelerations[task_group] = [avg_x_acceleration, avg_y_acceleration, avg_z_acceleration]

    # 存储误差数据（单位为 "cm/s²"）
    acceleration_errors[task_group] = [error_x_acceleration, error_y_acceleration, error_z_acceleration]

# 创建一个横向子图，包含三个子图，分别表示X、Y和Z方向的加速度
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 定义标签和颜色
labels = ['X', 'Y', 'Z']
colors = ['lightblue', 'lightgreen', 'lightcoral']

# 循环绘制每个子图
for i, label in enumerate(labels):
    ax = axes[i]
    ax.bar(task_groups.keys(), [avg_accelerations[task][i] for task in task_groups], yerr=[acceleration_errors[task][i] for task in task_groups], color=colors[i], alpha=0.7)
    ax.set_xlabel('Task Groups')
    ax.set_ylabel(f'Average Acceleration ({label}-direction) (cm/s²)')  # 更新Y轴标签
    ax.set_title(f'Average Acceleration in {label}-direction for Task Groups')
    ax.set_ylim(0.0000, 0.0002)  # 设置Y轴范围

# 调整子图之间的间距
plt.tight_layout()

# 保存图形为PNG文件
plt.savefig('XYZAcceleration_cm_per_s2.png', dpi=300)

# 显示图形
plt.show()
