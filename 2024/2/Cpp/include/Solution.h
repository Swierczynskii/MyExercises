#ifndef SOLUTION_H
#define SOLUTION_H

#include <string>
#include <vector>
#include <unordered_map>

class Solution{

  public:
    void run();

    void printSafeReports();

    void printReports();

    Solution(const std::string& filePath);

    ~Solution();
  
  private:
    std::vector<std::vector<int>> reports; // vector due to the fact, that it wont be updated
    std::unordered_map<std::string, std::vector<std::vector<int>>> mappedReports;

    void isSafe();

    void ingestFile(const std::string& filePath);

    bool isDecreasing(std::vector<int>& report);

    bool isIncreasing(std::vector<int>& report);

    bool isDifferenceCorrect(std::vector<int>& report);

};

#endif // SOLUTION_H