
var maxSubArray = function(nums) {
    let j = 0;
    let maxNum = -9999999;
    if (nums.length === 1) {
        return nums[0];
    }
    for (let i = 0; i < nums.length; i++) {
        j = i;
        while (j < nums.length) {
            result = nums.slice(i, j+1).reduce((a, b) => a + b);
            if (result < 0) {
                j = i;
                break;
            }
             maxNum = Math.max(maxNum, result);
            j += 1;
        };
    }
    return maxNum;
};

// console.log(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
console.log(maxSubArray([5,4,-1,7,8]))