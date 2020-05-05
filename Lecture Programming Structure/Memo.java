
public class Memo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str = "Hello";
		String substr = str.substring(0,4);
		int len = str.length(); //길이는5
		int Firstchar = str.charAt(0); //첫번째 문자열의 모양
		int Index = str.indexOf(Firstchar); //첫번째문자열의 위치
		char c = str.charAt(Index);
		System.out.println(str);
		System.out.println(substr);

	}

}
