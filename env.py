# 设置环境中的任务和智能体类
# 以及循环中用到的数据结构
import numpy as np
import random

class Task:
    def __init__(self, task_id, x, y, value):
        self.id = task_id
        self.x = x
        self.y = y
        self.value = value
        self.prob_matrix = None  # 可选：存储概率矩阵等信息

class Agent:
    def __init__(self, agent_id, x, y, vel, fuel):
        self.id = agent_id
        self.x = x
        self.y = y
        self.vel = vel
        self.fuel = fuel
        self.coalition = []   # 当前加入的联盟任务索引
        self.task_values = {} # 存储每个任务的价值预期


class ValueParams:
    def __init__(self, N, M, K, init_belief_value):
        self.N = N
        self.M = M
        self.K = K
        self.init_belief_value = init_belief_value


class World:
    def __init__(self,XMIN,XMAX,YMIN,YMAX,ZMIN,ZMAX,N,M):
        # 坐标范围
        self.XMIN = XMIN
        self.XMAX = XMAX
        self.YMIN = YMIN
        self.YMAX = YMAX
        self.ZMIN = ZMIN
        self.ZMAX = ZMAX
        self.N = N
        self.M = M

class ValueData:
    """
    ValueData 类用于存储每个 agent 的状态信息，
    对应 MATLAB 中的 Value_data(i) 结构体。

    参数说明
    --------
    agent : Agent
        当前 agent 对象，用于读取其 ID。
    N : int
        机器人总数。
    M : int
        任务数量。
    K : int
        每个任务的类型数量。
    init_belief_value : float
        每个类型的初始概率（例如 1/K）。
        系统会自动生成长度为 K 的概率向量。
    """

    def __init__(self, agent, N, M, K, init_belief_value):
        self.agentID = agent.id
        self.iteration = 0
        self.unif = 0
        self.coalitionstru = np.zeros((M + 1, N), dtype=int)
        init_row = np.ones(K) * init_belief_value
        self.initbelief = np.zeros((M, K))
        for j in range(M):
            self.initbelief[j, :] = init_row
        self.observe = np.zeros((M, K))
        self.preobserve = np.zeros((M, K))
