// 프로그래머스 멀리 뛰기

// 한번에 1칸 or 2칸
// 칸이 총 4개일 경우 5가지 방법으로 맨 끝간에 도달

// 사용될 칸의 수 n이 주어지면
// return 방법 몇가지 % 1234567 

function solution(n) {
    const dp = [1, 1, 2];
    for (let i = 2; i < n+1; i++) dp[i] = (dp[i-1] + dp[i-2]) % 1234567;
    return dp[n]
}

console.log(solution(4))
// 5
console.log(solution(3))
// 3