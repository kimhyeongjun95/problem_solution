// 1 ~ n번으로 분류되는 개인정보 n개
// 약관 종류는 여러 가지
// 갹 악관마다 개인정보 보관 유효기간 존재
// 각 개인정보가 어떤 약관으로 수집됐는지 알고 있음
// 수집된 개인정보는 유효기간전까지만 보관 가능

// 오늘 날짜로 파기해야할 개인정보 번호들 구하기
// 모든 달은 28일

// 파기해야할 개인정보의 번호를 오름차순으로 return

function solution(today, terms, privacies) {
  const [curYear, curMonth, curDay] = today.split(".").map((v) => parseInt(v));
  const check = {};
  const result = [];

  for (const term of terms) {
    const [type, month] = term.split(" ");
    check[type] = parseInt(month);
  }

  for (let i = 0; i < privacies.length; i++) {
    const privacy = privacies[i];
    const [date, type] = privacy.split(" ");
    const [year, month, day] = date.split(".").map((v) => parseInt(v));

    let nextYear = year + Math.floor(check[type] / 12);
    let nextMonth = month + (check[type] % 12);
    let nextDay = day - 1;

    if (nextMonth > 12) {
      nextYear += 1;
      nextMonth %= 12;
    }
    if (nextDay === 0) {
      nextDay = 28;
      nextMonth -= 1;
    }

    if (
      curYear > nextYear ||
      (curYear === nextYear && curMonth > nextMonth) ||
      (curYear === nextYear && curMonth === nextMonth && curDay > nextDay)
    )
      result.push(i + 1);
  }
  return result;
}

console.log(
  solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
);

// [1, 3]

console.log(
  solution(
    "2020.01.01",
    ["Z 3", "D 5"],
    ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
  )
);

// [1, 4, 5]
