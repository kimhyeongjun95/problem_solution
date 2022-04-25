// 프로그래머스 최댓값과 최솟값

// s에 나타나는 숫자 중 최소값과 최대값 return


function solution(s) {
	let arr = s.split(' ');
	let result = arr.map(str => {
		return Number(str);
	});
	let answer = String(Math.min(...result)) + " " + String(Math.max(...result))
	return answer
}

console.log(solution("1 2 3 4"))
// "1 4"
console.log(solution("-1 -2 -3 -4"))
// "-4 -1"
console.log(solution("-1 -1"))
// "-1 -1"