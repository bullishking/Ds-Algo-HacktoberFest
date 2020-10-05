// Special diamond pattern with following conditions
        // Single For Loop
        // Single if else if ladder
        // Only 3 variables in whole program
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i , num , row_controller;
    scanf("%d" , &num);

    row_controller = 1 - num;

    for(i = 1 ; row_controller < num ; i++)
{
        if(i < 1 + abs(row_controller))
            printf(" ");
        else if(i < 2 * num - (1 + abs(row_controller)))
            printf("*" , abs(row_controller) + 1);
        else
        {
            printf("*\n" , abs(row_controller) + 1);
            i = 0;
            row_controller += 1;
        }
    }
    return 0;
}