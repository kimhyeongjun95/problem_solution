var maxArea = function(height) {
    let answer = 0;
    let l = 0;
    let r = height.length - 1;

    while (l < r) {
        area = (r - l) * Math.min(height[l], height[r]);
        answer = Math.max(answer, area);

        if (height[l] < height[r]) {
            l += 1;
        } else {
            // if it's same, doesn't matter to move which pointer
            r -= 1;
        }
    }
    return answer

};

console.log(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
// 49
console.log(maxArea([1, 1]))
// 1