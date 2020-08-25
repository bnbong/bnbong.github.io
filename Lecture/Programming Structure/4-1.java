//calculating score

import java.util.Scanner;
class Main4_1 {
  public static void main(String[] args) {
  		double grade; // 평점
  		
  		// 토익 점수를 저장하는 변수를 선언한다
  			// 여기에 코드를 삽입하세요
  		int toeic_grade;
  		// Scanner 객체를 생성하고 scan이 가리키게 한다
  		Scanner scan = new Scanner(System.in);
  		
  		//평점을 입력 받는다
	    System.out.print("grade:");
  		grade = scan.nextDouble();
  		
  		// 토익 점수를 입력 받는다
  		System.out.print("TOEIC score:");
  			// 여기에 코드를 삽입 하세요
  		toeic_grade = scan.nextInt();
  		// 평점과 토익 점수에 따라 적절한 메시지를 출력한다
  		if (toeic_grade >= 700) {
  		  if (grade >= 4.0) System.out.println("A");
  		  else if (grade >= 3.5) System.out.println("B");
  		  else if (grade >= 3.0) System.out.println("C");
  		  else System.out.println("D");
  		} 
  		else System.out.println("D");
              // 여기에 코드를 삽입하세요
        scan.close();
  }
}