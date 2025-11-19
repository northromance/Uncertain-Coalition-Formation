# 设置环境中的任务和智能体类
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
    def __init__(self, N, M):
        self.N = N
        self.M = M


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

