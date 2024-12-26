function solution(cacheSize, cities) {
  let memory = [];
  let count = 0;

  for (const city of cities) {
    const currentCity = city.toLowerCase();
    if (!memory.includes(currentCity)) {
      memory.push(currentCity);
      if (memory.length > cacheSize) {
        memory.shift();
      }
      count += 5;
    } else {
      const newMemory = memory.filter((v) => v !== currentCity);
      memory = [...newMemory, currentCity];
      count += 1;
    }
  }

  return count;
}

console.log(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]));
// 50
console.log(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]));
// 21
console.log(
  solution(2, [
    "Jeju",
    "Pangyo",
    "Seoul",
    "NewYork",
    "LA",
    "SanFrancisco",
    "Seoul",
    "Rome",
    "Paris",
    "Jeju",
    "NewYork",
    "Rome",
  ])
);
// 60
console.log(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]));
// 16
