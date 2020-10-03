#include<iostream>
#include<conio.h>
using namespace std;

int main()
{
	system("cls");
	int n,sp,st=1;
	cout<<"Enter The Number Of Lines= ";
	cin>>n;
	cout<<"\nThe Output:-\n"<<endl;
	sp=n-1;
	for(int i=1;i<=n;i++)
	{
		for(int j=sp;j>0;j--)
			cout<<" ";
		for(int k=1;k<=st;k++)
			cout<<"*";
		st=st+2;
		sp--;
		cout<<endl;
	}
	getch();
}
