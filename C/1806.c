#include <stdio.h>
#include <stdlib.h>

int main() {
  int N, S;
  scanf("%d %d", &N, &S);
  
  int *arr = (int*)malloc(sizeof(int)*(N+1));
  arr[0] = 0;
  for(int i=1;i<N+1;i++) {
    scanf("%d", &arr[i]);
    arr[i] += arr[i-1];
  }

  int start = 0;
  int end = 1;
  int min_len = N+1;
  while(1) {
    if(arr[end] - arr[start] >= S) {
      if(min_len > end - start) {
        min_len = end - start;
      }
      // start 포인터 당기기
      start++;
    }
    else {
      if(end == N) break;
      // end 포인터 밀기
      end++;
    }
  }
  if(min_len < N+1) {
    printf("%d", min_len);
  }
  else {
    printf("0");
  }

}