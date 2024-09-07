// 나올 수 있으면 1
// 없으면 0

function solution(board) {
  let O_Count = 0;
  let X_Count = 0;
  let O_BINGO = false;
  let X_BINGO = false;
  for (let i = 0; i < board.length; i++) {
    let O_ROW_COUNT = 0;
    let O_COL_COUNT = 0;
    let X_ROW_COUNT = 0;
    let X_COL_COUNT = 0;
    for (let j = 0; j < board[0].length; j++) {
      if (board[i][j] === "O") {
        O_Count += 1;
        O_COL_COUNT += 1;
      }
      if (board[j][i] === "O") {
        O_ROW_COUNT += 1;
      }
      if (board[i][j] === "X") {
        X_Count += 1;
        X_COL_COUNT += 1;
      }
      if (board[j][i] === "X") {
        X_ROW_COUNT += 1;
      }
    }

    if (O_ROW_COUNT === 3 || O_COL_COUNT === 3) O_BINGO = true;
    if (X_ROW_COUNT === 3 || X_COL_COUNT === 3) X_BINGO = true;
  }
  if (board[0][0] === "O" && board[1][1] === "O" && board[2][2] === "O") O_BINGO = true;
  if (board[0][2] === "O" && board[1][1] === "O" && board[2][0] === "O") O_BINGO = true;
  if (board[0][0] === "X" && board[1][1] === "X" && board[2][2] === "X") X_BINGO = true;
  if (board[0][2] === "X" && board[1][1] === "X" && board[2][0] === "X") X_BINGO = true;

  if (O_BINGO && X_BINGO) return 0;
  if (O_Count < X_Count) return 0;
  if (2 <= O_Count - X_Count) return 0;
  if (X_BINGO && X_Count !== O_Count) return 0;
  if (O_BINGO && O_Count - 1 !== X_Count) return 0;
  return 1;
}

console.log(solution(["O.X", ".O.", "..X"]));
// 1
console.log(solution(["OOO", "...", "XXX"]));
// 0
console.log(solution(["...", ".X.", "..."]));
// 0
console.log(solution(["...", "...", "..."]));
// 1
