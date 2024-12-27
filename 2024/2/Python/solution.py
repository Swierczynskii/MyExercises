import os
from typing import List, Dict

class Solution:

  def __init__(self, path):
    self._reports: List[List[int]]
    self._safe_dictionary: Dict[str, List[List[int]]]
    self._path: str = path
  
  def _is_decreasing(self, reports):
    return reports == sorted(reports, reverse=True)

  def _is_increasing(self, reports):
    return reports == sorted(reports)
  
  def _is_difference_correct(self, report):
    for idx, level in enumerate(report[:-1]):
      abs_val = abs(level - report[idx+1])
      if abs_val > 3 or abs_val == 0:
        return False
    return True

  def _ingest_input(self, path):
    with open(path, "r") as f:
      higher_list = []
      for line in f:
        lower_list = [int(letter) for letter in line.split() if letter.isdigit()]
        higher_list.append(lower_list)
      self._reports = higher_list

  def _is_safe(self):

    safe_reports = []
    unsafe_reports = []
    for report in self._reports:
      if self._is_decreasing(report) or self._is_increasing(report):
        if self._is_difference_correct(report):
          safe_reports.append(report)
        else:
          unsafe_reports.append(report)
      else:
        unsafe_reports.append(report)
    self._safe_dictionary = {"Safe":safe_reports, "Unsafe":unsafe_reports}

  def run(self):
    self._ingest_input(self._path)
    self._is_safe()
    print(self._safe_dictionary)

if __name__ == '__main__':
  input_path = os.path.dirname(os.path.realpath(__file__)).replace("Python", "input.txt")
  
  solution = Solution(input_path)
  solution.run()

