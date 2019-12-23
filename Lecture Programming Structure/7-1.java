//using classes

import java.util.*;

public class Main7_1 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String shotAnswer;	// 예방주사 접종여부 입력 값
		String dogName; 	  // 개 이름
		int dogAge; 	  	  // 개 나이
		String dogBreed; 	  // 개 품종
		boolean dogShot; 	  // 예방주사 접종여부
		

		Dog Dog1 = new Dog();
		System.out.println(Dog1.toString());
		//이름: , 나이: 0, 품종: , 접종여부: false
		
		Dog1.setName("haru");
		Dog1.setAge(3);
		Dog1.setBreed("Jindo");
		Dog1.setboostreShot();
		System.out.println(Dog1.toString());
		//이름: haru, 나이: 3, 품종: Jindo, 접종여부: true
		
		Dog Dog2 = new Dog("dangdang",4,"poodle");
		System.out.println(Dog2.toString());
		//이름: dangdang, 나이: 4, 품종: poodle, 접종여부: false
		
	}

}

public class Pet {
	private String name; // 이름
	private int age; // 나이

	// 애완동물의 이름과 나이를 각각 기본 값으로 초기화하면서
	// Pet 객체를 생성한다
	// 나이 기본값: 빈 문자열, 나이 기본값: 0
	public Pet() {
	  name = "";
	  age = 0;
		// 여기에 코드를 입력하세요
	}

	// 애완동물의 이름과 나이를 각각 주어진 값으로 초기화하면서
	// Pet 객체를 생성한다
	public Pet(String name, int age) {
		// 여기에 코드를 입력하세요
		setName(name);
		setAge(age);
		
	}

	// 애완동물의 이름을 변경한다
	public void setName(String newName) {
		// 여기에 코드를 입력하세요
		name = newName;
	}

	//애완동물의 나이를 변경한다
	public void setAge(int Age) {
		// 여기에 코드를 입력하세요
		age = Age;
	}

	// 애완동물의 이름을 알려 준다
	public String getName() {
		// 여기에 코드를 입력하세요
		return name;
	}

	// 애완동물의 나이를 알려 준다
	public int getAge() {
	  return age;
		// 여기에 코드를 입력하세요
	}


	// 애완동물의 이름과 나이를 알려 준다
	public String toString() {
		// 여기에 코드를 입력하세요
		return ("이름: "+name+ " 나이: "+age);
	}
}
public class Dog extends Pet{
	private String breed;	    	// 품종
	private boolean boostreShot;// 예방주사 접종 여부
	
	// 개의 이름, 나이, 품종을 각각 기본 값으로 초기화하고
	// 예방주사 접종여부는 false로 초기화하면서 Dog 객체를 생성한다
	// 품종 기본 값: 빈 문자열
	public Dog()
	{
	  breed = "";
	  boostreShot = false;
	// 여기에 코드를 입력하세요
	}
	
	// 개의 이름, 나이, 품종을 각각 주어진 값으로 초기화하고
	// 예방주사 접종여부는 false로 초기화하먼서 Dog 객체를 생성한다
	public Dog(String name, int age, String breed)
	{
	  super(name,age);
	  setBreed(breed);
	  
	  
	// 여기에 코드를 입력하세요
	}
	
	// 개의 모든 데이터를 알려 준다
	public String toString() {
	// 여기에 코드를 입력하세요
		return super.toString() + " 품종: "+breed+" 접종여부: "+boostreShot;
	}

	// 개의 품종을 변경한다
	public void setBreed(String newBreed){
	// 여기에 코드를 입력하서세요
	  breed = newBreed;
	}
	
	// 개의 예방주사 접종여부를 변경한다
	public void setboostreShot() {
		//여기에 코드를 입력하세요
		boostreShot = true;
		
	}

	// 개의 품종을 알려준다
	public String getGreed() {
		//여기에 코드를 입력하세요
		return breed;
	}
	
	// 개의 예방주사 접종 여부를 알려준다
	public boolean getboostreShot() {
		// 여기에 메소드를 입력하세요
		return boostreShot;
	}
}

