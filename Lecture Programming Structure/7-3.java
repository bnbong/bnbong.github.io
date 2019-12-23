//using classes

// Employee.java
// 직원을 나타낸다
public class Employee {
	public String name;			 // 이름
	public String department;	 // 소속부서
	
	// 직원의 이름과 소속부서를 각각 주어진 값으로 초기화 하면서
	// 새로운 Employee 객체를 생성한다.
	public Employee(String Name, String Department){
		//여기에 코드를 입력하세요
		setName(Name);
		setDepartment(Department);
	}
	
	// 이름을 반환한다
	public String getName() {
		//여기에 코드를 입력하세요
		return name;
	}
	// 소속부서를 반환한다
	public String getDepartment() {
		//여기에 코드를 입력하세요
		return department;
	}
	// 이름을 변경한다
	public void setName(String Name) {
		//여기에 코드를 입력하세요
		name = Name;
	}
	
	// 소속부서를 변경한다
	public void setDepartment(String newDepartment) {
		//여기에 코드를 입력하세요
		department = newDepartment;
	}
	
}
// 정규직 직원을 나타낸다
public class RegEmployee extends Employee{
	protected double yearlySalary;	// 연봉
	protected double bonusRate;		// 보너스 지급률

	// 정규직 직원의 이름, 소속부서, 연봉과 보너스 지급률을
	// 각각 주어진 값으로 초기화하면서 RegEmployee 객체를 생성한다
	public RegEmployee (String name, String department, double yearlySalary, double bonusRate) {
			// 여기에 코드를 입력하세요
			super(name, department);
			this.yearlySalary = yearlySalary;
			this.bonusRate = bonusRate;
	}
	// 정규직 직원의 월급을 계산한다
	public double pay(){
	// 여기에 코드를 입력하세요
		return (yearlySalary / 12.0 * (1.0 + bonusRate));
	}
	
	// 정규직 직원의 모든 데이터를 반환한다
	public String toString() {
		// 여기에 코드를 입력하세요
		return ("직원의 이름 : " + name+ ", 소속 부서: " + department +", 연봉: " + yearlySalary + ", 보너스 지급률: "+bonusRate);
	}
	
}
// 계약직 직원을 나타낸다.
public class TempEmployee extends Employee{
	// 계약직 직원에 대한 객체 변수들을 선언한다
	protected double payRate;	// 시간당 임금
	private int hoursWorked;	// 근무 시간

	// 계약직직원의 이름, 소속부서, 시간담 임금을 주어진 값으로 초기화하고
	// 근무 시간은 0으로 초기화 하면서 TempEmployee 객체를 생성한다
	public TempEmployee(String name, String department, double payRate)
	{
		//여기에 코드를 입력하세요
		super(name, department);
		this.payRate = payRate;
		this.hoursWorked = hoursWorked;
	}
	// 계약직 직원의 월급을 계산한다
	public double pay(){
		//여기에 코드를 입력하세요
    double temp = this.hoursWorked;
    this.hoursWorked = 0;
		return (temp * payRate);
	}
	// 계약직 직원의 추가 근무시간을 누적된 근무시간에 더한다
	public void addHours (int moreHours){
  	//여기에 코드를 입력하세요
		hoursWorked += moreHours;
	}
	// 근무 시간을 반환한다
	public int getHoursworked() {
	  //여기에 코드를 입력하세요
		return hoursWorked;
	}
	// 계약직 직원의 모든 데이터를 반환한다
	public String toString() {
		//여기에 코드를 입력하세요
		return ("직원의 이름 : "+name+", 소속 부서: "+department +", 시간당 임금: " + payRate + ", 근무 시간: " +hoursWorked);
	}

}

public class Main7_3 {

	public static void main(String[] args) {
		RegEmployee employeeOne; // RegEmployee 객체 잠조변수
		TempEmployee employeeTwo; // TempEmployee 객체 참조변수
		
		employeeOne = new RegEmployee("선미","마케팅",6000, 0.4);
		System.out.println(employeeOne.toString());
		//직원의 이름 : 선미, 소속 부서: 마케팅, 연봉: 6000.0, 보너스 지급률: 0.4
		System.out.println(employeeOne.pay());
		//700.0
		
		employeeTwo = new TempEmployee("지나", "연구개발", 1);
		System.out.println(employeeTwo.getHoursworked());
		//0
		employeeTwo.addHours(300);
		System.out.println(employeeTwo.getHoursworked());
		//300
		
		System.out.println(employeeTwo.toString());
		//직원의 이름 : 지나, 소속 부서: 연구개발, 시간당 임금: 1.0, 근무 시간: 300
		System.out.println(employeeTwo.pay());
		//300.0
		System.out.println(employeeTwo.toString());
		//직원의 이름 : 지나, 소속 부서: 연구개발, 시간당 임금: 1.0, 근무 시간: 0



	}

}
