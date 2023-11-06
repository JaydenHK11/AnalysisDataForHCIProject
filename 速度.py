import pandas as pd

# 定义四组数据的文件路径
data_paths = {
    "H-TASK1": ["h-task1-1.csv", "h-task1-2.csv", "h-task1-3.csv", "h-task1-4.csv", "h-task1-5.csv", "h-task1-6.csv", "h-task1-7.csv", "h-task1-8.csv", "h-task1-9.csv", "h-task1-10.csv"],
    "H-TASK2": ["h-task2-1.csv", "h-task2-2.csv", "h-task2-3.csv", "h-task2-4.csv", "h-task2-5.csv", "h-task2-6.csv", "h-task2-7.csv", "h-task2-8.csv", "h-task2-9.csv", "h-task2-10.csv"],
    "V-TASK1": ["v-task1-1.csv", "v-task1-2.csv", "v-task1-3.csv", "v-task1-4.csv", "v-task1-5.csv", "v-task1-6.csv", "v-task1-7.csv", "v-task1-8.csv", "v-task1-9.csv", "v-task1-10.csv"],
    "V-TASK2": ["v-task2-1.csv", "v-task2-2.csv", "v-task2-3.csv", "v-task2-4.csv", "v-task2-5.csv", "v-task2-6.csv", "v-task2-7.csv", "v-task2-8.csv", "v-task2-9.csv", "v-task2-10.csv"],
}

# 创建一个空的DataFrame来存储所有数据
all_data = pd.DataFrame()

# 循环加载数据并计算速度和记录时间
task_stats = {}
for condition, files in data_paths.items():
    condition_data = pd.DataFrame()
    task_speeds = []
    task_record_times = []

    for file in files:
        # 加载CSV文件
        df = pd.read_csv(file)

        # 计算总速度
        df['Speed'] = ((df['PositionX']**2 + df['PositionY']**2 + df['PositionZ']**2)**0.5)

        # 计算记录时间
        record_time = df['Time'].max() - df['Time'].min()

        # 保存速度和记录时间
        task_speeds.append(df['Speed'].mean())
        task_record_times.append(record_time)

        condition_data = pd.concat([condition_data, df], ignore_index=True)

    # 计算平均速度和平均记录时间
    avg_speed = sum(task_speeds) / len(task_speeds)
    avg_record_time = sum(task_record_times) / len(task_record_times)

    task_stats[condition] = {
        'Average Speed': avg_speed,
        'Average Record Time': avg_record_time,
    }

# 打印四个组的平均速度和平均记录时间
for condition, stats in task_stats.items():
    print(f"Group: {condition}")
    print(f"Average Speed: {stats['Average Speed']:.2f} units/s")
    print(f"Average Record Time: {stats['Average Record Time']:.2f} seconds")
    print()
