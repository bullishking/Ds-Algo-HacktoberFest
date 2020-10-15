import java.awt.List;
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;

public class Solution {
    static class QueueObj{
        int pos;
        int step;
        QueueObj(int pos,int step)
        {
            this.pos=pos;
            this.step=step;
        }
    }
    static int minStep(int board[])
    {
        Queue<QueueObj> q=new LinkedList<>();
        boolean visited[]=new boolean[100];
        q.add(new QueueObj(0,0));
        visited[0]=true;
        while(!q.isEmpty())
        {
            QueueObj temp=q.poll();
            visited[temp.pos]=true;
            if(temp.pos==99)
                return temp.step;
            if(board[temp.pos]!=0)
            {
                q.add(new QueueObj(board[temp.pos],temp.step));
                visited[board[temp.pos]]=true;
            }
            else
            {
                for (int i=1;i<=6;i++)
                {
                    if(temp.pos+i<=99&&!visited[temp.pos+i])
                    {
                        q.add(new QueueObj(temp.pos+i,temp.step+1));
                        visited[temp.pos+i]=true;
                    }
                }
            }
        }
        return -1;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder output=new StringBuilder();
        String s[]=br.readLine().trim().split(" ");
        int t=Integer.parseInt(s[0]);
        while (t-->0)
        {
            int board[]=new int[100];
            s=br.readLine().trim().split(" ");
            int n=Integer.parseInt(s[0]);
            while (n-->0)
            {
                s=br.readLine().trim().split(" ");
                int l1=Integer.parseInt(s[0])-1;
                int l2=Integer.parseInt(s[1])-1;
                board[l1]=l2;
            }
            s=br.readLine().trim().split(" ");
            int m=Integer.parseInt(s[0]);
            while (m-->0)
            {
                s=br.readLine().trim().split(" ");
                int s1=Integer.parseInt(s[0])-1;
                int s2=Integer.parseInt(s[1])-1;
                board[s1]=s2;
            }
            output.append(minStep(board)+"\n");
        }
        System.out.println(output);
    }
}
