
public class Memo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str = "Hello";
		String substr = str.substring(0,4);
		int len = str.length(); //���̴�5
		int Firstchar = str.charAt(0); //ù��° ���ڿ��� ���
		int Index = str.indexOf(Firstchar); //ù��°���ڿ��� ��ġ
		char c = str.charAt(Index);
		System.out.println(str);
		System.out.println(substr);

	}

}
