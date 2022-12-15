// return
// the length of the longest strictly increasing subsequence

/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function (nums) {
    let answer = 1;
    const dp = Array(nums.length + 1).fill(0);

    return answer;
};

console.log(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]));
// 4
console.log(lengthOfLIS([0, 1, 0, 3, 2, 3]));
// 4
console.log(lengthOfLIS([7, 7, 7, 7, 7, 7, 7]));
// 1
console.log(lengthOfLIS([4, 10, 4, 3, 8, 9]));
// 3
