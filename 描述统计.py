import pandas as pd
import matplotlib.pyplot as plt
import statistics  # Import the statistics module

# 定义四组数据的文件路径
data_paths = {
    "H-TASK1": ["h-task1-1.csv", "h-task1-2.csv", "h-task1-3.csv", "h-task1-4.csv", "h-task1-5.csv", "h-task1-6.csv", "h-task1-7.csv", "h-task1-8.csv", "h-task1-9.csv", "h-task1-10.csv"],
    "H-TASK2": ["h-task2-1.csv", "h-task2-2.csv", "h-task2-3.csv", "h-task2-4.csv", "h-task2-5.csv", "h-task2-6.csv", "h-task2-7.csv", "h-task2-8.csv", "h-task2-9.csv", "h-task2-10.csv"],
    "V-TASK1": ["v-task1-1.csv", "v-task1-2.csv", "v-task1-3.csv", "v-task1-4.csv", "v-task1-5.csv", "v-task1-6.csv", "v-task1-7.csv", "v-task1-8.csv", "v-task1-9.csv", "v-task1-10.csv"],
    "V-TASK2": ["v-task2-1.csv", "v-task2-2.csv", "v-task2-3.csv", "v-task2-4.csv", "v-task2-5.csv", "v-task2-6.csv", "v-task2-7.csv", "v-task2-8.csv", "v-task2-9.csv", "v-task2-10.csv"],
}

# 创建一个空的DataFrame来存储所有数据
all_data = pd.DataFrame()

# 循环加载数据并计算速度
task_speeds = {}
for condition, files in data_paths.items():
    condition_speeds = []

    for file in files:
        # 加载CSV文件
        df = pd.read_csv(file)

        # 计算总速度
        df['Speed'] = ((df['PositionX']**2 + df['PositionY']**2 + df['PositionZ']**2)**0.5)

        # 计算平均速度
        avg_speed = df['Speed'].mean()

        # 将平均速度存储到对应组的列表中
        condition_speeds.append(avg_speed)

    # 将每个CSV文件的平均速度存储到四个组的数据结构中
    task_speeds[condition] = condition_speeds

# 创建DataFrame用于箱线图
stats_df = pd.DataFrame(task_speeds)

# 检查每个组中的CSV文件数量
valid_groups = []
for group, speeds in stats_df.items():
    if len(speeds) >= 1:  # 至少有一个CSV文件
        valid_groups.append(group)

# 绘制箱线图可视化四个组中每个CSV文件的平均速度
if valid_groups:
    plt.figure(figsize=(10, 6))
    plt.boxplot([stats_df[group] for group in valid_groups], labels=valid_groups)
    plt.title('Average Speed Comparison')
    plt.ylabel('Average Speed (units/s)')

    # 添加散点图和误差线
    for i, speeds in enumerate([stats_df[group] for group in valid_groups]):
        x = [i + 1] * len(speeds)  # 横坐标位置
        plt.scatter(x, speeds, c='b', marker='o', alpha=0.5, label=valid_groups[i])
        plt.errorbar(x, speeds, yerr=[speeds.std() / 2] * len(speeds), fmt='none', ecolor='r', elinewidth=1, capsize=5)

    plt.legend(loc='upper right')
    plt.xticks(range(1, len(valid_groups) + 1), valid_groups, rotation=45)
    plt.tight_layout()

    # 保存图形为PDF文件
    plt.savefig('AverageSpeed.pdf')

    # 统计和输出每个组的数据和描述性统计信息
    for group, speeds in stats_df.items():
        if len(speeds) >= 1:
            print(f"Group: {group}")
            print("Data:", speeds)
            print(f"Max: {max(speeds)}")
            print(f"Min: {min(speeds)}")
            print(f"Median: {statistics.median(speeds)}")
            print(f"Mean: {statistics.mean(speeds)}")
            print("\n")


    # 显示图表
    plt.show()
else:
    print("No valid data available for plotting.")
