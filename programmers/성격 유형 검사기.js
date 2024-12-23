function solution(survey, choices) {
  const check = ["R", "T", "C", "F", "J", "M", "A", "N"].reduce((acc, cur) => {
    acc[cur] = 0;
    return acc;
  }, {});

  for (let i = 0; i < survey.length; i++) {
    const [negative, positive] = survey[i].split("");
    const choice = choices[i];
    const score = Math.abs(4 - choice);
    if (choice < 4) {
      check[negative] += score;
    }
    if (choice > 4) {
      check[positive] += score;
    }
  }

  let answer = "";

  const checkObj = (fir, sec) => {
    if (check[fir] >= check[sec]) answer += fir;
    else answer += sec;
  };
  checkObj("R", "T");
  checkObj("C", "F");
  checkObj("J", "M");
  checkObj("A", "N");

  return answer;
}

console.log(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]));
// TCMA

console.log(solution(["TR", "RT", "TR"], [7, 1, 3]));
// "RCJA"
