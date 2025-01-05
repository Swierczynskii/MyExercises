#include <iostream>
#include <string>
#include <regex>
#include "../include/Solution.h"

// PRIVATE:
void Solution::getMuls(const std::string& data){

    std::regex const pattern(R"(mul\((\d{1,3}),(\d{1,3})\))");
    std::smatch m; 
  
    // if (regex_search(data, m, pattern)) {
    //     for (int i=1; i<m.size(); i++) {
    //         std::cout << m[i] << std::endl;
    //     }
    // }
}
// PUBLIC:

void Solution::addMulResults(){

}

void Solution::printMuls(){

}

Solution::Solution(const std::string& corrMem) {
    getMuls(corrMem);
};

Solution::~Solution(){

};