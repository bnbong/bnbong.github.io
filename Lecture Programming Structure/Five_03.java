import java.util.Scanner;
class Five_03 {
  public static void main(String[] args) {
  String sentence;
  System.out.print("Please enter a sentence:");
	Scanner scan = new Scanner(System.in);
  sentence = scan.nextLine();
  sentence = sentence.replaceAll(" ","");
  System.out.println(sentence.length());
  //���⿡ �ڵ带 �Է��ϼ���
  
  }
}