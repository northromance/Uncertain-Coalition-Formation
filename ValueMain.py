import numpy as np
import env
from CoalitionFun import * # 导入 CoalitionFun 模块中的函数


class ValueData:
    """
    ValueData 类用于存储每个 agent 的状态信息，
    包括联盟结构、任务信念以及观测矩阵，
    对应 MATLAB 中的 Value_data(i) 结构体。
    """
    def __init__(self, agent, N, M):
        self.agentID = agent.id            # agent 编号
        self.agentIndex = agent.id         # agent 索引
        self.iteration = 0                 # 联盟改变次数
        self.unif = 0                      # 均匀随机变量

        self.coalitionstru = np.zeros((M+1, N), dtype=int)  # 联盟矩阵 (M+1 行, N 列)
        self.initbelief = np.zeros((M+1, 3))               # 初始信念矩阵 (M+1 x 3)
        for j in range(M):
            self.initbelief[j, :] = [1/3, 1/3, 1/3]       # 每个任务三种类型概率均等

        self.observe = np.zeros((M, 3))      # 当前观测矩阵
        self.preobserve = np.zeros((M, 3))   # 上一轮观测矩阵


# =========================
# CoalitionMain 联盟形成主函数
# =========================
def CoalitionMain(agents, tasks, Graph, world):
    """
    初始化 Value_data、资源成本、总成本、净收益和初始联盟

    输入:
        agents: Agent 列表
        tasks: Task 列表
        Graph: 邻接矩阵（N x N）

    输出:
        Value_data: 每个 agent 的信息列表
        Rcost: 每个 agent 对每个任务的资源成本 (N x M)
        cost_sum: 每个 agent 总成本 (N,)
        net_profit: 每个 agent 总收益 (N,)
        initial_coalition: 初始联盟矩阵 (M+1 x N)
    """
    N = world.N
    M = world.M
    
    # 初始化 Value_data
    Value_data = [ValueData(agent, N, M) for agent in agents]
    
    # 所有 agent 放入 "void 任务" 中（最后一行）
    for k in range(N):
        for i in range(N):
            Value_data[k].coalitionstru[M, i] = agents[i].id
    
    # 初始化每个 agent 对每个任务的观测矩阵
    for agent_data in Value_data:
        agent_data.observe[:, :] = 0
        agent_data.preobserve[:, :] = 0

    # 进行50次循环 
    for counter in range(50):

        # TODO: 保存每轮初始 belief
        for i in range(N):
            for j in range(M):
                # 假设 tasks[j] 有 prob 属性
                if not hasattr(Value_data[i].tasks[j], 'prob'):
                    Value_data[i].tasks[j].prob = np.zeros((50, 3))
                Value_data[i].tasks[j].prob[counter, :] = Value_data[i].initbelief[j, :]

        # 一次联盟迭代 

        
        Value_data = CoalitionIteration(agents, tasks, Value_data, Value_Params, Graph)

        # TODO: 


        # TODO: 个体观测矩阵更新 


        # TODO:  根据观测矩阵进行信念融合 得到新的信念
        # 4. 与邻居通信进行信息融合
        # 包括与邻居进行证据合并 
        # 各个节点按照权重矩阵进行线性共识更新
        # 然后一致的信念恢复
        # 得到全局一致的稳定的信念



        # TODO: 计算 Rcost、cost_sum、net_profit

    # 最终返回结果
    return Value_data, None, None, None, initial_coalition
