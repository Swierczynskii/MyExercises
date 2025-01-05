import re
from typing import List, Tuple

class Solution:

    def __init__(self, data):
        self._corr_memory :str = data
        self._mem_list: List[Tuple] = self._get_muls()
        self.summed_val: int = 0

    def _get_muls(self):
        return re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", self._corr_memory)
       
    def mul_and_add_results(self):
        for muls in self._mem_list:
            # print(sel)
            self.summed_val += int(muls[0])*int(muls[1])

    def print_muls(self):
        for mul in self._mem_list:
            print(mul)



if __name__ == '__main__':
    corrupted_memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))mul(123, 123)"
  
    solution = Solution(corrupted_memory)
    solution.mul_and_add_results()
    print("Solution: ", solution.summed_val)

