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

  let idx = 0;
  let idxR = idx + 1;
  let count = 27;
  let result = [];

  while (idx < msg.length) {

    // 2
    while (check[msg.slice(idx, idxR)] && idxR < msg.length) {
      idxR += 1;
    }
    // 2-1
    console.log(check[msg.slice(idx, idxR-1)])
    result.push(check[msg.slice(idx, idxR-1)])
    // 2-2
    check[msg.slice(idx, idxR)] = count;
    count += 1;
    console.log(idx, idxR)
    console.log(result);
    console.log(check);
    idx = idxR - 1;
    idxR = idx + 1;
  }
  

}

console.log(solution("KAKAO"))
// [11, 1, 27, 15]
// console.log(solution("TOBEORNOTTOBEORTOBEORNOT"))
// [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
// console.log(solution("ABABABABABABABAB"))
// [1, 2, 27, 29, 28, 31, 30]


