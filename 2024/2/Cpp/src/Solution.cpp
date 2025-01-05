#include <iostream>
#include <string>
#include <fstream>
#include "../include/Solution.h"

// PRIVATE:

void Solution::ingestFile(const std::string& filePath){

    std::ifstream inputFile(filePath);

    if (!inputFile.is_open()) {
        throw std::runtime_error("Error while ingesting a file [function: ingest_file()]");
    }

    std::string line;

    while (std::getline(inputFile, line)) {
        std::vector<int> tempList;
        for (char ch : line) {
            if (std::isdigit(ch)) {
                int digit = ch - '0'; 
                // "0" represents a string object
                // while '0' represents a char in cpp
                // substracting char '0' from digit char gives us an integer (character - ASCII value of 0 = integer character)
                tempList.push_back(digit);
            }
        }
        reports.push_back(tempList);
    }

    inputFile.close();
};

bool Solution::isDecreasing(std::vector<int>& report){
    for (size_t i = 1; i < report.size(); ++i){
        if (report[i-1] < report[i]){
            return false;
        }
    }
    return true;
};

bool Solution::isIncreasing(std::vector<int>& report){
    for (size_t i = 1; i < report.size(); ++i){
        if (report[i-1] > report[i]){
            return false;
        }
    }
    return true;
};

bool Solution::isDifferenceCorrect(std::vector<int>& report){
    for (size_t i = 1; i < report.size(); ++i){
        int diff = abs(report[i-1] - report[i]);
        if (diff < 1 || diff > 3){
            return false;
        }
    }
    return true;
};

void Solution::isSafe(){
    for (size_t i = 0; i < reports.size(); ++i){
        if (isDecreasing(reports[i]) || isIncreasing(reports[i])) {
            if (isDifferenceCorrect(reports[i])){
                mappedReports["Safe"].push_back(reports[i]);
            }else{
                mappedReports["Unsafe"].push_back(reports[i]);
            }
        }else{
            mappedReports["Unsafe"].push_back(reports[i]);
        }
    }
};

// PUBLIC:

void Solution::printSafeReports(){
    std::cout << "Safe reports:" << std::endl;
    for (const auto& vec : mappedReports["Safe"]) {
        std::string tempStr;
        for (int num : vec) {
            std::string tempStr2 = std::to_string(num) + " ";
            tempStr += tempStr2;
        }
        std::cout << tempStr << std::endl;
    }

    std::cout << "Unsafe reports:" << std::endl;
    for (const auto& vec : mappedReports["Unsafe"]) {
        std::string tempStr;
        for (int num : vec) {
            std::string tempStr2 = std::to_string(num) + " ";
            tempStr += tempStr2;
        }
        std::cout << tempStr << std::endl;
    }
}

void Solution::printReports(){
    // for debugging purposes
    std::string tempStr;
    std::cout << reports.size() << std::endl;
    for (size_t i = 0; i < reports.size(); ++i){
        std::string tempStr;
        for (size_t j = 0; j < reports[i].size(); ++j) {
            std::string tempStr2 = std::to_string(reports[i][j]) + " ";
            tempStr += tempStr2;
        }
        std::cout << tempStr << std::endl;

    }
}

void Solution::run(){
    isSafe();
    printSafeReports();
    // print_reports();
};

Solution::Solution(const std::string& filePath) {
    ingestFile(filePath);
};

Solution::~Solution(){

};