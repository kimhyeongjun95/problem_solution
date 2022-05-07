// 프로그래머스 타겟 넘버

function solution(numbers, target) {
    let answer = 0;
    const find = (count, sum) => {

        if (count === numbers.length) {
            if (sum === target) {
                answer += 1;
            }
            return;
        }
        
        find(count+1, sum + numbers[count]);
        find(count+1, sum - numbers[count]);
    }
    find(0, 0)
    return answer;
}

// console.log(solution(
// 	[1, 1, 1, 1, 1],
// 	3
// ))
// 5
console.log(solution(
	[4, 1, 2, 1],
	4,
))
// 2