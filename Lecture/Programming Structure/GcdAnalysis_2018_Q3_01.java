public class GcdAnalysis_2018_Q3_01 {
	public static int findGCD_minus(int n, int m) {
		if (n < m) {int tmp = n; n = m; m = tmp;}
		if (m == n) return 1; 
		return 1 + findGCD_minus(n - m, m); 
	}
	public static int findGCD_mod(int n, int m) {
		if (n < m) {int tmp = n; n = m; m = tmp;}
		if (m == 0) return 1; 
		return 1 + findGCD_mod(m, n % m); 
	}
	
	public static int gcd_analysis(int n, int m) {
		return findGCD_minus(n,m)  - findGCD_mod(n, m);
	}
	
	public static void main (String args[]) {
		System.out.println(gcd_analysis(1024, 82));
	}
}
