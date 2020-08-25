class Complex {
	private double real;
	private double imaginary; 
	
	public Complex(double a, double b) {
		this.real = a;
		this.imaginary = b;
	}
	public Complex add(Complex other) {
		double new_real; // 결과로 반환할 객체의 실수부 
		double new_imaginary; // 결과로 반환할 객체의 허수부
		// fill here! 
		new_real = this.real + other.real;
		new_imaginary = this.imaginary + other.imaginary;
		Complex result = new Complex(new_real, new_imaginary);
		return result; 
	}
	public Complex sub(Complex other) {
		// fill here!
		double new_real;
		double new_imaginary;
		new_real = this.real - other.real;
		new_imaginary = this.imaginary - other.imaginary;
		Complex result = new Complex(new_real, new_imaginary);
		return result;
	}
	public Complex mul(Complex other) {
		double new_real;
		double new_imaginary;
		new_real = (this.real * other.real) - (this.imaginary * other.imaginary);
		new_imaginary = (this.real * other.imaginary) + (this.imaginary * other.real);
		Complex result = new Complex(new_real, new_imaginary);
		return result;
	}
	public double getReal() {
		return real;
	}
	public double getImaginary() {
		return imaginary;
	}
}

public class Q2_2019 {
	public static void main(String[] args) {
		// test code 
		Complex c1 = new Complex(3, -1);
		Complex c2 = new Complex(-5, 2);
		Complex c1_add_c2 = c1.add(c2);
		Complex c1_sub_c2 = c1.sub(c2);
		Complex c1_mul_c2 = c1.mul(c2);
		System.out.println("c1 + c2 = " + c1_add_c2.getReal() + " + " + c1_add_c2.getImaginary() + "i"); // c1 + c2 = -2.0 + 1.0i 
		System.out.println("c1 - c2 = " + c1_sub_c2.getReal() + " + " + c1_sub_c2.getImaginary() + "i"); // c1 - c2 = 8.0 + -3.0i
		System.out.println("c1 * c2 = " + c1_mul_c2.getReal() + " + " + c1_mul_c2.getImaginary() + "i"); // c1 * c2 = -13.0 + 11.0i
	}
}
