import java.util.Scanner;
class Five_05 {
  public static void main(String[] args) {
		int n;

		System.out.print("Please enter an integer:");
		Scanner scan = new Scanner(System.in);
		n = scan.nextInt();
		int i,j;
		for (i=1; i<=n; i++) {
		  for (j=1; j<=n; j++) {
		    if (i != j) {
		      if (i % j == 0) System.out.println("("+i+","+j+")");
		    }
		  }
		}
		
		// 여기에 코드를 입력하세요
		
  }
}