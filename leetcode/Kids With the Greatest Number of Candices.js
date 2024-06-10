/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function (candies, extraCandies) {
  const arr = Array(candies.length);
  const maxNum = Math.max(...candies);
  candies.forEach((v, i) => (arr[i] = v + extraCandies >= maxNum));
  return arr;
};

console.log(kidsWithCandies([2, 3, 5, 1, 3], 3));
// [true, true, true, false, true];
