#include <iostream>
#include <vector> // std::vector<int> - data structure
#include <algorithm> // std:sort()
#include <cmath> // std::abs()

class Solution {
  private:
    std::vector<int> firstList;
    std::vector<int> secondList;

  int calcDistance(){
    int sum = 0;

    for (size_t i=0; i < firstList.size(); i++){
      sum += std::abs(firstList[i]-secondList[i]);
    }

    return sum;
  }

  public:

  Solution(std::vector<int> flist, std::vector<int> slist) {
      firstList = flist;
      secondList = slist;

      sort(firstList.begin(), firstList.end());
      sort(secondList.begin(), secondList.end());
  }

  ~Solution() {
  }

  void displayDistance(){
      int distance = calcDistance();
      std::cout << distance << std::endl;
  }
};



int main() {
    std::vector<int> vecFirstList = {3, 4, 2, 1, 3, 3};
    std::vector<int> vecSecondList = {4, 3, 5, 3, 9, 3};

    Solution solution(vecFirstList, vecSecondList);

    solution.displayDistance();

    return 0;
}