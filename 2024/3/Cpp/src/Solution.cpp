#include <iostream>
#include <string>
#include <sstream>
#include <regex>
#include "../include/Solution.h"

// PRIVATE:
void Solution::getMuls(const std::string& data){
    // https://en.cppreference.com/w/cpp/regex/regex_iterator
    std::regex const mulPattern(R"(mul\((\d{1,3}),(\d{1,3})\))");
    std::regex const digitPattern(R"(\d{1,3})");
  
    auto mulMatchBegin = std::sregex_iterator(data.begin(), data.end(), mulPattern);
    auto mulMatchEnd = std::sregex_iterator();

    for (std::sregex_iterator i = mulMatchBegin; i != mulMatchEnd; ++i){
        std::smatch match = *i;
        std::string matchStr = match.str();

        auto digitMatchBegin = std::sregex_iterator(matchStr.begin(), matchStr.end(), digitPattern);
        auto digitMatchEnd = std::sregex_iterator();

        int mul = 1;

        for (std::sregex_iterator i = digitMatchBegin; i != digitMatchEnd; ++i){
            std::smatch digitMatch = *i;
            int matchedDigit = std::stoi(digitMatch.str());

            mul *= matchedDigit;
        }
        corruptedMemVec.push_back(mul);
    }
}

void Solution::addMulResults(){
    summedVals = 0;
    for (size_t i = 0; i < corruptedMemVec.size(); ++i){
        summedVals += corruptedMemVec[i];
    }
}

// PUBLIC:

int Solution::getSum() const{
    return summedVals;
}

Solution::Solution(const std::string& corrMem) {
    getMuls(corrMem);
    addMulResults();
};

Solution::~Solution(){};