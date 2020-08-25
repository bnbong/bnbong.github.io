//using scanner and loop

import java.util.Scanner;
class Main5_4 {
  public static void main(String[] args) {
		System.out.print("Please enter a sentence:");
		int a=0;
		int e=0;
		int i=0;
		int o=0;
		int u=0;
		int consonant=0;
		Scanner scan = new Scanner(System.in);
		String sentence = scan.nextLine();
		sentence = sentence.replaceAll(" ","");
		sentence = sentence.toLowerCase();
		// 공백 제거
		// 소문자 변환
		int j;
    for (j=0; j <= sentence.length()-1; j++) {
      if (sentence.charAt(j) == 'a') a++;
      else if (sentence.charAt(j) == 'e') e++;
      else if (sentence.charAt(j) == 'i') i++;
      else if (sentence.charAt(j) == 'o') o++;
      else if (sentence.charAt(j) == 'u') u++;
      else consonant++;
    }

		// 여기에 코드를 입력 하세요
		
		
		System.out.println("a:"+a);
		System.out.println("e:"+e);
		System.out.println("i:"+i);
		System.out.println("o:"+o);
		System.out.println("u:"+u);
        System.out.println("consonant:"+consonant);
        scan.close();
  }
}