
var groupAnagrams = function(strs) {
    strs.sort()
    let check = {};
    for (let i = 0; i < strs.length; i++) {
        let temp = strs[i].split('').sort().join('');
        check[temp] == null ? check[temp] = [strs[i]] : check[temp].push(strs[i]);
    }
    return Object.values(check);
};

console.log(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
// [["bat"],["nat","tan"],["ate","eat","tea"]]