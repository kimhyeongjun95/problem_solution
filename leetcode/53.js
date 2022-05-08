
var maxSubArray = function(nums) {
    let curSum = 0;
    let maxNum = nums[0];

    for (let i = 0 ; i < nums.length; i++) {
        if (curSum < 0) curSum = 0;
        curSum += nums[i];
        maxNum = Math.max(maxNum, curSum);
    }

    return maxNum;
};

// console.log(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
// console.log(maxSubArray([5,4,-1,7,8]))
console.log(maxSubArray([-2,-1]))