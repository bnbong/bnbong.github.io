import java.util.Scanner;
class Four_02 {
  public static void main(String[] args) {
		int totalcreditearned; // �� �̼�����
		// ���� ������ �����ϴ� ������ �����Ѵ�
			//���⿡ �ڵ带 �����ϼ���
		int toeic_score;
		// Scanner ��ü�� �����ϰ� scan�� ����Ű�� �Ѵ�
		Scanner scan = new Scanner(System.in);
		
		System.out.print("total credit:");
			// ���⿡ �ڵ带 �����ϼ���
		totalcreditearned = scan.nextInt();
		System.out.print("TOEIC score:");
			// ���⿡ �ڵ带 �����ϼ���
		toeic_score = scan.nextInt();
		// �� �̼������� TOEIC ������ ���� ����/����/�����Ұ� ���θ� ����Ѵ�
			// ���⿡ �ڵ带 �����ϼ���
		if (totalcreditearned >= 140) {
		  if (toeic_score >= 700) System.out.println("graduation");
		  else System.out.println("completion");
		}
		else System.out.println("failure");
  }
}