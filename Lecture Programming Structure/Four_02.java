import java.util.Scanner;
class Four_02 {
  public static void main(String[] args) {
		int totalcreditearned; // 총 이수학점
		// 토익 점수를 저장하는 변수를 선언한다
			//여기에 코드를 삽입하세요
		int toeic_score;
		// Scanner 객체를 생성하고 scan이 가리키게 한다
		Scanner scan = new Scanner(System.in);
		
		System.out.print("total credit:");
			// 여기에 코드를 삽입하세요
		totalcreditearned = scan.nextInt();
		System.out.print("TOEIC score:");
			// 여기에 코드를 삽입하세요
		toeic_score = scan.nextInt();
		// 총 이수학점과 TOEIC 점수에 따라 졸업/수료/졸업불가 여부를 출력한다
			// 여기에 코드를 삽입하세요
		if (totalcreditearned >= 140) {
		  if (toeic_score >= 700) System.out.println("graduation");
		  else System.out.println("completion");
		}
		else System.out.println("failure");
  }
}