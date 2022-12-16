// return
// the length of the longest strictly increasing subsequence

/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function (nums) {
    const dp = Array(nums.length).fill(0);
    dp[nums.length - 1] = 1;
    for (let i = nums.length - 2; i >= 0; i--) {
        let maxNumber = 1;
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] < nums[j]) maxNumber = Math.max(maxNumber, dp[j] + 1);
        }
        dp[i] = maxNumber;
    }
    return Math.max(...dp);
};

console.log(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]));
// 4
console.log(lengthOfLIS([0, 1, 0, 3, 2, 3]));
// // 4
console.log(lengthOfLIS([7, 7, 7, 7, 7, 7, 7]));
// // 1
console.log(lengthOfLIS([4, 10, 4, 3, 8, 9]));
// // 3
