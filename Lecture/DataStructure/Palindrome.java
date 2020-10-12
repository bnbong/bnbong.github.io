package cse2010.homework4;

/*
 * CSE2010 Homework #4
 * Problem 1: Palindrome
 *
 * Complete the code below.
 *
 */

public class Palindrome {

    public static boolean isPalindrome(String target) {

        return isPalindrome(target, 0, target.length() - 1);
    }

    private static boolean isPalindrome(String as, int start, int end) {

        // your code goes here ...

        if(as.isEmpty() == true) return true;
        if(as.length() == 1 && isAlpha(as.charAt(start)) == false) return true;

        while(start < as.length() && end > 0){
            if(as.charAt(start) == ' ') {
                start++;
                if(start == as.length()) return true;
                continue;
            }
            if(as.charAt(end) == ' ') {
                end--;
                if(end == 0) return true;
                continue;
            }

            if(isAlpha(as.charAt(start)) == false) {
                start++;
                if(start == as.length()) return true;
                continue;
            }
            if(isAlpha(as.charAt(end)) == false) {
                end--;
                if(end == 0) return true;
                continue;
            }

            if(toLower(as.charAt(start)) != toLower(as.charAt(end))) break;

            else{
                start++;
                end--;
                if(start > end || start == as.length()-1 || end == 0) return true;
            }
        }

        return false;
    }

    private static boolean isAlpha(final char ch) {
        if (ch >= 'a' && ch <= 'z' || ch >= 'A' && ch <= 'Z')
            return true;
        else
            return false;
    }

    private static int toLower(char c) {
        if ((c >= 'A') && (c <= 'Z'))
            return c + ('a' - 'A');
        return c;
    }

}
