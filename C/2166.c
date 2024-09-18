#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
  int N;
  scanf("%d", &N);

  int **arr = (int**)malloc(sizeof(int*) * N);

  for(int i=0;i<N;i++) {
    arr[i] = (int*)malloc(sizeof(int) * 2);
    scanf("%d %d", &arr[i][0], &arr[i][1]);
  }

  long long mem = 0;
  for(int i=1;i<N;i++) {
    mem += ((long long)arr[i-1][0] * arr[i][1]);
    mem -= ((long long)arr[i-1][1] * arr[i][0]);
  }
  mem += ((long long)arr[N-1][0] * arr[0][1]);
  mem -= ((long long)arr[N-1][1] * arr[0][0]);
  
  printf("%.1f", ((long long)((long double)llabs(mem) * 10.0 + 0.5)) / 2.0 / 10.0);
}