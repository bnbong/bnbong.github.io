//using classes

//이 클래스는 교과목을 나타낸다.
public class Course {
	// 교과목에 대한 객체 변수들을 선언한다
	protected String courseName;
	protected int attendScore;

	// 교과목의 이름을 주어진 값으로 초기화하면서 Course 객체를 생성한다.
	public Course(String courseName) {
		// 여기에 코드를 입력하세요
		setCourseName(courseName);
		setattendScore(attendScore);
	}
	// 교과목의 이름을 반환한다
	public String getCourseName() {
		return courseName;
	}

	// 교과목의 출석 점수를 반환한다
	public int getattendScore() {
		// 여기에 코드를 입력하세요
		return attendScore;
	}
	
	// 교과목의 학점인  I를 반환한다
	public String getGrade() {
		// 여기에 코드를 입력하세요
		return "I";
	}

	// 교과목의 이름과 출석 점수를 반환한다
	public String toString(){
		// 여기에 코드를 입력하세요
		return ("교과목 이름: " + courseName + ", 출석점수: " + attendScore);
	}
	// 교과목의 이름을 변경한다
	public void setCourseName(String newCourseName) {
		// 여기에 코드를 입력하세요
		courseName = newCourseName;
	}
	// 교과목의 출석 점수를 변경한다
	public void setattendScore(int newattendScore) {
		// 여기에 코드를 입력하세요
		this.attendScore = newattendScore;
	}

}
public class LetterGradeCourse extends Course {
	int assignScore; // 과제 점수
	int examScore; // 시험 점수

	// 문자 학점 교과목의 변수들 값을 주어진 값들로 초기화한다
	public LetterGradeCourse(String cname) {
		// 여기 에 코드를 입력하세요
		super(cname);
		

	}

	// 교과목의 과제 점수를 반환한다
	public int getAssignScore() {
		// 여기에 코드를 입력하세요
		return assignScore;
	}
	
	// 교과목의 시험 점수를 반환한다
	public int getExamScore() {
		// 여기에 코드를 입력하세요
		return examScore;
	}
	
	//교과목의 총점을 계산하여 반환한다
	public double getTotal() {
		// 여기에 코드를 입력하세요
		return (super.getattendScore() * 2.0 + assignScore * 3.0 + examScore * 5.0) / 10.0;
	}
	// 교과목의 학점을 반환한다
	public String getGrade() {
		// 여기에 코드를 입 력 하세요
		String grade;
		if (this.getTotal() >= 90.0) grade = "A";
		else if (this.getTotal() >= 80.0) grade = "B";
		else if (this.getTotal() >= 70.0) grade = "C";
		else if (this.getTotal() >= 60.0) grade = "D";
		else grade = "F";
		return grade;
	}
	
	// 교과목의 이름, 출석 점수, 과제 점수와 시험 점수를 반환한다.
	public String toString(){
		// 여기에 코드를 입력하세요
		return (super.toString() + ", 과제 점수: " + assignScore + ", 시험 점수:" + examScore);
	}

	// 교과목의 과제 점수를 변경한다
	public void setAssignScore(int newAssignScore) {
		// 여기에 코드를 입력하세요
		this.assignScore = newAssignScore;

	}
	// 교과목의 시힘 점수를 변경한다
	public void setExamScore(int newexamScore) {
		// 여기에 코드를 입력하세요
		this.examScore = newexamScore;
	}

}
public class LetterGradeCourse extends Course {
	int assignScore; // 과제 점수
	int examScore; // 시험 점수

	// 문자 학점 교과목의 변수들 값을 주어진 값들로 초기화한다
	public LetterGradeCourse(String cname) {
		// 여기 에 코드를 입력하세요
		super(cname);
		

	}

	// 교과목의 과제 점수를 반환한다
	public int getAssignScore() {
		// 여기에 코드를 입력하세요
		return assignScore;
	}
	
	// 교과목의 시험 점수를 반환한다
	public int getExamScore() {
		// 여기에 코드를 입력하세요
		return examScore;
	}
	
	//교과목의 총점을 계산하여 반환한다
	public double getTotal() {
		// 여기에 코드를 입력하세요
		return (super.getattendScore() * 2.0 + assignScore * 3.0 + examScore * 5.0) / 10.0;
	}
	// 교과목의 학점을 반환한다
	public String getGrade() {
		// 여기에 코드를 입 력 하세요
		String grade;
		if (this.getTotal() >= 90.0) grade = "A";
		else if (this.getTotal() >= 80.0) grade = "B";
		else if (this.getTotal() >= 70.0) grade = "C";
		else if (this.getTotal() >= 60.0) grade = "D";
		else grade = "F";
		return grade;
	}
	
	// 교과목의 이름, 출석 점수, 과제 점수와 시험 점수를 반환한다.
	public String toString(){
		// 여기에 코드를 입력하세요
		return (super.toString() + ", 과제 점수: " + assignScore + ", 시험 점수:" + examScore);
	}

	// 교과목의 과제 점수를 변경한다
	public void setAssignScore(int newAssignScore) {
		// 여기에 코드를 입력하세요
		this.assignScore = newAssignScore;

	}
	// 교과목의 시힘 점수를 변경한다
	public void setExamScore(int newexamScore) {
		// 여기에 코드를 입력하세요
		this.examScore = newexamScore;
	}

}
class Main7_2 {
    public static void main(String[] args) {
          LetterGradeCourse courseOne;
          PassFailCourse courseTwo;
          String grade;
          
          courseOne = new LetterGradeCourse("Data structure");
          System.out.println(courseOne.toString());
          //교과목 이름: Data structure, 출석점수: 0, 과제 점수: 0, 시험 점수:0
          
          courseOne.setattendScore(95);
          courseOne.setAssignScore(98);
          courseOne.setExamScore(83);
          
          System.out.println(courseOne.toString());
          //교과목 이름: Data structur, 출석점수: 95, 과제 점수: 98, 시험 점수:83
          System.out.println(courseOne.getGrade());
        //B
        
          courseTwo = new PassFailCourse("Culture Seminar");
          System.out.println(courseTwo.toString());
          
          //교과목 이름: Culture Seminar, 출석점수: 0, 보고서 점수: 0, 발표 점수:0
          
          courseTwo.setattendScore(85);
          courseTwo.setReportScore(92);
          courseTwo.setPtScore(78);
          System.out.println(courseTwo.toString());
          //교과목 이름: Culture Seminar, 출석점수: 85, 보고서 점수: 92, 발표 점수:78
          System.out.println(courseTwo.getGrade());
          //CR
    }
  }