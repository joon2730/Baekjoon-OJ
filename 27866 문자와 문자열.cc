// https://www.acmicpc.net/problem/27866
// 단어 S와 정수 i가 주어졌을 때, S의 i번째 글자를 출력하는 프로그램을 작성하시오.

#include <string>
#include <iostream>

int main () {
    std::string S;
    int i;

    std::cin >> S >> i;
    std::cout << S[i - 1];
    
}
