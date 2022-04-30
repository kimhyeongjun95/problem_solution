// 프로그래머스 피보나치 수

function solution(n) {
  let arr = [0, 1, 1, 2, 3, 5];
  
  if (n > 5) {
    for (let i = 6; i < n+1; i++) {
      arr.push((arr[i-1] + arr[i-2]) % 1234567)
    }
  }
  let answer = arr[n]
  return answer;
}

console.log(solution(3))
// 2
console.log(solution(4))
// 2
console.log(solution(5))
// 5
console.log(solution(6))
// 5
console.log(solution(7))
// 5


