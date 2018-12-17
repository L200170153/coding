#include<stdio.h>
int main()

{
	int a;
	float b;
	
	printf("Menentukan bilangan ganjil atau genap!\n");
	printf("Masukkan angka yang ingin anda tentukan!\n");
	scanf("%d", &a);
	if (a == 0)
		printf("Bilangan yang anda masukkan adalah angka nol");
		else
		if (a % 2 == 1)
		printf("Bilangan yang anda masukkan adalah bilangan ganjil");
		else
		if (a % 2 == 0)
		printf("Bilangan yang anda masukkan adalah bilangan genap");
		
		
		
	return 0;	
} 
