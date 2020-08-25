
public class Q6_2018 {
	public static String getConcat(Object[] arr) {
		//fill here!
		String result = "";
		for(int i = 0; i < arr.length; i++) {
			if (arr[i] instanceof String) {
				result += (String) arr[i];
			}
		}
		return result;
	}

	class Q6_another {
		public static String getSum(Object[] arr) {
			int sum = 0;
			for(int i = 0; i < arr.length; i++) {
				if(arr[i] instanceof Integer) {
						sum += (int) arr[i];
				}
			}
			return sum;
		}
	}
	public static void main(String[] args) {
		Object[] a = new Object[5];
		a[0] = 10;
		a[1] = "a";
		a[2] = 1.0;
		a[3] = 2;
		a[4] = "b";
		System.out.println(getConcat(a)); //ab
	}
}
