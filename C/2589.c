#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define max(a, b) ((a) > (b) ? (a) : (b))

int **map;

typedef struct {
  int x;
  int y;
  int dist;
} Point;

Point queue[2500];
int front = 0;
int length = 0;

void push(Point p) {
  queue[(front + length) % 2500].x = p.x;
  queue[(front + length) % 2500].y = p.y;
  queue[(front + length) % 2500].dist = p.dist;
  length++;
}

Point pop() {
  Point p = queue[front];
  front = (front + 1) % 2500;
  length--;
  return p;
}

int bfs(int x, int y, int h, int w) {
  int visited[h][w];
  memset(visited, 0, sizeof(visited));

  int dx[4] = {0, 0, 1, -1};
  int dy[4] = {1, -1, 0, 0};
  
  Point p;
  p.x = x;
  p.y = y;
  p.dist = 0;
  push(p);
  visited[y][x] = 1;
  
  while (1) {
    Point current = pop();
    for (int i = 0; i < 4; i++) {
      int nx = current.x + dx[i];
      int ny = current.y + dy[i];
      if (nx >= 0 && nx < w && ny >= 0 && ny < h && map[ny][nx] == 0 && visited[ny][nx] == 0) {
        Point next;
        next.x = nx;
        next.y = ny;
        next.dist = current.dist + 1;
        push(next);
        visited[ny][nx] = 1;
      }
    }
    if (length == 0) {
      return current.dist;
    }
  }
}
  
int main() {
  int h, w;
  scanf("%d %d", &h, &w);

  char c;
  map = (int **)malloc(sizeof(int *) * h);
  for (int i = 0; i < h; i++) {
    getchar();
    map[i] = (int *)malloc(sizeof(int) * w);
    for (int j = 0; j < w; j++) {
      scanf("%c", &c);
      if (c == 'W') {
        map[i][j] = 1;
      }else if(c == 'L') {
        map[i][j] = 0;
      }
    }
  }

  int max_dist = 0, dist;
  for(int i=0;i<h;i++){
    for(int j=0;j<w;j++){
      if (map[i][j] == 1) continue;
      dist = bfs(j, i, h, w);
      max_dist = max(max_dist, dist);
    }
  }
  printf("%d\n", max_dist);
}