#include <stdio.h>
#include <stdlib.h>

#define min(a, b) (a < b ? a : b)
#define max(a, b) (a > b ? a : b)

int ccw(long long int x1, long long int y1, long long int x2, long long int y2, long long int x3, long long int y3) {
  long long int k = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1);
  if(k > 0) return 1;
  else if(k < 0) return -1;
  else return 0;
}

int line_cross(int x1, int y1, int x2, int y2, int x3, int y3, int x4, int y4) {
  int case_a = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4);
  int case_b = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2);

  if(case_a == 0 && case_b == 0) { // 한직선 상에 있을때
    if(x1 == x3) {
      // a1~a2 b1~b2
      int a1 = min(y1, y2);
      int a2 = max(y1, y2);
      int b1 = min(y3, y4);
      int b2 = max(y3, y4);
      // 겹친 길이 <= 두 선분의 길이 합
      if(max(a2, b2) - min(a1, b1) <= (a2 - a1) + (b2 - b1)) return 1;
      else return 0;
    }else {
      // 겹친 길이 <= 두 선분의 길이 합
      int a1 = min(x1, x2);
      int a2 = max(x1, x2);
      int b1 = min(x3, x4);
      int b2 = max(x3, x4);
      if(max(a2, b2) - min(a1, b1) <= (a2 - a1) + (b2 - b1)) return 1;
      else return 0;
    }
  }else if(case_a <= 0 && case_b <= 0) {  // 교차하거나 연결되어 있을때
    return 1;
  }else {
    return 0;
  }
}

int main() {
  int x1, y1, x2, y2, x3, y3, x4, y4;
  scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
  scanf("%d %d %d %d", &x3, &y3, &x4, &y4);
  printf("%d\n", line_cross(x1, y1, x2, y2, x3, y3, x4, y4));
}
