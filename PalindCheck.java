package semester2; // change package name as per your file


import java.util.Scanner;

public class PalindCheck {
//This code removes numbers,symbols and characters from the given string. Later it checks, if the given string is palindrome or not.

	public static void main (String[] args)
	{
		int ans,i = 0;
		String dummy="";
		Scanner input = new Scanner(System.in);
		System.out.print("Enter the word to check for palindrome: ");
		String word = input.nextLine();
		word=word.toLowerCase(); // changing to lowercase to avoid case sensitivity problems while comparing
		while(i<word.length())
		{
			if(((int)word.charAt(i) >= 97) && ((int)word.charAt(i) <= 122)) // filters only aphabet letters
					dummy =dummy+word.charAt(i);
			i++;
		}
		//System.out.println("given: "+word+"\t\tfiltered: "+dummy);
		ans = isPalindrome(dummy);
		if(ans==5)
			System.out.println("It is Palindrome, TRUE");
		else
			System.out.println("It isn't Palindrome, FALSE");	
	}
	
	public static int isPalindrome(String word) { // user-defined method to check if it's palindrome or not
		
		int res=-1;
		String temp="";
		word=word.toLowerCase();
		int i = word.length()-1;
		int wCount;
		while(i >= 0)
		{
			wCount = (int)word.charAt(i);
			if(( wCount >= 97) && ( wCount <= 122)) // This reverses the given string and stores it in a temp variable.
				temp=temp+word.charAt(i);
			i--;
		}
		if(temp.equals(word)) // compares if the given filtered string an the reversed string matches
			res = 5;
		else
			res = -1;
		
		return res; // returns the result to the calling method
	}
}