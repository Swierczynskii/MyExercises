import numpy as np
from typing import List

FIRST_LIST = [3,4,2,1,3,3]
SECOND_LIST = [4,3,5,3,9,3]


class Solution():

  def __init__(self, flist, slist):
    if len(flist) == len(slist):
      flist.sort()
      slist.sort()
      self._first_list: List = flist
      self._second_list: List = slist
    else:
      raise Exception("Lists have to be the same length!")

  def get_lists_distance(self):
    return sum([abs(first_id-sec_id) for first_id, sec_id in zip(self._first_list, self._second_list)])
  

def numpy_get_lists_distance(flist, slist):   
  return sum(np.abs(np.sort(np.array(flist))-np.sort(np.array(slist))))


if __name__ == '__main__':
  '''Solution based on a numpy library'''
  print(numpy_get_lists_distance(FIRST_LIST, SECOND_LIST))

  '''Solution based on a python list manipulation'''
  solution = Solution(FIRST_LIST, SECOND_LIST)
  print(solution.get_lists_distance())