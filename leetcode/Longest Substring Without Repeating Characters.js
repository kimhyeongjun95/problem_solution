var lengthOfLongestSubstring = function(s) {

    let temp = new Set();
    let l = 0;
    let count = 0;
    for (let i = 0; i < s.length; i++) {
        while (temp.has(s[i])) {
            count = Math.max(count, temp.size);
            temp.delete(s[l])
            l += 1;
        }
        temp.add(s[i]);
    }
    count = Math.max(count, temp.size);
    return count;
};
console.log(lengthOfLongestSubstring("abcabcbb"))
console.log(lengthOfLongestSubstring("dvdf"))