#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int N;
int* queen; // 해당 i번째 행의 퀸 위치(열)

int dfs(int pos) {
  int cnt = 0;
  if (pos == N) return 1;
  for (int i = 0; i < N; i++) {
    int flag = 1;
    for (int j = 0; j < pos; j++) {
      if (queen[j] == i || abs(queen[j]-i) == pos-j) {
        flag = 0;
        break;
      }
    }
    if (flag) {
      queen[pos] = i;
      cnt += dfs(pos+1);
    }
  }
  return cnt;
}

int main() {
  scanf("%d", &N);
  queen = (int*)malloc(sizeof(int)*N);
  printf("%d", dfs(0));
}