#include <stdio.h>
#include <stdlib.h>

#define min(a, b) (a < b ? a : b)
#define max(a, b) (a > b ? a : b)

int ccw(int x1, int y1, int x2, int y2, int x3, int y3) {
  int k = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1);
  if(k > 0) return 1;
  else if(k < 0) return -1;
  else return 0;
}

int line_cross(int x1, int y1, int x2, int y2, int x3, int y3, int x4, int y4) {
  int case_a = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4);
  int case_b = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2);
  int a1, a2, b1, b2;
  if(case_a == 0 && case_b == 0) { // 한직선 상에 있을때
    if(x1 == x3) {
      // a1~a2 b1~b2
      a1 = min(y1, y2);
      a2 = max(y1, y2);
      b1 = min(y3, y4);
      b2 = max(y3, y4);
      // 겹친 길이 <= 두 선분의 길이 합
      if(max(a2, b2) - min(a1, b1) <= (a2 - a1) + (b2 - b1)) return 1;
      else return 0;
    }else {
      // 겹친 길이 <= 두 선분의 길이 합
      a1 = min(x1, x2);
      a2 = max(x1, x2);
      b1 = min(x3, x4);
      b2 = max(x3, x4);
      if(max(a2, b2) - min(a1, b1) <= (a2 - a1) + (b2 - b1)) return 1;
      else return 0;
    }
  }else if(case_a <= 0 && case_b <= 0) {  // 교차하거나 연결되어 있을때
    return 1;
  }else {
    return 0;
  }
}

int find(int *union_set, int x) {
  if(union_set[x] == x) {
    return x;
  }else {
    return union_set[x] = find(union_set, union_set[x]);
  }
}

int main() {
  int N;
  scanf("%d", &N);
  int **arr = (int**)malloc(sizeof(int*)*N);
  for(int i=0;i<N;i++) {
    arr[i] = (int*)malloc(sizeof(int)*4);
    for(int j=0;j<4;j++) {
      scanf("%d", &arr[i][j]);
    }
  }
  
  int *union_set = (int*)malloc(sizeof(int)*N);
  for(int i=0;i<N;i++) union_set[i] = i;

  int *size = (int*)malloc(sizeof(int)*N);
  for(int i=0;i<N;i++) size[i] = 1;

  for(int i=0;i<N-1;i++) {
    for(int j=i+1;j<N;j++) {
      if(line_cross(arr[i][0], arr[i][1], arr[i][2], arr[i][3], arr[j][0], arr[j][1], arr[j][2], arr[j][3])) {
        int a = find(union_set, i);
        int b = find(union_set, j);
        if(a != b) {
          if(size[a] < size[b]) {
            union_set[a] = b;
            size[b] += size[a];
          } else {
            union_set[b] = a;
            size[a] += size[b];
          }
        }
      }
    }
  }

  int group_cnt = 0;
  int max_size = 0;
  for(int i=0;i<N;i++) {
    int root = find(union_set, i);
    if(root == i) {
      group_cnt++;
      if(size[i] > max_size) {
        max_size = size[i];
      }
    }
  }
  printf("%d\n", group_cnt);
  printf("%d", max_size);
}
