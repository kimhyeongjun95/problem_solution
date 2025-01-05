// 10초 전 이동
// - 남은 시간 10초 미만 => 처음 위치
// 10초 후 이동
// - 남은 시간 10초 미만 => 마지막 위치
// 오프닝 건너뛰기
// - 현재 위치가 오프닝 구간인 경우, 오프닝이 끝나는 위치 이동

function solution(video_len, pos, op_start, op_end, commands) {
  const convertToMinute = (time) => {
    return time
      .split(":")
      .map((v) => parseInt(v))
      .map((v, idx) => (idx === 0 ? v * 60 : v))
      .reduce((a, b) => a + b);
  };
  4;
  const videoLen = convertToMinute(video_len);
  let curTime = convertToMinute(pos);
  const startTime = convertToMinute(op_start);
  const endTime = convertToMinute(op_end);
  if (startTime <= curTime && curTime <= endTime) curTime = endTime;

  for (const command of commands) {
    curTime += command === "next" ? 10 : -10;
    if (curTime < 0) curTime = 0;
    if (curTime > videoLen) curTime = videoLen;
    if (startTime <= curTime && curTime <= endTime) curTime = endTime;
  }

  const hour = Math.floor(curTime / 60)
    .toString()
    .padStart(2, "0");
  const minute = (curTime % 60).toString().padStart(2, "0");
  return hour + ":" + minute;
}

console.log(solution("34:33", "13:00", "00:55", "02:55", ["next", "prev"]));
// "13:00"
console.log(solution("10:55", "00:05", "00:15", "06:55", ["prev", "next", "next"]));
// "06:55"
console.log(solution("07:22", "04:05", "00:15", "04:07", ["next"]));
// "04:17"
