import java.util.Vector;

public class Q2_2018 {
	public static int getSum(Vector<Integer> v) {
		int sum = 0;
		for(int i = 0; i < v.size(); i++) {
			int n = v.elementAt(i);
			sum += n;
		}
		return sum;
	}
	public static void main(String[] args) {
		Vector<Integer> v = new Vector<Integer>();
		v.add(5); v.add(4); v.add(-1); v.add(2, 100);
		System.out.println(getSum(v)); //should print 108
	}
}
