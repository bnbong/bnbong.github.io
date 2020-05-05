/*
class TranslateTable {
	private int[] encode; // �ڵ� -> ��ȣȭ�� �ڵ� (encode[0]: 0�� ��ȣȭ�� �ڵ尪) 
	private int[] decode; // ��ȣȭ�� �ڵ� -> �ڵ�  
	public TranslateTable(int seed) {
		encode = new int[10];
		decode = new int[10];
		// fill here!
		encode[0] = seed;
		decode[seed] = 0;
		for(int i=1; i<9; i++) {
			 int new_code = (encode[i-1]+3) % 10;
			 encode[i] = new_code;
			 decode[new_code] = i;
		}
	}
	private int c2i(char c) {
		// fill here!
		if(c==' ') return 0;
		if('0'<=c && c<='9') return c-'0';
		throw new RuntimeException("c2i: invalid character " + c);
	}
	private char i2c(int i) {
		// fill here!
		if(0<=i && i<=9) return (char)('0'+i);
		throw new RuntimeException("i2c: invalid code " + i);
		
	}
	private char encode(char c) { return i2c(encode[c2i(c)]); }
	private char decode(char c) { return i2c(decode[c2i(c)]); }
	public String encode(String s) {
		// fill here!
		String answer1 = "";
		for(int i = 0; i < s.length(); i++) {
			answer1 = answer1 + encode(s.charAt(i));
		}
		return answer1;
	}
	public String decode(String s) {
		// fill here!
		String answer2 = "";
		for(int i = 0; i < s.length(); i++) {
			answer2 = answer2 + decode(s.charAt(i));
		}
		return answer2;
	}
}

public class Q4 {
	public static void main(String[] args) {
		TranslateTable m = new TranslateTable(1);
		String original = "0123456789";
		String encoded = m.encode(original);
		String decoded = m.decode(encoded);
		System.out.println("original: " + original); // original: 0123456789
		System.out.println("encoded: " + encoded); // encoded: 1470369258
		System.out.println("decoded: " + decoded); // decoded: 0123456789
	}
}
*/
class TranslateTable {
	private int[] encode; // 코드 -> 암호화된 코드 (encode[0]: 0의 암호화된 코드값) 
	private int[] decode; // 암호화된 코드 -> 코드  
	public TranslateTable(int seed) {
		// fill here!
		encode = new int[10];
		decode = new int[10];
		encode[0] = seed; 
		decode[seed] = 0; 
		for (int i = 1; i < encode.length; i++) {
			int code = (encode[i-1] + 3) % encode.length;
			encode[i] = code; 
			decode[code] = i;
		}
	}
	private int c2i(char c) {
		// fill here!
		return c - '0';
	}
	private char i2c(int i) {
		// fill here!
		return (char)(i + '0');
	}
	private char encode(char c) {
		return i2c(encode[c2i(c)]);
	}
	private char decode(char c) {
		return i2c(decode[c2i(c)]);
	}
	public String encode(String s) {
		String result = ""; 
		for (int i = 0; i < s.length(); i++) {
			result = result + encode(s.charAt(i));
		}
		return result; 
	}
	public String decode(String s) {
		String result = ""; 
		for (int i = 0; i < s.length(); i++) {
			result = result + decode(s.charAt(i));
		}
		return result; 
	}
}

public class Q4 {
	public static void main(String[] args) {
		TranslateTable m = new TranslateTable(1);
		String original = "0123456789";
		String encoded = m.encode(original);
		String decoded = m.decode(encoded);
		System.out.println("original: " + original); // original: 0123456789
		System.out.println("encoded: " + encoded); // encoded: 1470369258
		System.out.println("decoded: " + decoded); // decoded: 0123456789
	}
}