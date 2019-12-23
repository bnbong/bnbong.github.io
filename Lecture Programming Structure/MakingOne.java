
public class MakingOne {
	public static int getMinimal(int x) {
		int m1 = 9999, m2 = 9999, m3 = 9999;
		if (x == 1) return 0;
		if (x % 3 == 0) {
			m1 = 1 + getMinimal(x / 3);
		}
		if (x % 2 == 0) {
			m2 = 1+ getMinimal(x / 2);
		}
		m3 = 1 + getMinimal(x-1);
		return Math.min(Math.min(m1, m2),m3);
	}
	public static void main(String args[]) {
		System.out.println(getMinimal(2));
		System.out.println(getMinimal(10));
	}
}
