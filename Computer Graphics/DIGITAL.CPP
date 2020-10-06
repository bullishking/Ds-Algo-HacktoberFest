#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#include<graphics.h>
#include<dos.h>
#include<conio.h>
#include<string.h>
int main(){
int gd=DETECT,gm;
int midx,midy;
long mytime;
char date[256];
initgraph(&gd,&gm,"C://TURBOC3//BGI");
midx=getmaxx()/2;
midy=getmaxy()/2;
while(!kbhit())
{
cleardevice();
mytime=time(NULL);
strcpy(date,ctime(&mytime));
settextjustify(CENTER_TEXT,CENTER_TEXT);
settextstyle(TRIPLEX_FONT, HORIZ_DIR,3);
moveto(midx,midy);
outtext(date);
sleep(1);
}
getch();
closegraph();
return 0;
}
