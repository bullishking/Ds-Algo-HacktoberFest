#include<graphics.h>
#include<conio.h>
#include<stdio.h>

void mpcircle(int xc, int yc, int r)
{
    int x = r;
    int y = 0;
    int p = 0;
    while (x >= y)
    {
        putpixel(xc + y, yc + x, 4);
        putpixel(xc + x, yc + y, 3);
        putpixel(xc - y, yc + x, 10);
        putpixel(xc - x, yc + y, 13);
        putpixel(xc - x, yc - y, 12);
        putpixel(xc - y, yc - x, 14);
        putpixel(xc + y, yc - x, 15);
        putpixel(xc + x, yc - y, 9);
        if (p <= 0)
        {
            y += 1;
            p += 2 * y + 1;
        }

        if (p > 0)
        {
            x -= 1;
            p -= 2 * x + 1;
        }
    }
}
main()
{
	initwindow(800,800);
	mpcircle(350,300,150);
	
	mpcircle(213,154,50);
	mpcircle(487,154,50);
	mpcircle(224,170,30);
	mpcircle(477,170,30);
	
	mpcircle(350,375,75);
	mpcircle(350,335,15);
	line(350,350,350,400);
	arc(350,375,180,0,25);
	
	mpcircle(275,250,35);
	mpcircle(425,250,35);
	mpcircle(275,270,15);
	mpcircle(425,270,15);
	getch();
	closegraph();
}
