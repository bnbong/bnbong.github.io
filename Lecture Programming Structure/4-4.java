//Employee practice

public class Employee {
	private Double salary;	// 연봉
	private int evalGrade;	// 근무평가등급
	
	public Employee(double salary, int evalGrade) {
		this.salary = salary;
		this.evalGrade = evalGrade;
	}
	
	// get 함수 모음
	public double getSalary() {
		return salary;
	}
	
	public int getEvalGrade() {
		return evalGrade;
	}
	
	// set 함수 모음
	public void setSalary(double salary) {
		this.salary = salary;
	}
	
	public void setEvalGrade(int evalGrade) {
		this.evalGrade = evalGrade;
	}
	
	public void set(double salary, int evalGrade) {
		this.salary = salary;
		this.evalGrade = evalGrade;
	}
	
	// 근무평가등급에 따라 현재 연봉을 인상시키고, 연봉 인상 금액을 반환한다.
	public Double applyIncreaseRate() {
		// 여기에 코드를 삽입하세요
		if (this.evalGrade == 1) salary = (this.salary * 106.0)/100.0; //
		else if (this.evalGrade == 2) salary = (this.salary * 104.0)/100.0;
		else salary = (this.salary * 102.0)/100.0;
		return salary;
	}
}
class Main4_4 {
    public static void main(String[] args) {
          // 여기에 test code 를 작성해서 테스트해볼 수 있습니다.
          // 예:
          //Employee emp = new Employee(2400.0, 1);
          //1이면 우수, 0이면 보통, -1이면 불량
          //System.out.println(emp.applyIncreaseRate());	// 2544.0 출력
    }
  }