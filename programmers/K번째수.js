// 프로그래머스 K번째수

// i ~ j 까지 slicing
// i = 2, j = 5
// [1, 5, 2, 6, 3, 7, 4] => [5, 2, 6, 3]
// 정렬
// k = 3
// k번째 숫자 push
// result return

function solution(array, commands) {
    let answer = [];

	for (let command of commands) {
		let [i, j, k] = command;
		let arr = array.slice(i-1, j);
		arr.sort((a, b) => a - b)
		answer.push(arr[k-1])
	}
	return answer;
}

console.log(solution(
	[1, 5, 2, 6, 3, 7, 4],
	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	
))
// [5, 6, 3]