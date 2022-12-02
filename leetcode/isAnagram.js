// Anagram이란
// 모든 letter들을 한 번만 쓰면서 다른 단어를 만들 수 있도록

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
    const check = new Map();
    const check2 = new Map();
    for (let i = 0; i < s.length; i++) {
        if (!check.has(s[i])) check.set(s[i], 1);
        else check.set(s[i], check.get(s[i]) + 1);
    }
    for (let i = 0; i < t.length; i++) {
        if (!check2.has(t[i])) check2.set(t[i], 1);
        else check2.set(t[i], check2.get(t[i]) + 1);
    }
    for (let [key, val] of check.entries()) {
        if (check2.get(key) !== val) return false;
    }
    for (let [key, val] of check2.entries()) {
        if (check.get(key) !== val) return false;
    }
    return true;
};

console.log(isAnagram("anagram", "nagaram"));
// true
console.log(isAnagram("rat", "car"));
// false
