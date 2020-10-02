#include<iostream>
#include<graphics.h>
#include<conio.h>
#include<stdio.h>

main()
{
      initwindow(800,800);
	  circle(400,400,100);
	  circle(400,250,50);
	  
	  circle(425,235,10);
	  circle(375,235,10);
	  circle(375,240,5);
	  circle(425,240,5);
	  
	  circle(400,280,12);
	  
	  circle(300,80,10);
	  circle(200,105,10);
	  circle(304,270,10);
	  circle(260,197,10);
	  circle(180,190,10);
	  circle(190,340,10);
	  circle(230,265,10);
	  circle(260,410,10);
	  circle(235,480,10);
	  circle(135,475,10);
	  
	  circle(380,20,10);
	  circle(470,40,10);
	  circle(590,95,10);
	  circle(520,155,10);
	  circle(497,262,10);
	  circle(582,209,10);
	  circle(622,309,10);
	  circle(592,429,10);
	  circle(503,470,10);
	  circle(645,478,10);
	
	  line(350,200,450,200);
	  line(350,200,400,100);
	  line(450,200,400,100);
	  line(400,250,404,258);
	  line(385,260,400,250);
	  line(385,260,404,258);
	  line(500,400,550,350);
	  line(525,500,550,350);
	  line(568,353,532,347);
	  line(568,353,572,329);
	  line(532,347,536,323);
	  line(572,329,536,323);
	  line(536,323,526,263);
	  line(572,329,597,272);
	  line(526,263,597,272);
	  line(50,500,750,500);
	  line(300,400,250,350);
	  line(245,345,250,350);
	  line(255,345,250,350);
	  line(245,355,250,350);
	  
	  
	
   	  setfillstyle(SOLID_FILL,WHITE);
	  floodfill(400,400,WHITE);
	  floodfill(401,250,WHITE);
	  
	 
	  
	  setfillstyle(SOLID_FILL,BLUE);
	  floodfill(400,150,WHITE);
	  
	  setfillstyle(SOLID_FILL,YELLOW);
	  floodfill(551,347,WHITE);
	  
	  setfillstyle(SOLID_FILL,BROWN);
	  floodfill(540,323,WHITE);
	  
	  
	   setfillstyle(SOLID_FILL,RED);
	  floodfill(400,285,WHITE);
	  
	   setfillstyle(SOLID_FILL,DARKGRAY);
	  floodfill(425,234,WHITE);
	  floodfill(375,234,WHITE);
	  
	  setfillstyle(SOLID_FILL,BLACK);
	  floodfill(375,240,WHITE);
	  floodfill(425,240,WHITE);
	  
	  setfillstyle(SOLID_FILL,WHITE);
	  floodfill(300,80,WHITE);
	  floodfill(200,105,WHITE);
	  floodfill(304,270,WHITE);
	  floodfill(260,197,WHITE);
	  floodfill(180,190,WHITE);
	  floodfill(190,340,WHITE);
	  floodfill(230,265,WHITE);
	  floodfill(260,410,WHITE);
	  floodfill(235,480,WHITE);
	  floodfill(135,475,WHITE);
	  
	  floodfill(645,478,WHITE);
	  floodfill(503,470,WHITE);
	  floodfill(592,429,WHITE);
	  floodfill(622,309,WHITE);
	  floodfill(582,209,WHITE);
	  floodfill(497,262,WHITE);
	  floodfill(520,155,WHITE);
	  floodfill(590,95,WHITE);
	  floodfill(470,40,WHITE);
	  floodfill(380,20,WHITE);
	  
	  
	getch();
	closegraph();
}
