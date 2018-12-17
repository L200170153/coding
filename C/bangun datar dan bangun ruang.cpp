#include <stdio.h>
int main ()

{
	int a, b, c, d, e, f, g, h, i;
	float ab, bc, cd, df, fg, pi=3.14;
	

	printf("Menghitung keliling dan luas bangun datar\n");
	printf("&\n");
	printf("Menghitung luas permukaan dan volume bangun ruang\n");
	printf("\n");
	printf("Menu :\n");
	printf("1. Bangun datar\n");
	printf("2. Bangun ruang\n");
	printf("\n");
	printf("Pilih...");
	scanf("%d", &a);
	printf("\n");
	printf("\n");
	if (a==1)
		{
			printf("Anda memilih bangun datar...\n");
			printf("Bangun datar apa yang ingin anda hitung keliling atau luasnya?\n");
			printf("1. Persegi\n");
			printf("2. Persegi panjang\n");
			printf("3. Lingkaran\n");
			printf("4. Jajaran genjang\n");
			printf("5. Trapesium\n");
			printf("6. Belah ketupat\n");
			printf("7. Layang layang\n");
			printf("8. Segitiga\n");
			printf("9. Segi n\n");
			printf("\n");
			printf("Pilih...");
			scanf("%d", &b);
			printf("\n");
			printf("\n");
			if (b==1)
				{
					printf("Anda memilih Persegi...\n");
					printf("Apa yang ingin Anda hitung?\n");
					printf("1. Luas\n");
					printf("2. Keliling\n");
					printf("Pilih...");
					printf("\n");
					scanf("%d", &c);
					printf("\n");
					printf("\n");
					if (c==1)
					{
						printf("Anda memilih luas...\n");
						printf("Masukkan panjang sisinya...");
						scanf("%d", &d);
						e = d * d;
						printf("Luas perseginya adalah...%d\n", e);
					}
					if (c==2)
					{
						printf("Anda memilih keliling...\n");
						printf("Masukkan panjang sisinya...");
						scanf("%d", &d);	
						e = 4 * d;
						printf("Keliling perseginya adalah...%d\n", e);
					}
					else
					{
						printf("Perintah yang Anda masukkan salah! Mohon isi dengan benar!");
					}
				}
			else
			if (b==2)
				{
					printf("Anda memilih persegi panjang...\n");
					printf("Apa yang ingin Anda hitung?\n");
					printf("1. Luas\n");
					printf("2. Keliling\n");
					printf("Pilih...");
					printf("\n");
					scanf("%d", &c);
					printf("\n");
					printf("\n");
					if (c==1)
					{
						printf("Anda memilih luas...\n");
						printf("Masukkan panjangnya...\n");
						scanf("%d", &d);
						printf("Masukkan lebarnya...\n");
						scanf("%d", &f);
						e = d * f;
						printf("Luas persegi panjangnya adalah...%d\n", e);
					}
					if (c==2)
					{
						printf("Anda memilih keliling...\n");
						printf("Masukkan panjangnya...\n");
						scanf("%d", &d);
						printf("Masukkan lebarnya...\n");
						scanf("%d", &f);
						e = d + f;
						e *= 2 ;
						printf("Keliling perseginya adalah...%d\n", e);
					}
					else
					{
						printf("Perintah yang Anda masukkan salah! Mohon isi dengan benar!");
					}
				}
			if (b==3)
				{
					printf("Anda memilih Lingkaran...\n");
					printf("Apa yang ingin Anda hitung?\n");
					printf("1. Luas\n");
					printf("2. Keliling\n");
					printf("Pilih...");
					printf("\n");
					scanf("%d", &c);
					printf("\n");
					printf("\n");
					if (c==1)
					{
						printf("Anda memilih luas...\n");
						printf("Masukkan jari-jarinya...\n");
						scanf("%d", &d);
						ab = pi * d * d;
						printf("Luas lingkarannya adalah...%f\n", ab);
					}
					if (c==2)
					{
						printf("Anda memilih keliling...\n");
						printf("Masukkan jari-jarinya...\n");
						scanf("%d", &d);
						d *=2;
						ab = pi * d;
						printf("Keliling lingkarannya adalah...%f\n");
					}
					else
					{
						printf("Perintah yang Anda masukkan salah! Mohon isi dengan benar!");
					}
				}
			if (b==4)
				{
					printf("Anda memilih jajaran genjang...\n");
					printf("Apa yang ingin Anda hitung?\n");
					printf("1. Luas\n");
					printf("2. Keliling\n");
					printf("Pilih...");
					printf("\n");
					scanf("%d", &c);
					printf("\n");
					printf("\n");
					if (c==1)
					{
						printf("Anda memilih luas...\n");
						printf("Masukkan alasnya...\n");
						scanf("%d", &d);
						printf("Masukkan tinnginya...\n");
						scanf("%d", &e);
						f = d * e;
						printf("Luas jajaran genjangnya adalah...%d\n", f);
					}
					if (c==2)
					{
						printf("Anda memilih luas...\n");
						printf("Masukkan alasnya...\n");
						scanf("%d", &d);
						printf("Masukkan sisi miringnya...\n");
						scanf("%d", &e);
						f = d + e;
						f *= 2;
						printf("Luas jajaran genjangnya adalah...%d\n", f);
					}
					else
					{
						printf("Perintah yang Anda masukkan salah! Mohon isi dengan benar!");
					}
			}
				
		}
	else
		if (a==2)
		{
			printf("Anda memilih bangun ruang...\n");
			printf("Bangun ruang apa yang ingin anda hitung luas permukaan atau volumenya?\n");
		}
	else
		{
			printf("Pilihan anda salah! Mohon isi dengan benar!");
		}
	return 0;
}
