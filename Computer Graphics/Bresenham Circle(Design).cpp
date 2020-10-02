#include<graphics.h>
#include<conio.h>
#include<stdio.h>
void drawCircle(int xc, int yc, int x, int y)
{
	putpixel(xc+x , yc+y , 10);
	putpixel(xc-x, yc+y , 4);
	putpixel(xc+x , yc-y, 3);
	putpixel(xc-x, yc-y, 9);
	putpixel(xc+y , yc+x , 11);
	putpixel(xc-y, yc+x , 14);
	putpixel(xc+y , yc-x, 13);
	putpixel(xc-y, yc-x, 15);
}
void bcircle(int xc, int yc, int r)
{
	int x=0,y=r,d=3-(2*r);
	drawCircle(xc,yc,x,y);
	while(x<=y)
	{
		if(d<=0)
		{
			d=d+(4*x)+6;
		}
		else
		{
			d=d+(4*x)-(4*y)+10;
			y=y-1;
		}
		x=x+1;
		drawCircle(xc,yc,x,y);
	}
}
main()
{
	int r;
	initwindow(800,800);
	r=200;
	while(r<=300)
	{
		bcircle(400,400,r);
		r=r+20;
	}
	r=10;
	while(r<=50)
	{
		bcircle(150,400,r);
		r=r+10;
	}
	r=10;
	while(r<=50)
	{
		bcircle(650,400,r);
		r=r+10;
	}
	r=10;
	while(r<=50)
	{
		bcircle(400,150,r);
		r=r+10;
	}
	r=10;
	while(r<=50)
	{
		bcircle(400,650,r);
		r=r+10;
	}
	r=10;
	while(r<=100)
	{
		bcircle(300,400,r);
		r=r+10;
	}
	r=10;
	while(r<=100)
	{
		bcircle(500,400,r);
		r=r+10;
	}
	r=10;
	while(r<=100)
	{
		bcircle(400,300,r);
		r=r+10;
	}
	r=10;
	while(r<=100)
	{
		bcircle(400,500,r);
		r=r+10;
	}
	r=20;
	while(r<=100)
	{
		bcircle(400,400,r);
		r=r+20;
	}
	getch();
	closegraph();
}
