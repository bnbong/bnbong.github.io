import java.text.*;

public class CelsiusToFahrenheit1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int c = new Integer(args[0]).intValue();
		double f = ((9.0/5.0) * c) + 32;
		System.out.println("For Celsius degrees " + c + ",");
		DecimalFormat formatter = new DecimalFormat("0.0");
		System.out.println("Degrees Fahrenheit " + formatter.format(f));

	}

}
