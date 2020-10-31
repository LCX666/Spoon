from time import time
import numpy as np

from classes.result import Result
from utils.settings import INF

def edge(para):
    """
	function: use edge free in CPU to solve the SSSP. 
        (more info please see the developer documentation) .
	
	parameters:  
		edgeSet: edgeSet graph data. (more info please see the developer documentation) .
        n: the number of the vertexs in the graph.
        m: the number of the edges in the graph.
        s: the source list, can be number.(more info please see the developer documentation).
        pathRecordingBool: record the path or not.
	
	return: Result(class).(more info please see the developer documentation) .   
    """

    t1 = time()

    edgeSet, n, m, s, pathRecordingBool = para.edgeSet, para.n, para.m, para.srclist, para.pathRecordingBool
    src, des, val = para.edgeSet[0], para.edgeSet[1], para.edgeSet[2]

    # 退出标识
    flag = 1

    # dist
    dist = np.full((n, ), INF).astype(np.int32)
    dist[s] = 0 
    # print(dist.shape)  
    while True:
        # 如果没有点的距离发生改变，则退出遍历
        if flag == 0:
            break

        flag = 0

        # edge = (u, v, w): u -> v = w
        for i in range(len(src)):
            u, v, w = src[i], des[i], val[i]
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                flag = 1


    timeCost = time() - t1

    # 结果
    result = Result(dist = dist, timeCost = timeCost)
    
    if pathRecordingBool:
        result.calcPath(edgeSet = edgeSet)

    return result

