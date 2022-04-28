// 프로그래머스 최솟값 만들기

// 각각 한 개의 숫자를 뽑아 곱함
// 누적된 값이 최소가 되도록 하는 것이 목표
// 최소값 return

function solution(A,B){

	A.sort((a, b) => a - b)
	B.sort((a, b) => b - a)

	let result = 0;
	for (let i = 0; i < length; i++) {
		result += A[i] * B[i]
	}
	return result;
}

console.log(solution([1, 4, 2], [5, 4, 4]))
// 29
console.log(solution([1,2], [3,4]))
// 10

