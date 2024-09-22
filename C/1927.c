#include <stdio.h>
#include <stdlib.h>
#define MAX 1000000

int heap[MAX];
int heapSize = 0;

void insert(int data) {
    int key = heapSize;
    heap[heapSize++] = data;
    
    while (key != 0 && heap[key] < heap[(key - 1) / 2]) {
        int temp = heap[key];
        heap[key] = heap[(key - 1) / 2];
        heap[(key - 1) / 2] = temp;
        
        key = (key - 1) / 2;
    }
}

int delete() {
    if (heapSize == 0) return 0;
    int root = heap[0];
    
    heap[0] = heap[--heapSize];
    
    int key = 0;
    while (1) {
        int left = key * 2 + 1;
        int right = key * 2 + 2;
        int max_key = key;
        
        if (left < heapSize && heap[max_key] > heap[left]) max_key = left;
        if (right < heapSize && heap[max_key] > heap[right]) max_key = right;
        
        if (max_key == key) break;
        
        int temp = heap[key];
        heap[key] = heap[max_key];
        heap[max_key] = temp;
        
        key = max_key;
    }
    return root;
}

int main() {
    int n;
    scanf("%d", &n);
    
    for (int i = 0; i < n; i++) {
        int data;
        scanf("%d", &data);
        if (data == 0) printf("%d\n", delete());
        else insert(data);
    }
}