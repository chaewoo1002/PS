#include <stdio.h>

int main() {
    int n, chess[6] = {1, 1, 2, 2, 2, 8};
    
    for (int i = 0; i < 6; i++) {
        scanf("%d", &n);
        printf("%d ", chess[i] - n);
    }
    return 0;
}