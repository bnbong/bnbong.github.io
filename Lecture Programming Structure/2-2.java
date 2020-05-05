//printing variable backward.

import java.util.Scanner; 

class Main2_2 {
  public static void main(String[] args) {
    String str = "";  // 입력받는 문자열 
    String outputStr = ""; //출력 문자열 
    Scanner scan = new Scanner(System.in);
    str = scan.next(); // 문자열 입력받기 
    // 여기에 코드를 입력하세요. 
    char a = str.charAt(0);
    char b = str.charAt(1);
    char c = str.charAt(2);
    
    outputStr = outputStr + c + b + a;
    
    System.out.println(outputStr);
    scan.close();
  }
}