// Importing the Libraries
#include<stdio.h>



int fact(int a)             // Function for calculating Factorial of agiven Number.
{                           // Takes a number as argument and returns the factorial of that number
    int p=1,i=1;
    for(i=1;i<=a;i++)
    {
        p=p*i;
    }
    return(p);
}



int main()                              // Main Function or Main Body
{
    int n,m,i,j,k;                      // Declaring the required variables
    printf("Enter the value of n : ");
    scanf("%d",&n);                     // Taking the value of the size or no. of rows of pascal Triangle
    for(i=0;i<n;i++)                    // Implimenting the main logic for printing pascal's triangle
    {
        for(j=1;j<=(n-i-1);j++)
        {
            printf(" ");
        }
        for(k=0;k<=i;k++)
        {
            m=fact(i)/(fact(i-k)*fact(k));  // Caling the function of factorial declared above the main program
            printf("%d ",m);
        }
        printf("\n");                       //Going to new line after each row is printed.
    }
    return 0;
}
