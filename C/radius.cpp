#include<stdio.h>

int main()
{
	int   c, d, e, f;
	float pi = 3.14, a, b,ab, cd;
	
	printf("Insert radius\n");
	scanf("%f", &a);
	b = pi*a*a;
	printf("Area = %f\n", b);
	
	printf("Insert two integers...\n");
	scanf("%d%d", &c, &d);
	ab = c % d;
	printf("Hasil div 2 angka tersebut adalah %2f\n", ab);
	
	
	return 0;
}
