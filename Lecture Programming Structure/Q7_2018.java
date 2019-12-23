
public class Q7_2018 {
	public static boolean isPrime(int n) {
		//modify this function
		boolean answer = true;
		boolean item_found = false;
		if(2 > n || 1000000 < n) {
			throw new RuntimeException();
		}
		int current = n / 2;
		while(!item_found && current > 1) {
			if(n % current == 0) item_found = true;
			else current = current - 1;
		}
		if(item_found) answer = false;
		return answer;
	}
	public static void main(String[] args) {
		System.out.println(isPrime(11)); //true
		System.out.println(isPrime(1000001)); //RuntimeException
		System.out.println(isPrime(1)); //RuntimeEx
	}
}
