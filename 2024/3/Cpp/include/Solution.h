#ifndef SOLUTION_H
#define SOLUTION_H

#include <string>
#include <vector>

class Solution{

  public:

    void addMulResults();

    void printMuls();

    Solution(const std::string& corrMem);

    ~Solution();
  
  private:
  
    std::string corruptedMemory;
    std::vector<int> corruptedMemVec;
    int summedVals;

    void getMuls(const std::string& data);

};

#endif // SOLUTION_H