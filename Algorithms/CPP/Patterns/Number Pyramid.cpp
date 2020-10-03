#include<iostream>
#include<conio.h>
using namespace std;

int main()
{
	int i, j, k, x, y;
	
	cout<<"Enter the height of Pyramid: ";
	cin>>y;
	cout<<endl;
	x=2*y+1;
	for(int i=0;i<y;i++)
	{
		k=1;
		for(int j=0;j<y-1-i;j++)
		{
			cout<<"   ";
		}
		for(int j=y-1-i;j<y+i;j++)
		{
			if(k<10)
			cout<<" "<<k<<" ";
			else
			cout<<" "<<k;
				
			if(j<y-1)
			k++;
			else
			k--;
		}
		for(int j=y+i;j<x;j++)
		{
			cout<<"   ";
		}
		cout<<endl;
	}
	getch();
}
