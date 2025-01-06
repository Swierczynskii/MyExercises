#ifndef SOLUTION_H
#define SOLUTION_H

#include <string>
#include <vector>

class Solution{
  private:
  // vars
    std::string corruptedMemory;
    std::vector<int> corruptedMemVec;
    int summedVals;
  // methods 
    void getMuls(const std::string& data);
    void addMulResults();


  public:
  // methods
    int getSum() const;
  // Constructor & Destructor
    Solution(const std::string& corrMem);
    ~Solution();
};

#endif // SOLUTION_H