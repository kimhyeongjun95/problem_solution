// coins: different denominations
// amount: total amount of money

// return the fewest number of coins
// to make up that amount

// if cannot be made, return -1

/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function (coins, amount) {
    const dp = Array(amount + 1).fill(amount + 1);
    dp[0] = 0;
    for (let i = 1; i < dp.length; i++) {
        for (const coin of coins) {
            if (i - coin >= 0) {
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
    }
    if (dp[amount] === amount + 1) return -1;
    return dp[amount];
};

console.log(coinChange([1, 2, 5], 11));
// 3
console.log(coinChange([2], 3));
// // -1
console.log(coinChange([1], 0));
// // 0
