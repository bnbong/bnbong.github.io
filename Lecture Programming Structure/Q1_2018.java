
public class Q1_2018 {
	public static String reverse(String s) {
		String result = "";
		
		for(int i = s.length() - 1; i >= 0; i--) {
			result = result + s.charAt(i);
		}
		return result;
	}
	
	public static void main(String[] args) {
		System.out.println(reverse("abcd"));
	}
}
