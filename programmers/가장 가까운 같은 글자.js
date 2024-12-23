// s의 각 위치마다
// 자신보다 앞에 같은 글자 X: -1
// 자신보다 앞에 같은 글자 O :거리 수 표현

function solution(s) {
  const check = {};
  const arr = [];

  for (let i = 0; i < s.length; i++) {
    const current = s[i];
    console.log(check[current]);

    if (check[current] !== undefined) {
      arr.push(i - check[current]);
    } else {
      arr.push(-1);
    }

    check[current] = i;
  }

  return arr;
}

console.log(solution("banana"));
// [-1, -1, -1, 2, 2, 2]
console.log(solution("foobar"));
// [-1, -1, 1, -1, -1, -1]
