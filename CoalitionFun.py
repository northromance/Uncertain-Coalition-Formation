# CoalitionFunction.py
import numpy as np


def CoalitionIteration(agents, tasks, Value_data, Value_Params, Graph):
    """
    执行多机器人联盟形成的主循环迭代（单轮联盟形成迭代）

    参数:
        agents: list of Agent 对象
        tasks: list of Task 对象
        Value_data: list of ValueData 对象
        Value_Params: 参数对象，包含 N, M
        Graph: 邻接矩阵 N x N

    返回:
        Value_data: 更新后的 ValueData 列表
    """

    N = Value_Params.N

    doneflag = 0      # 收敛标志位
    T = 0             # 当前时间步
    lastTime = 0      # 上次有 agent 任务变化的时间

    while doneflag == 0:

        # =========================
        # 1. 每个 agent 自主选择任务 
        # 基于模拟退火的分布式联盟形成算法
        incremental = np.zeros(N)   # 每个 agent 任务变化增量
        curnumberrow = np.zeros(N)  # 当前任务索引（TODO: 根据 Value_order 输出修改）

        for agent_idx in range(N):
            # TODO: 调用 Value_order 实现任务选择
            inc, cur_row, updated_agent_data = Value_order(
                agents, tasks, Value_data[agent_idx], Value_Params
            )

            incremental[agent_idx] = inc
            curnumberrow[agent_idx] = cur_row
            Value_data[agent_idx] = updated_agent_data

            # 打印每个 agent 的增量
            print(f"Agent {agent_idx + 1} incremental: {incremental[agent_idx]}")

        # =========================
        # 2. 检查是否所有 agent 增量为 0
        if np.sum(incremental == 0) == N:
            # 所有 agent 增量为 0，lastTime 不变
            lastTime = lastTime
        else:
            lastTime = T

        # =========================
        # 3. 邻居 agent 通信
        # TODO: Value_communication 完成邻居间联盟结构同步
        # 
        Value_data = Value_communication(agents, tasks, Value_data, Value_Params, Graph)

        # =========================
        # 4. 与邻居通信进行信息融合

        # =========================
        # 4. 收敛检查
        if (T - lastTime) > 2:
            doneflag = 1  # 收敛，退出循环
        else:
            T += 1        # 下一轮迭代

    return Value_data

# ==============================
# Value_order 函数
# 计算联盟结构和任务选择
def Value_order(agents, tasks, agent_data, Value_Params, Graph):
    """
    每个 agent 自主选择任务，计算增量和当前任务索引

    参数:
        agents: list
            Agent 对象列表
        tasks: list
            Task 对象列表
        agent_data: ValueData
            单个 agent 的 ValueData 对象
        Value_Params: object
            参数对象，包含 N (agent 数量), M (任务数量)
        Graph: np.ndarray
            邻接矩阵 N x N

    返回:
        incremental: int
            当前 agent 任务选择增量 (0: 未改变, 1: 改变)
        cur_row: int
            当前 agent 所选择任务的索引
        updated_agent_data: ValueData
            更新后的 agent_data 对象
    """

    # --------------------------
    # TODO: 保存初始联盟结构和相关信息
    # AValue_data = copy.deepcopy(agent_data) 或手动保存必要字段

    # --------------------------
    # TODO: 获取 agent 当前任务索引和所在联盟成员

    # --------------------------
    # TODO: 计算 agent 当前效用
    # curagentutility = Value_utility(...)

    # --------------------------
    # TODO: 遍历所有任务，计算候选任务效用
    # candidateagentutility[j] = Value_utility(...)

    # --------------------------
    # TODO: 找到最大效用及对应任务索引
    # value, taskindex = max(candidateagentutility)

    # --------------------------
    # TODO: 根据增量判断是否更新联盟结构
    incremental = 0  # 占位
    cur_row = 0      # 占位

    # --------------------------
    # TODO: 更新 agent_data 联盟结构和其他信息
    updated_agent_data = agent_data  # 占位

    return incremental, cur_row, updated_agent_data

# ==============================
# Value_communication 函数
# 通信函数
def Value_communication(agents, tasks, Value_data, Value_Params, Graph):
    """
    邻居 agent 间通信，更新每个 agent 的联盟结构和相关信息。
    对应 MATLAB 中的 Value_communication 函数。

    参数:
        agents: list
            Agent 对象列表
        tasks: list
            Task 对象列表
        Value_data: list
            所有 agent 的 ValueData 对象列表
        Value_Params: object
            参数对象，包含 N (agent 数量), M (任务数量)
        Graph: np.ndarray
            邻接矩阵 N x N (1 表示邻居，0 表示非邻居)

    返回:
        Value_data: list
            更新后的所有 agent ValueData 对象列表
    """

    N = Value_Params.N  # agent 数量

    # 遍历所有 agent
    for k in range(N):
        for n in range(N):
            # 如果 k 和 n 是邻居
            if Graph[k, n] == 1:
                # TODO: 根据迭代次数和随机变量判断是否更新 n 的信息
                if (Value_data[k].iteration > Value_data[n].iteration) or \
                   ((Value_data[k].iteration == Value_data[n].iteration) and 
                    (Value_data[k].unif > Value_data[n].unif)):
                    # 更新 n 的联盟结构和状态
                    Value_data[n].coalitionstru = Value_data[k].coalitionstru.copy()
                    Value_data[n].iteration = Value_data[k].iteration
                    Value_data[n].unif = Value_data[k].unif

    return Value_data

