
import java.util.Scanner; 
public class Q1_2019 {
	public static void main(String[] args) {
		String name;
		int number;
		int numsq;
		
		Scanner scan = new Scanner(System.in);
		System.out.print("Your name: ");
		name = scan.next(); 
		System.out.print("Your favorite number: ");
		number = scan.nextInt();
		numsq = number * number; 
		System.out.println(name + ", the square of your favorite number = " + numsq);
	}
}
