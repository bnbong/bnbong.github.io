public class PossibleExprs_2018_Q4 {
	public static int getPossible(int n) {
		int result = 0;
		if (n == 0) return 1;
		if (n >= 1) result += getPossible(n - 1);
		if (n >= 2) result += getPossible(n - 2);
		if (n >= 3) result += getPossible(n - 3);
		return result;
	}
	public static void main(String args[]) {
		System.out.println(getPossible(17));
		System.out.println(getPossible(10));
		System.out.println(getPossible(20));
		System.out.println(getPossible(30));
	}
}