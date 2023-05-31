// https://www.acmicpc.net/problem/10807
// 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

#include <iostream>
#include <string>
#include <sstream>

int main() {

    // read input
    int N, v, i;
    std::string s;

    std::cin >> N;

    // https://stackoverflow.com/questions/21567291/why-does-stdgetline-skip-input-after-a-formatted-extraction
    std::getline(std::cin >> std::ws, s);
    std::istringstream iss(s);

    std::cin >> v;

    // count v
    int cnt = 0;
    while (iss >> i) {
        if (i == v) {
            cnt++;
        }
    }

    // print output
    std::cout << cnt;
}