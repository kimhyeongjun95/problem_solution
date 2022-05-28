 var containsDuplicate = function(nums) {
    let check = new Set();
    for (let i = 0; i < nums.length; i++) {
        if (check.has(nums[i])) {
            return true
        }
        check.add(nums[i])
    }
    return false
};

console.log(containsDuplicate([1,2,3,1]))
// true
console.log(containsDuplicate([1,2,3,4]))
// false