
public class Q4_2018 {
	public static int[] computeFrequency(String s) {
		int[] freq = new int[25];
		for(int i = 0; i < s.length(); i++) {
			char c = s.toLowerCase().charAt(i);
			int index = c - 'a';
			if(0 <= index && index <= 24) {
				freq[index]++;
			}
		}
		return freq;
	}
	class Q4answer {

		  public static int divide(String s) {

			 try {

			  int i = new Integer(s).intValue();

			  return (12 / i);

			 }

			 catch(NumberFormatException e) { // NumberFormatException

				 return -1;

			 }

			 catch(ArithmeticException e) { // ArithmeticException

				 return -2;

			 }

		  }

		}
	public static void main(String[] args) {
		int[] result = computeFrequency("ABCDss123");
		for (int i = 0; i < 25; i++)
            System.out.print(result[i] + " ");
		// should print ¡°1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0¡± 
	}

}
