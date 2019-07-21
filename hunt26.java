import java.util.*;
public class RevList
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		int num = in.nextInt();
		int arry[] = new int[num];
		for(int i=0 ; i<num ; i++)
			arry[i] = in.nextInt();
		reverse(arry,num);
	}
	public static void reverse(int arry[],int num)
	{
		for(int i=num-1 ; i>=0 ; i--)
		{
			if(i!=0)
				System.out.print(arry[i]+"->");
			else
				System.out.print(arry[i]);
		}
	}
}
