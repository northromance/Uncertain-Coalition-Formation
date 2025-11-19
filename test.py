import numpy as np
import random

# 定义 Task 类
class Task:
    def __init__(self, task_id, x, y, value):
        self.id = task_id
        self.x = x
        self.y = y
        self.value = value
        self.prob_matrix = None  # 可选：存储概率矩阵等信息

# ==========================
# 初始化任务列表
# ==========================
tasks = [Task(j+1, np.random.randint(0,101), np.random.randint(0,101), random.choice([300,500,1000]))
         for j in range(6)]

# ==========================
# 访问和打印任务信息
# ==========================
print("=== 初始任务信息 ===")
for task in tasks:
    print(f"Task {task.id}: x={task.x}, y={task.y}, value={task.value}")

# ==========================
# 修改任务属性示例
# 给每个任务的 value 增加 50
# ==========================
for task in tasks:
    task.value += 50

# ==========================
# 打印修改后的任务信息
# ==========================
print("\n=== 修改后任务信息 ===")
for task in tasks:
    print(f"Task {task.id}: x={task.x}, y={task.y}, value={task.value}")

# ==========================
# 单个任务访问示例
# 访问第3个任务
# ==========================
task3 = tasks[2]  # Python索引从0开始
print(f"\n第3个任务的信息: id={task3.id}, x={task3.x}, y={task3.y}, value={task3.value}")
