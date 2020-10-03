#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a[20], i, j, x, var, key;
    
    cout<<"Enter the no. of elements you want to enter: ";
    cin>>x;
    
    cout<<"\n Enter the elements: ";

    for(i=0; i<x; i++)
    {
        cin>>a[i];
    }
    
    cout<<"\n 1. Sort the elements in Ascending order ";
    cout<<"\n 2. Sort the elements in Descending order ";
    cout<<"\n Your Choice: ";
    cin>>key;
    
    if(key==1)
    {
        i=0;
         while(i<x)
        {
            for(j=i+1; j<x; j++)
            {
                if(a[i]>a[j])
                {
                	var=a[i];
                    a[i]=a[j];
                    a[j]=var;
                }
            }
            i++;
        }  
    }
    
    else if(key==2)
    {
        i=0;
	    while(i<x)
	    {
	   	    for(j=i+1; j<x; j++)
            {
	            if(a[i]<a[j])
	           	{
	                var=a[i];
	                a[i]=a[j];
	                a[j]=var;
	            }
	        }
	        i++;
	    }  
   	}
        
    else
    cout<<"\n Wrong value entered";
    
    cout<<"\n The sorted list of elements is: ";
    for(i=0; i<x; i++)
    {
        cout<<a[i]<<"\t";
    }
    
	return 0;
}




