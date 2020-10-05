#include<graphics.h>
#include<stdio.h>
#include<dos.h>
#include<conio.h>
int main(){
int gd=DETECT,gm;
int x,y,i;
initgraph(&gd,&gm,"C:\\TURBOC3\\BGI");
x=getmaxx()/2;
y=getmaxy()/2;
for(i=30;i<200;i++)
{
delay(50);
setcolor(i/10);
arc(x,y,0,180,i-10);
}
getch();
closegraph();
return 0;
}