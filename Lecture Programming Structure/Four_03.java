import java.util.Scanner;
class Four_03 {
  public static void main(String[] args) {
		// �� ������ �� ��ҵ��� �������� �����ϴ� �������� �����Ѵ�
		int attendScore;
		int assignmentScore;
		int quizScore;
		int midtermexamScore;
		int finalexamScore;
		// ������ �����ϴ� ������ �����Ѵ�
			// ���⿡ �ڵ带 �����ϼ���
    double totalScore;
		//������ �����ϴ� ������ �����Ѵ�
			//���⿡ �ڵ带 �����ϼ���
		String grade;
		// Ű����κ��� �Է��ϴ� �����͸� �б� ���� Scanner ��ü�� �����.
		Scanner scan = new Scanner(System.in);
		
		// ����ڷκ��� �� �� ����� ������ �� ���� �ϳ��� �Է��϶�� ��û�Ѵ�.
		// �׸��� �Էµ� ������ �д´�.
	  System.out.print("attendance score:");
		// ���⿡ �ڵ带 �����ϼ���
		attendScore = scan.nextInt();
		System.out.print("assignment score:");
		// ���⿡ �ڵ带 �����ϼ���
		assignmentScore = scan.nextInt();
		System.out.print("quiz score:");
		// ���⿡ �ڵ带 �����ϼ���
		quizScore = scan.nextInt();
		System.out.print("midterm exam score:");
		// ���⿡ �ڵ带 �����ϼ���
		midtermexamScore = scan.nextInt();
		System.out.print("final exam score:");
		// ���⿡ �ڵ带 �����ϼ���
		finalexamScore = scan.nextInt();
				
		// ������ ����Ѵ�
		totalScore = (attendScore * 10.0 + assignmentScore * 40.0 + quizScore * 10.0 + midtermexamScore * 20.0 + finalexamScore * 20.0)/100;
			// ���⿡ �ڵ带 �����ϼ���
		// ������ �����Ѵ�
			// ���⿡ �ڵ带 �����ϼ���
		if (totalScore >= 90.0) grade = "A";
		else if (totalScore >=80.0) grade = "B";
		else if (totalScore >=70.0) grade = "C";
		else if (totalScore >= 60.0) grade = "D";
		else grade = "F";
		// ������ ������ ����Ѵ�
		System.out.println("total score:" + totalScore);
		System.out.println("grade:" + grade);
  }
}