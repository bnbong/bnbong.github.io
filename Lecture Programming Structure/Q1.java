import java.io.*; 
import javax.swing.*;

public class Q1 {
	public static void main(String[] args) throws IOException {
		BufferedReader infile = new BufferedReader(new FileReader("test"));
		while (infile.ready()) {
			System.out.println(infile.readLine());
		}
		infile.close();
	}
	
}