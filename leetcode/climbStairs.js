// takes n steps to reach the top
// Each time either climb 1 or 2 steps
// how many distinct ways can you climb to the top?

/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
    const dp = Array(n).fill(0);
    for (let i = 0; i < n + 1; i++) {
        if (i === 0) continue;
        else if (i === 1) dp[i] = 1;
        else if (i === 2) dp[i] = 2;
        else dp[i] = dp[i - 1] + dp[i - 2];
    }
    return dp[n];
};

console.log(climbStairs(2));
// 2
console.log(climbStairs(3));
