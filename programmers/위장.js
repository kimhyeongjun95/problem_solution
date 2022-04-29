// 프로그래머스 위장

// 서로 다른 옷의 조합의 수를 return
// clothes : [이름, 종류]

// 1. 경우의 수 :( 종류:n+1 * n+1 ....) 
// 2. 모든 경우의 수에서 -1하기

function solution(clothes) {

  let check = {}
  for (let cloth of clothes) {
    check[cloth[1]] = check[cloth[1]] ? check[cloth[1]] + 1 : 1 
  }
  
  let answer = 1;
  for (let key in check) {
    answer *= check[key] + 1
  }
  return answer - 1;

}

console.log(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
// 5
// console.log(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
// 3