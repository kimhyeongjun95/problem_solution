// 프로그래머스 (2018 카카오 3차) 압축

// LZW 압축

// 1. 알파벳 base 사전 만들기
// 2. 현재 입력(w)이 in check 중 가장 긴 문자열 찾기:
// 2-1. answer에 check (w)val push
// 2-2. check에 w + c : val

function solution(msg) {

  let alpha = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  let check = {}
  // 1
  for (let i = 1; i < 27; i++) {
    check[alpha[i].toUpperCase()] = i
  }

  let count = 27;
  let result = [];
  msg = msg.split('');
  let cur = msg.shift()
  let next = msg[0];
  while (msg.length) {
    if (!check[cur+next] && check[cur]) {
      result.push(check[cur]);
      check[cur + next] = count;
      count += 1;
      cur = msg.shift();
      next = msg[0];
    } else {
      cur = cur + msg.shift();
      next = msg[0];
    }
  } 
  result.push(check[cur]);
  return result;
}

console.log(solution("KAKAO"))
// [11, 1, 27, 15]
console.log(solution("TOBEORNOTTOBEORTOBEORNOT"))
// [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
console.log(solution("ABABABABABABABAB"))
// [1, 2, 27, 29, 28, 31, 30]


