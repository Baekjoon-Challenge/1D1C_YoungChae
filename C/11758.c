#include <stdio.h>

int main() {
  int p1x, p1y, p2x, p2y, p3x, p3y;
  scanf("%d %d %d %d %d %d", &p1x, &p1y, &p2x, &p2y, &p3x, &p3y);
  
  // ux*uy - vy*vx
  int k = (p2x - p1x) * (p3y - p1y) - (p2y - p1y) * (p3x - p1x);
  if(k < 0) {
    printf("-1");
  }
  else if(k == 0) {
    printf("0");
  }
  else {
    printf("1");
  }
  
}