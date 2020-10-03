#include<iostream>
#include<conio.h>
using namespace std;

int main()
{
	system("cls");
	int n;
	cout<<"Enter The Number Of Lines= ";
	cin>>n;
	cout<<"\nThe Output:-\n"<<endl;
	for(int i=1;i<=n;i++)
	{
		for(int j=1;j<=i;j++)
			cout<<"*";
		cout<<endl;
	}
	getch();
}
