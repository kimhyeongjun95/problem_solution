var isPalindrome = function(x) {
    x = String(x).split('');
    for (let i = 0; Math.round(i < x.length / 2); i++) {
        if (x[i] !== x[x.length-i-1]) return false;
    }
    return true;
};

console.log(isPalindrome(121))
console.log(isPalindrome(-121))
console.log(isPalindrome(10))