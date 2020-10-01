// Given a number x , we need to find pair in array having the sum as x in O(n)

import java.util.*;
import java.lang.*;
import java.io.*;

class FindPairWithGivenSum
{
     static void findPair(int arr[], int x)
    {
        HashSet<Integer> s = new HashSet<Integer>();
        for (int i = 0; i < arr.length; ++i) {
            int temp = x - arr[i];
 
             if (s.contains(temp)) {
                System.out.println(
                    "Pair with given sum "
                    + x + " is (" + arr[i]
                    + ", " + temp + ")");
            }
            s.add(arr[i]);
        }
    }

	public static void main (String[] args) throws java.lang.Exception
	{
        int a[] = { 1, 4, 45, 6, 10, 8, 2, 7, 9 };
        int x = 16;
        findPair(a,x);
    }
}