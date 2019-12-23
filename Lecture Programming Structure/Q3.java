import java.util.*;
public class Q3 {	
	public static int getPayroll(String line) {
		if (line == null) return -1;
		try {
			StringTokenizer t = new StringTokenizer(line, "|");
			String s = t.nextToken().trim();
			int hours = new Integer(t.nextToken().trim()).intValue();
			int payrate = new Integer(t.nextToken().trim()).intValue();
			return hours * payrate;
		} catch(NoSuchElementException e) {
			return -2;
		} catch(NumberFormatException e) {
			return 0;
		}
	}
	public static void main(String[] args) {
		System.out.println(getPayroll("student|2|4")); // 8
		System.out.println(getPayroll(null)); // -1
		System.out.println(getPayroll("abcd")); // -2
		System.out.println(getPayroll("lee|a|b")); // 0
	}
}