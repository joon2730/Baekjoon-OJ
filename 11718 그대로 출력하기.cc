// https://www.acmicpc.net/problem/11718
// 입력 받은 대로 출력하는 프로그램을 작성하시오.

#include <string>
#include <iostream>

int main() {
    std::string s;

    while (std::getline(std::cin, s)) {
        std::cout << s << std::endl;
    }
}