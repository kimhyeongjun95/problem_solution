// 곡괭이, 철 곡괭이, 돌 곡괭이
// 각각 0~5개
// 광물을 캘 때는 피로도 소모

// 곡괭이와 광물에 따른 피로도 테이블 존재
// 각 곡괭이는 종류에 상관없이 5개를 캔 후 더이상 사용 X

// 한 번 사용한 곡괭이는 사용할 수 없을 때까지 사용
// 주어진 순서대로만 캘 수 있음
// 광산에 있는 모든 광물 캐기 or 더 사용할 곡괭이 없을 때까지

// 최소의 피로도 return

function solution(picks, minerals) {
  let count = Infinity;
  const scoreBoard = {
    DIA: {
      diamond: 1,
      iron: 1,
      stone: 1,
    },
    IRON: {
      diamond: 5,
      iron: 1,
      stone: 1,
    },
    STONE: {
      diamond: 25,
      iron: 5,
      stone: 1,
    },
  };
  const find = (type, restPicks, idx, duration, tired) => {
    const currentMineral = minerals[idx];
    const score = scoreBoard[type][currentMineral];
    const hasNoPicks = restPicks.reduce((a, b) => a + b) === 0 && duration === 0;

    if (idx >= minerals.length || hasNoPicks) {
      count = Math.min(tired, count);
      return;
    }

    if (duration === 0) {
      if (restPicks[0] > 0) find("DIA", [restPicks[0] - 1, restPicks[1], restPicks[2]], idx, 5, tired);
      if (restPicks[1] > 0) find("IRON", [restPicks[0], restPicks[1] - 1, restPicks[2]], idx, 5, tired);
      if (restPicks[2] > 0) find("STONE", [restPicks[0], restPicks[1], restPicks[2] - 1], idx, 5, tired);
      return;
    }

    find(type, restPicks, idx + 1, duration - 1, tired + score);
  };

  // picks: [dia, iron, stone]
  if (picks[0] > 0) find("DIA", [picks[0] - 1, picks[1], picks[2]], 0, 5, 0);
  if (picks[1] > 0) find("IRON", [picks[0], picks[1] - 1, picks[2]], 0, 5, 0);
  if (picks[2] > 0) find("STONE", [picks[0], picks[1], picks[2] - 1], 0, 5, 0);
  return count;
}

console.log(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]));
// 12
console.log(
  solution(
    [0, 1, 1],
    ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
  )
);
// 50
