var maxProduct = function(nums) {
    let answer = Math.max(...nums);
    let minNum = nums[0];
    let maxNum = nums[0];

    for (let i = 1; i < nums.length; i++) {
        let val = nums[i];
        let maxPrev = maxNum;
        let minPrev = minNum;
        if (val === 0) {
            maxNum = 0;
            minNum = 0;
            continue
        }
        maxNum = Math.max(val, val * maxPrev, val * minPrev);
        minNum = Math.min(val, val * maxPrev, val * minPrev);

        answer = Math.max(answer, maxNum);
    }

    return answer;
};

console.log(maxProduct([2, 3, -2, 4]));
// 6
console.log(maxProduct([-2, 0, -1]));
// 0