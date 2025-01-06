#ifndef SOLUTION_H
#define SOLUTION_H

#include <string>
#include <vector>
#include <unordered_map>

class Solution{
  private:
  // vars
    std::vector<std::vector<int>> reports; // vector due to the fact, that it wont be updated
    std::unordered_map<std::string, std::vector<std::vector<int>>> mappedReports;

  // methods 
    void ingestFile(const std::string& filePath);
    bool isDecreasing(std::vector<int>& report);
    bool isIncreasing(std::vector<int>& report);
    bool isDifferenceCorrect(std::vector<int>& report);
    void isSafe();

  public:
  //  methods
    void run();
    void printSafeReports();
    void printReports();
  // Constructor & Deconstructor
    Solution(const std::string& filePath);
    ~Solution();
};

#endif // SOLUTION_H