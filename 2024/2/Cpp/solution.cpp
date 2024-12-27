#include <iostream>
#include <string>

class Solution{

  private:
    std::string file_path;

    void ingest_file(std::string file_path){

    }

  Solution(std::string path){
      file_path = path;
      ingest_file(file_path);
  }

  ~Solution(){
  }

  void run(){
    
  }

};

int main() {
    

    return 0;
}