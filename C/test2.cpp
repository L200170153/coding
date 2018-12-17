#include <stdio.h>

int main()
{
	int f, s, add, substract, multiply;
	float divide;
	
	printf("Enter two integer\n");
	scanf("%d%d", &f, &s);
	
	add = f + s;
	substract = f - s;
	multiply = f * s;
	divide = f / (float)s;
	
	printf("sum = %d\n", add);
	printf("substract = %d\n", substract);
	printf("multiply = %d\n", multiply);
	printf("Division = %2f\n", divide);
	printf("\n");
	printf("\n");
	
	
	return 0;
	
}
