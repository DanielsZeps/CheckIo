from typing import List
from math import floor

def checkio(data: List[int]):
    data.sort()
    if len(data) % 2 == 0:
        return (data[floor(len(data)/2)-1] + data[floor(len(data)/2)]) / 2
    else:
        return data[floor(len(data)/2)]
    #replace this for solution
