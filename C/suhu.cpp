#include <stdio.h>
int main()
{
	int a, ab;
	float celcius, reamur, fahrenheit, rc;
	
	printf("Konversi suhu\n");
	printf("Masukkan jenis suhu yang akan dikoversi\n");
	printf("1. Celcius\n");
	printf("2. Reamur\n");
	printf("3. Fahrenheit\n");
	printf("\n");
	printf("Masukkan pilihan Anda...");
	scanf("%d", &a);
	if (a == 1)
		{
			printf("Anda memilih celcius\n");
			printf("\n");
			printf("Masukkan suhu yang ingin Anda konversi...");
			scanf("%f", &celcius);
			printf("Anda memasukkan %f\n", celcius);
			printf("\n");
			reamur = (float)4/5 * celcius;
			fahrenheit = (float)9/5 * celcius + 32;
			printf("Jika dalam Reamur maka...%2f\n", reamur);
			printf("Jika dalam Fahrenheit maka...%2f\n", fahrenheit);
			printf("\n");
			printf("Terima Kasih");
		}
		else
		if (a==2)
		{
			printf("Anda memilih Reamur\n");printf("\n");
			printf("Masukkan suhu yang ingin Anda konversi...");
			scanf("%f", &reamur);
			printf("Anda memasukkan %f\n", reamur);
			printf("\n");
			celcius = (float)5/4 * reamur;
			fahrenheit = (float)9/4 * reamur + 32;
			printf("Jika dalam Celcius maka...%2f\n", celcius);
			printf("Jika dalam Fahrenheit maka...%2f\n", fahrenheit);
			printf("\n");
			printf("Terima Kasih");
		}
		else
		if (a==3)
		{
			printf("Anda memilih Fahrenheit");
			printf("\n");
			printf("Masukkan suhu yang ingin Anda konversi...");
			scanf("%f", &fahrenheit);
			printf("Anda memasukkan %f\n", fahrenheit);
			printf("\n");
			ab = fahrenheit - 32;
			reamur = (float)4/9 * ab;
			celcius = (float)5/9 * ab;
			printf("Jika dalam Reamur maka...%2f\n", reamur);
			printf("Jika dalam Celcius maka...%2f\n", celcius);
			printf("\n");
			printf("Terima Kasih");
		}
	else
	{
		printf("Perintah yang anda masukkan salah\n");
		printf("Press any key to out of this program");
	}
	return 0;
}
