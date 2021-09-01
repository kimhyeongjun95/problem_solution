# 같은 색상이 상하좌우 인접 -> 같은 구역
# 적록색약 R, G 같은 색상으로 보임

# RRRBB 00011
# GGBBB 00111
# BBBRR 11100
# BBRRR 11000
# RRRRR 00000
# 적록색약은 3개로 보이고 아닌사람은 4개로 보임. (구역)
# dfs or bfs

import sys
input = sys.stdin.readline