// Employee.java 
// ������ ��Ÿ����. 
public class Employee {
  private String name; // �̸� 
  private int number; // ��ȣ 
  private int age; // ���� 
  
  // ���ο� Employee ��ü�� �����Ѵ�  
  public Employee() {
    
  }
  // ������ �޼ҵ� - �̸��� ��ȯ�Ѵ�. 
  public String getName() {
    return name; 
  }
  // ������ �޼ҵ� - ��ȣ�� ��ȯ�Ѵ�. 
  public int getNumber() {
    // ���⿡ �ڵ带 �����ϼ���. 
    return number;
    
  }
  // ������ �޼ҵ� - ���̸� ��ȯ�Ѵ�. 
  public int getAge() {
    // ���⿡ �ڵ带 �����ϼ���. 
    return age;
    
  }
  // �� Employee ��ü�� ������ ���� ���ڿ��� ��ȯ�Ѵ�. 
  public String toString() {
    return "Name: " + name + "\n" + "Number: " + number + "\n" + "Age: " + age;
  }
  // ������ �޼ҵ� - �̸��� �־��� ������ �����Ѵ�. 
  public void setName(String Name) {
    // ���⿡ �ڵ带 �����ϼ���.
    name = Name;
  
    
  }
  // ������ �޼ҵ� - ��ȣ�� �־��� ������ �����Ѵ�. 
  public void setNumber(int Number) {
    // ���⿡ �ڵ带 �����ϼ���. 
    number = Number;
  
    
  }
  // ������ �޼ҵ� - ���̸� �־��� ������ �����Ѵ�. 
  public void setAge(int Age) {
    // ���⿡ �ڵ带 �����ϼ���. 
    age = Age;
  
    
  }
}
//Main.java 
//Employee ��ü�� ����� ����Ѵ�.  
/*
public class Main {
public static void main(String[] args) {
 Employee emp1 = new Employee();
 emp1.setName("lee");
 emp1.setNumber(100);
 emp1.setAge(25); 
 System.out.println(emp1); 
}
}
*/