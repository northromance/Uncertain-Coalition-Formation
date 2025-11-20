import numpy as np
import random
import matplotlib.pyplot as plt
import networkx as nx
from env import Agent, Task, ValueParams # 导入环境中的Agent、Task和ValueParams类
import utility
import ValueMain
import env


# ==========================
# 设置随机种子和环境参数
# ==========================
SEED = 24375
np.random.seed(SEED)  # 设置NumPy随机种子，保证可重复性
random.seed(SEED)     # 设置Python内置随机库种子

# 机器人和任务数量
N = 5  # 机器人数量
M = 5   # 任务数量
K = 3 # 任务类型个数
init_belief_value = 1/3 # 初始信念值

# 任务初始化
# 初始化位置和价值
# 初始化6个任务，位置随机，价值从预定义列表中选择
tasks = [Task(j+1, np.random.randint(0,101), np.random.randint(0,101), random.choice([300,500,1000]))
         for j in range(M)] # 初始化6个任务，位置随机，价值从预定义列表中选择

# 机器人初始化
# 初始化10个机器人，位置随机，速度和燃料固定
vel = 2 # 速度
fuel = 1 # 燃料消耗
agents = [Agent(i+1, np.random.randint(0,101), np.random.randint(0,101), vel, fuel) for i in range(N)]

# 初始化世界对象
world = env.World(XMIN=0, XMAX=100, YMIN=0, YMAX=100, ZMIN=0, ZMAX=0, N=N, M=M)

# 构造参数对象
Value_Params = ValueParams(N, M, K, init_belief_value)

p, result = utility.Value_graph(agents, Value_Params)

# 提取起点 S 和终点 E（与 MATLAB 功能一致）
S = [edge[0] for edge in result]   # result 第一列
E = [edge[1] for edge in result]   # result 第二列

# 初始化 N x N 的图矩阵 G，全 0
G = np.zeros((N, N), dtype=int)

# 填充边
for j in range(len(result)):
    start = result[j][0]  
    end   = result[j][1]  
    G[start - 1, end - 1] = 1

Graph = G + G.T

print("邻接矩阵 G:" )
print(Graph)

# 形成联盟

[Value_data,Rcost,cost_sum,net_profit, initial_coalition]= ValueMain.CoalitionMain(agents,tasks,Graph,world,Value_Params)

# 可视化
