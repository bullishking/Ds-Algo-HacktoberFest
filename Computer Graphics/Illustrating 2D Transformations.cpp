#include<iostream> 
#include<math.h>
#include<stdio.h> 
#include<graphics.h>
using namespace std; 
void Translation (int P[][2], int T[]) 
{ 
 	initwindow(800,800);
    setcolor (2); 
    rectangle (P[0][0], P[0][1], P[1][0], P[1][1]); 
    P[0][0] = P[0][0] + T[0]; 
    P[0][1] = P[0][1] + T[1]; 
    P[1][0] = P[1][0] + T[0]; 
    P[1][1] = P[1][1] + T[1]; 
	setcolor (3);
    rectangle (P[0][0], P[0][1], P[1][0], P[1][1]);
	getch();  
} 

void NewCoordinate(int S[][2], int New[][1]) 
{ 
    int temp[2][1] = { 0 }; 
    for (int i = 0; i < 2; i++) 
        for (int j = 0; j < 1; j++) 
            for (int k = 0; k < 2; k++) 
                temp[i][j] += (S[i][k] * New[k][j]); 
    New[0][0] = temp[0][0]; 
    New[1][0] = temp[1][0]; 
} 
   
void Scaling(int P[2][2], int Sx, int Sy) 
{ 
	initwindow(800,800);
   	setcolor (14);  
    rectangle (P[0][0], P[0][1], P[1][0], P[1][1]);
    int S[2][2] = { Sx, 0, 0, Sy }; 
    int New[2][1];   
    for (int i=0; i<2; i++) 
    { 
    	for (int j=0; j<2; j++)
    	{
	        New[0][0] = P[i][j]; 
	        New[1][0] = P[i][j]; 
	  
	        NewCoordinate(S, New); 
	  
	        P[i][j]= New[0][0]; 
	        P[i][j]= New[1][0];
		}
    }  
    setcolor (2);  
    rectangle (P[0][0], P[0][1], P[1][0], P[1][1]); 
	getch();
 } 
 
void Rotation(int x1, int y1, int x2, int y2, int x3, int y3, int angle) 
{ 
	initwindow(800,800);
    float t = 3.14*angle/180;
    	setcolor (5);
		line(x1,y1,x2,y2);
        line(x2,y2,x3,y3);
        line(x3,y3,x1,y1);        
        x1=abs(x1*cos(t)-y1*sin(t));
        y1=abs(x1*sin(t)+y1*cos(t));
        x2=abs(x2*cos(t)-y2*sin(t));
        y2=abs(x2*sin(t)+y2*cos(t));
		x3=abs(x3*cos(t)-y3*sin(t));
    	y3=abs(x3*sin(t)+y3*cos(t));    	
    	setcolor (5);
		line(x1,y1,x2,y2);
        line(x2,y2,x3,y3);
        line(x3,y3,x1,y1);
        getch();
} 

int main() 
{ 
   
	int P[2][2] = {100, 100, 200, 200};
	int Sx = 2, Sy = 2;
	int size = 2, angle;
	int key, i, j;
    do
   {
       cout<<"\n Enter your choice :";
       cout<<"\n 1.Translation";
       cout<<"\n 2.Scaling";
       cout<<"\n 3.Rotation";
       cout<<"\n 4.Exit";
       cout<<"\n Ans:";
       cin>>key;
       if(key==1)
       {
          int T[] = {200, 100}; 
    		Translation (P, T);  
       }
       else if(key==2)
       {
       	 Scaling(P, Sx,Sy);
       }
       else if(key==3)
       {
       		int x1,y1,x2,y2,x3,y3;
			cout<<"\nEnter the vertices of Triangle: ";
			cin>>x1>>y1>>x2>>y2>>x3>>y3;
          	cout<<"\nEnter the angle of rotation in Degree: ";
			cin>>angle;	                                 
		    Rotation(x1,y1,x2,y2,x3,y3,angle);
       }
   }while (key!=4); 
    getch(); 
    return 0; 
}
