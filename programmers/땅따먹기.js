// 프로그래머스 땅따먹기
// N행 4열

// 1행부터 밟으면서 내려올때, 같은 열을 연속해서 밟을 수 없음
// 최대 얻을 수 있는 점수 return

function solution(land) {
    const N = land.length;
    dp = Array.from(Array(N), () => Array(4).fill(0));
    for (let i = 0; i < 4; i++) dp[0][i] += land[0][i];
    for (let i = 1; i < N; i++) {
        for (let j = 0; j < 4; j++) {
            let maxNum = 0;
            for (let k = 0; k < 4; k++) {
                if (j == k) continue;
                maxNum = Math.max(maxNum, dp[i - 1][k]);
            }
            dp[i][j] = land[i][j] + maxNum;
        }
    }
    return Math.max(...dp[N - 1]);
}

console.log(
    solution([
        [1, 2, 3, 5],
        [5, 6, 7, 8],
        [4, 3, 2, 1],
    ])
);
// 16
