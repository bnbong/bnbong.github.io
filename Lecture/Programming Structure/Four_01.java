import java.util.Scanner;
class Four_01 {
  public static void main(String[] args) {
  		double grade; // ����
  		
  		// ���� ������ �����ϴ� ������ �����Ѵ�
  			// ���⿡ �ڵ带 �����ϼ���
  		int toeic_grade;
  		// Scanner ��ü�� �����ϰ� scan�� ����Ű�� �Ѵ�
  		Scanner scan = new Scanner(System.in);
  		
  		//������ �Է� �޴´�
	    System.out.print("grade:");
  		grade = scan.nextDouble();
  		
  		// ���� ������ �Է� �޴´�
  		System.out.print("TOEIC score:");
  			// ���⿡ �ڵ带 ���� �ϼ���
  		toeic_grade = scan.nextInt();
  		// ������ ���� ������ ���� ������ �޽����� ����Ѵ�
  		if (toeic_grade >= 700) {
  		  if (grade >= 4.0) System.out.println("A");
  		  else if (grade >= 3.5) System.out.println("B");
  		  else if (grade >= 3.0) System.out.println("C");
  		  else System.out.println("D");
  		} 
  		else System.out.println("D");
  			// ���⿡ �ڵ带 �����ϼ���
  }
}