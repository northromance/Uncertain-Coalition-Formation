import numpy as np
import env
from CoalitionFun import * # 导入 CoalitionFun 模块中的函数
from Belief_fusion import *
from env import ValueData, ValueParams



# =========================
# CoalitionMain 联盟形成主函数
# =========================
def CoalitionMain(agents, tasks, Graph, world, ValueParams):
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
    K = ValueParams.K
    init_belief_value = ValueParams.init_belief_value


    # 初始化 Value_data
    Value_data = [ValueData(agent, N, M, K, init_belief_value) for agent in agents]
    
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

        # 一次联盟迭代 

        Value_data = CoalitionIteration(agents, tasks, Value_data, Value_Params, Graph)

        # TODO: 

        # TODO: 个体观测矩阵更新 


        # TODO: 根据观测矩阵进行信念融合
        robot_beliefs = belief_fusion_update(robot_beliefs, observation_matrix, neighbors, weight_matrix)

        # TODO: 计算 Rcost、cost_sum、net_profit

    # 最终返回结果
    return Value_data, None, None, None, initial_coalition
