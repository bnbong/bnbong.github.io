import java.util.Scanner;
class Five_02 {
  public static void main(String[] args) {
    int grade;			    // �� �л��� ����
		int numStudents=0;	//�л����� ��
		int numPass=0;	  	// ��� �л����� ��
		int numFail = 0;	  // ���� �л����� ��

		Scanner scan = new Scanner (System.in);
		
		System.out.print("Enter the first score(negative to exit)");
		grade = scan.nextInt();
		
		// ������ ������ �ƴ� ���� ������ �ݺ��Ѵ�
		while(grade >=0) {
			
			// �л����� ���� 1��ŭ ������Ų��
			// ���⿡ �ڵ带 �����ϼ���
			numStudents += 1;
			// ������ 60�̻��̸� ��� �л����� ���� 1��ŭ ������Ű��
			// �ƴϸ� ���� �л����� ���� 1��ŭ ������Ų��
			// ���⿡ �ڵ带 �����ϼ���
			if (grade >= 60) {
			  numPass += 1;
			}
			else {
			  numFail += 1;
			}
			System.out.println("Enter the next score(negative to exit):");
			grade = scan.nextInt();
			// ���� ������ �о� ���δ�
			// ���⿡ �ڵ带 �����ϼ���
			
		}
		System.out.println("numStudents:" + numStudents);
		System.out.println("numPass:"+numPass);
		System.out.println("numFail:"+numFail);
		// ��� �л����� ���� ���� �л����� ���� ����Ѵ�
		// ���⿡ �ڵ带 �����ϼ���
  }
}