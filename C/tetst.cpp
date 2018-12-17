#include <stdio.h>

int main()
{
	/*ini variebel*/
	int q, first, second, sum, t, a, n;
	float luas;
	
	
	/*Hello World*/
	printf("Hello World\n");
	
	
	/*masukkan angka*/
	printf("Enter an integer\n");
	/*fungsi printf("... mirip dengan writeln*/
	/*fungsi scanf("%d... mirip dengan readln*/
	scanf("%d", &q);
	printf("Integer that you have entered is %d\n", q);
	printf("\n");
	printf("\n");
	
	/*penambahan*/
	printf("Enter two integer to add\n");
	scanf("%d%d", &first, &second);
	
	sum = first + second;
	printf("Sum of entered number = %d\n", sum);
	printf("\n");
	printf("\n");
	
	
	/*menghitung luas segi3*/
	printf("Enter height and base\n");
	printf("Height...");
	scanf("%d", &t);
	printf("Base...");
	scanf("%d", &a);
	luas = 0.5*t*a;
	printf("Area of triangle is %f", luas);
	printf("\n");
	printf("\n");
	
	
	
	/*odd or even*/
	printf("Enter an integer\n");
	scanf("%d", &n);
	/*if n is completely divisible by 2 then prints even otherwise n is odd*/
	/*ganjil atau genap*/
	if (n%2 == 0)
	/*tanda % adalah tanda div (sisa hasil bagi), maksud dari fungsi diatas adalah jika n dibagi 2 bersisa 0 maka n adalah bilangan genap/even*/
		printf("Even\n");
		else
		printf("Odd\n");
	printf("\n");
	printf("\n");
	
	
	
	
	return 0;
}
