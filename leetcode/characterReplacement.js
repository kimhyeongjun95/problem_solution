/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
 var characterReplacement = function(s, k) {
    if (k >= s.length) return s.length;
    const check = {};
    let answer = 0;
    let l = 0;
    let maxR = 0;
    for (r = 0; r < s.length; r++) {
        check[s[r]] ? check[s[r]] += 1 : check[s[r]] = 1;
        maxR = Math.max(maxR, check[s[r]]);
        const remain = r - l + 1 - maxR;
        if (remain > k) {
            check[s[l]] -= 1;
            l += 1;
        }
        answer = Math.max(maxR, r - l + 1);
    }
    return answer;
};

console.log(characterReplacement('ABAB', 2));
console.log(characterReplacement('AABABBA', 1));