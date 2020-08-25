//using scanner

import java.util.Scanner;
class Main5_3 {
  public static void main(String[] args) {
  String sentence;
  System.out.print("Please enter a sentence:");
	Scanner scan = new Scanner(System.in);
  sentence = scan.nextLine();
  sentence = sentence.replaceAll(" ","");
  System.out.println(sentence.length());
  scan.close();
  
  }
}