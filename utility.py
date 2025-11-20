import math

def Value_graph(agents, Value_Params):
    """
    使用 Prim 算法计算一个图的最小生成树 (MST)

    参数：
        agents: 一个列表，每个元素是一个 dict 或对象，必须有 .x 和 .y 属性
        Value_Params: 一个含有 Value_Params.N 的对象或字典

    返回：
        p:     一个列表，记录节点加入 MST 的顺序
        result: 一个 3 x M 的列表，每列是 [起点, 终点, 权重]
    """
    
    N = Value_Params.N 
    
    # 1. 初始化距离矩阵
    a = [[0.0]*N for _ in range(N)]
    
    # 2. 计算欧氏距离，只填上三角
    for i in range(N):
        for j in range(i+1, N):
            dx = agents[i].x - agents[j].x
            dy = agents[i].y - agents[j].y
            dist = math.sqrt(dx*dx + dy*dy)
            a[i][j] = dist
            a[j][i] = dist

    # 对角线设为无穷大
    for i in range(N):
        a[i][i] = float('inf')

    # 3. 初始化 Prim 所需集合
    result = []          # 每条边为 [j, k, d]
    p = [0]              # 已加入 MST 的节点（python 下标从0开始）
    tb = list(range(1, N))  # 待加入节点

    # 4. Prim 主循环
    while len(result) != N - 1:
        
        # 生成所有 (已加入节点 → 待加入节点) 的边
        candidate_edges = []
        
        for j in p:
            for k in tb:
                candidate_edges.append((a[j][k], j, k))
        
        # 找到权重最小的边
        d, j, k = min(candidate_edges, key=lambda x: x[0])
        
        # 添加到结果
        result.append([j+1, k+1, d])  # +1 还原 MATLAB 的下标

        # 更新集合
        p.append(k)
        tb.remove(k)

    return p, result
