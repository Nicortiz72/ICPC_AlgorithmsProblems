#include<stdio.h>
#include<math.h>
int N=10000001;

int main() {
	int M[N] = {0};
	double S = 0;
	for(int i = 1; i < N; i++) {
		S += log10(i);
		M[i] = (int)S;
	}
	int c,n;
	scanf("%d", &c);
	for(int i=0;i<c;i++){
		scanf("%d", &n);
		printf("%d\n", M[n]+1);
	}
    return 0;
}
