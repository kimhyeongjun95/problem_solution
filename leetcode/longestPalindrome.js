// return longest palindrome substring

/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
    const checkPalindrome = (sub) => {
        for (let k = 0; k < parseInt(sub.length / 2); k++) {
            if (sub[k] !== sub[sub.length - 1 - k]) return false;
        }
        return true;
    };
    let answer = "";
    for (let i = 1; i < s.length; i++) {
        for (let j = 0; j < s.length - i + 1; j++) {
            const temp = s.slice(j, j + i);
            if (checkPalindrome(temp)) answer = temp;
        }
    }
    if (checkPalindrome(s)) answer = s;
    return answer;
};

console.log(longestPalindrome("babad"));
// "bab" or "aba"
console.log(longestPalindrome("cbbd"));
// "bb"
