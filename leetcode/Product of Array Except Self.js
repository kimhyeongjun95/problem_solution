var productExceptSelf = function(nums) {
    let one = false;
    let twos = false;
    count = 1;
    for (let i = 0 ; i < nums.length; i++) {
        if (!one && nums[i] === 0) {
            one = true;
            continue;
        }
        
        if (!twos && nums[i] === 0) {
            twos = true;
            break;
        }

        count *= nums[i];
    }

    let answer = new Array(nums.length).fill(0);
    if (twos) {
        return answer
    }
    
    if (one) {
        for (let i = 0; i < nums.length; i++) {
            if (nums[i] === 0) {
                answer[i] = count
            }
        }
        return answer
    }

    for (let i = 0; i < nums.length; i++) {
        if (nums[i]) {
            answer[i] = count / nums[i]
        }
    }

    return answer
};

console.log(productExceptSelf([1,2,3,4]))
// [24,12,8,6]
console.log(productExceptSelf([-1,1,0,-3,3]))
// [0, 0, 9, 0, 0]