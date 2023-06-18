/*
https://www.acmicpc.net/problem/25083
아래 예제와 같이 새싹을 출력하시오.
         ,r'"7
r`-_   ,'  ,/
 \. ". L_r'
   `~\/
      |
      |
*/

#include <string>
#include <iostream>

using std::string;

 const string BUD = 
R"END(wain:
; begin prologue
.import print
.import init
.import new
.import delete
lis $4      ; $4 will always hold 4
.word 4
lis $10     ; $10 will always hold address for print
.word print
lis $12     ; $12 will always hold address for init
.word init 
lis $13     ; $13 will always hold address for new
.word new
lis $14     ; $14 will always hold address for delete
.word delete
lis $11     ; $11 will always hold 1
.word 1
)END";

int main() {

    std::cout << BUD;
}