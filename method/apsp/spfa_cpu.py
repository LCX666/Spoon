from time import time
import numpy as np

from utils.debugger import Logger
from classes.result import Result
from method.sssp.spfa_cpu import spfa as spfa_sssp

logger = Logger(__name__)

def spfa(para):
    """
    function: 
        use spfa algorithm in CPU to solve the APSP. 
    
    parameters:  
        class, Parameter object.
    
    return: 
        class, Result object. (more info please see the developer documentation) .
    """

    logger.info("turning to func spfa-cpu-apsp")

    CSR = para.CSR
    n = para.n 
    pathRecording = para.pathRecordingBool
    
    start_time = time()
    Va=CSR[0]
    Ea=CSR[1]
    Wa=CSR[2]
    dist=[]
    for st in range(n):
        para.srclist = st
        resi = spfa_sssp(para)
        dist.append(resi.dist)
    para.srclist = None
    dist = np.array(dist)
    end_time = time()
    timeCost = end_time - start_time
    result = Result(dist = dist, timeCost = timeCost)
    return result
