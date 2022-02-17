// 프로그래머스 평균 구하기

function solution(arr) {
  let answer = 0;
  for (let i=0; i < arr.length; i++) {
    answer += arr[i]
  }
  return answer / arr.length;
}
console.log(solution([1, 2, 3, 4]));