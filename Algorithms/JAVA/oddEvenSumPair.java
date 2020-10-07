// count of odd and even sum pairs in an array in O(n)

import java.util.*;
import java.lang.*;
import java.io.*;

class OddEvenSumPair
{
     static void findCount(int arr[])
    {
        int evencount=0;
        int oddcount=0;
        for(int i=0;i<arr.length;i++)
        {
            if(arr[i]%2==0)
                evencount++;
            else
                oddcount++;
        }
        int evenpairs=0;
        evenpairs += (evencount*(evencount-1))/2;
        evenpairs += (oddcount*(oddcount-1))/2;

        int oddpairs=0;
        oddpairs+=evencount*oddcount;

        System.out.println("odd pairs"+" "+oddpairs);
        System.out.println("even pairs"+" "+evenpairs);
    }

	public static void main (String[] args) throws java.lang.Exception
	{
        int a[] = { 1, 4, 45, 6, 10, 8, 2, 7, 9 };
        findCount(a);
    }
}