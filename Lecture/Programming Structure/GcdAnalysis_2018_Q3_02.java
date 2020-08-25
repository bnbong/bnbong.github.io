public class GcdAnalysis_2018_Q3_02 {
	private static int minus_cnt = 0;
	private static int mod_cnt = 0;
	public static int findGCD_minus(int n, int m) {
		minus_cnt++;
		if (n < m) {int tmp = n; n = m; m = tmp;}
		if (m == n) return m; 
		return findGCD_minus(n - m, m); 
	}
	public static int findGCD_mod(int n, int m) {
		mod_cnt++;
		if (n < m) {int tmp = n; n = m; m = tmp;}
		if (m == 0) return n; 
		return findGCD_mod(m, n % m); 
	}
	
	public static int gcd_analysis(int n, int m) {
		findGCD_minus(n, m);
		findGCD_mod(n, m);
		return minus_cnt - mod_cnt;
	}
	
	public static void main (String args[]) {
		System.out.println(gcd_analysis(1024, 82));
	}
}
