// 프로그래머스 점프와 순간 이동

// 한 번에 K 칸 or (현재 온 거리) * 2 슈트
// 순간이동 : 건전지 사용 X
// K칸 점프 : 건전지 사용 O

// 건전지 사용량 최소값 return

// 5000 2500 1250 625 (624) 312 156 78 39 (38) 19 (18) 9 (8) 4 2 (1)

// 1. 계속 2로 나눈다
// 2. 나눌수 없을때, 짝수가 되도록 -1 (count + 1)
// 3. 숫자가 1이되면 count + 1 하고 return

function solution(n)
{
    let answer = 1;

    while (true) {
      // 3
      if (n === 1) {
        return answer;
      }

      // 1
      if (n % 2 === 0) {
        n /= 2;
      } else {
        // 2
        n -= 1;
        answer += 1;
      }
    }
}

console.log(solution(5))
// 2
console.log(solution(6))
// 2
console.log(solution(5000))
// 5


