// 프로그래머스 카드 뭉치

function solution(cards1, cards2, goal) {
  let idx = 0;
  while (true) {
    if (idx >= goal.length) return "YES";
    if (goal[idx] === cards1[0]) {
      idx += 1;
      cards1.shift();
      continue;
    } else if (goal[idx] === cards2[0]) {
      idx += 1;
      cards2.shift();
      continue;
    } else return "NO";
  }
}

console.log(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]));
// YES
