//using classes 

public class Student {
	private String name; // 이름
	private int number; // 학번
	//이름을 기본 값으로 초기화하면서 Student 객체를 생성한다
	public Student() {
    //여기에 코드를 입력하세요
    name = "";
    number= 0;
	}
	//이름을 매개번수 값으로 초기화하면서 Student 객체를 생성한다
	public Student(String Name, int Number) {
    //여기에 코드를 입력하세요
    setName(Name);
    setNumber(Number);
	}

	// 이름을 반환한다
	public String getName() {
    //여기에 코드를 입력하세요
    return name;
	}
	//학번을 반환한다
	public int getNumber() {
    //여기에 코드를 입력하세요
    return number;
	}
	// 학생의 모든 데이터를 반환한다.
	public String toString() {
    return("이름: "+name+",학번: " + number);
	}
	//현 객체의 현재 상태가 other 객체와 같은지 알려준다.
	public boolean equals(Student other) {
    return (this.name == other.name && this.number == other.number);
	}
	// 이름을 주어진 값으로 변경한다
	public void setName(String Name) {
    //여기에 코드를 입력하세요
    this.name = Name;
	}
	//학번을 주어진 값으로 변경한다
	public void setNumber(int Number) {
    //여기에 코드를 입력하세요
    this.number = Number;
	}
}
public class Graduate extends Student{
	private String tatype;	        //조교 유형
	private double scholarshipRate; //장학금 비율 
	
	//대학원생의 이름, 학번 조교 유형, 장학금 비율
	// 각각 주어진 값으로 초기화 하면서 객체를 생성
	public Graduate(String Name, int Number,String Tatype,double ScholarshipRate) {
    //여기에 코드를 입력하세요
    super(Name, Number);
    setTatype(Tatype);
    setScholarshipRate(ScholarshipRate);
	}
	//조교 유형 변경
	public void setTatype(String newTatype) {
    //여기에 코드를 입력하세요
    this.tatype = newTatype;
	}
	//장학금 비율 변경
	public void setScholarshipRate(double newScholarshipRate) {
    //여기에 코드를 입력하세요
    this.scholarshipRate = newScholarshipRate;
	}
		// 조교 유형을 반환한다
	public String getTatype() {
    //여기에 코드를 입력하세요
    return tatype;
	}
	
	//장학금 비율을 반환한다
	public double getScholarshipRate() {
    //여기에 코드를 입력하세요
    return scholarshipRate;
	}
	
	
		// 대학원생의 모든 데이터를 반환한다.
	public String toString() {
    //여기에 코드를 입력하세요
    
    return super.toString() + ", 조교 유형: " +tatype+ ", 장학금 비율: " + scholarshipRate;
	}
}
class Main7_4 {
    public static void main(String[] args) {
      Graduate student1 = new Graduate("홍길동",2010123456,"education",0.5);
      System.out.println(student1.toString());
      //이름: 홍길동,학번: 2010123456, 조교 유형: education, 장학금 비율: 0.5
      
        student1.setScholarshipRate(0.5);
          student1.setTatype("research");
          System.out.println(student1.toString());
          Graduate student2 = new Graduate("홍길동",2010123456,"education",1);
          //이름: 홍길동,학번: 2010123456, 조교 유형: research, 장학금 비율: 0.5
          
          System.out.println(student2.equals(student1));
          //true
    
    }
  }