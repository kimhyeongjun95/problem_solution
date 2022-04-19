// 프로그래머스 숫자 게임

// 2xN 명의 사원들
// N명씩 두 팀으로 나눠 숫자게임

// 무작위로 자연수 하나씩 부여
// 각 사원은 딱 한 번씩 경기
// 각 경기당 A 팀에서 한 사원
//           B 팀에서 한 사원
// 서로의 수 공개
// 숫자가 큰 팀 승리 : 승리팀 += 1

// A팀의 출전순서 공개
// B팀이 얻는 최대 승점 return

function solution(A, B) {
	A.sort((a, b) => a - b);
    B.sort((a, b) => a - b);
	let j = 0;
	let answer = 0;
	for (let i=0; i < A.length; i++) {
		if (A[j] < B[i]) {
			j += 1
			answer += 1
		}
	}
	return answer
}

console.log(solution([5,1,3,7], [2,2,6,8]))
// 3
console.log(solution([2,2,2,2], [1,1,1,1]))
// 0
