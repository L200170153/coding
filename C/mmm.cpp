#include <stdio.h>

int main ()
{
	int a, b;
	printf("Masukkan angka\n");
	scanf("%d", &a);
	b= a++ + 5;
	printf("Hasil %d\n", b);
	return 0;
}
