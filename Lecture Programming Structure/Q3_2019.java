
public class Q3_2019 {
	public static int getCRT(int p1, int p2, int r1, int r2) {
		int result = -1;
		for (int i = 0; i < p1 * p2; i++) {
			if (i % p1 == r1 && i % p2 == r2) result = i;
		}
		return result;
	}
	public static void main(String[] args) {
		System.out.println(getCRT(5, 7, 3, 4)); // 18
	}
}
