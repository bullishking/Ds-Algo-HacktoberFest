#include<conio.h>
#include<stdio.h>
#include<alloc.h>
struct node
{
 	int data;
struct node*next;
}
*start=NULL;
void create()
{
 char ch;
 do
 	{
  	struct node*new_node,*current;
  	new_node=(struct node*)malloc(sizeof(new_node));
printf("\n Enter the data:\t");
  		scanf("%d",&new_node->data);
  	new_node->next=NULL;
  		if(start==NULL)
  		{
   			start=new_node;
   			current=new_node;
  		}
  		else
  		{
   			current->next=new_node;
   			current=new_node;
  		}
  		printf("Do you want to add more nodes:\t");
  		ch=getch();
  	}
  	while(ch!='n');
}
void display()
{
 	struct node*new_node;
 	printf("\n\n Linked List:\t");
 	new_node=start;
 	while(new_node!=NULL)
 	{
 		printf("%d ",new_node->data);
 		new_node=new_node->next;
 	}
 	printf("NULL");
 	getch();
}
void main()
{
clrscr();
 	create();
 	display();
 	getch();
}
