 var maxProfit = function(prices) {
    let answer = 0;
    let minNum = prices[0];
    let maxNum = prices[0];
    for (let i = 0; i < prices.length; i++) {
        if (prices[i] > maxNum) {
            maxNum = prices[i]
            answer = Math.max(answer, maxNum - minNum)
        }
        if (prices[i] < minNum) {
            minNum = prices[i]
            maxNum = prices[i]
        }
    }
    return answer;
};

console.log(maxProfit([7,1,5,3,6,4]))
// 5
console.log(maxProfit([7,6,4,3,1]))
// 0