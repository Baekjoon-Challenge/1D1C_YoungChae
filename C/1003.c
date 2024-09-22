#include <stdio.h>

int main() {
    
	int DP0[41] = {1, 0, 1, 1, };
	int DP1[41] = {0, 1, 1, 2, };

	for(int i = 4; i < 41; i++) {
		DP0[i] = DP0[i - 1] + DP0[i - 2];
		DP1[i] = DP1[i - 1] + DP1[i - 2];
	}
    
    int T, N;
    scanf("%d", &T);
    
	for (int i = 0; i < T; i++) {
        scanf("%d", &N);
		printf("%d %d\n", DP0[N], DP1[N]);
	}
}