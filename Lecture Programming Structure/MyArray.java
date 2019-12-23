interface MyArray {
   int length(); // ���� �迭�� ����� ���� ����
   int capacity(); // �迭�� ��ü ���� ������ ���� ����
   String get_remove(int index); // index�� �ش��ϴ� �� ��ȯ��, �迭���� �ش� �� ���ֱ�.  
   boolean set(String val, int index); // index�� �ش��ϴ� ������ val ����
}

class StringArray implements MyArray {
   private int max_num; // ���� ������ �� ����
   private int num; // ������ �� ����
   private String[] arr;
   public StringArray(int num) {
      // fill here!
      arr = new String[num];
      this.max_num = num;
      this.num = 0;
   }
   public int length() {
      // fill here!
      return num;
   }
   public int capacity() {
      // fill here!
      return (max_num - num);
   }
   public String get_remove(int index) {
      // fill here!
      String temp = arr[index];
      this.num -= 1;
      for (int i = index; i < max_num - 1; i++) {
        arr[i] = arr[i+1];
      }
      return temp;
   }
   public boolean set(String val, int index) {
      // fill here!
      this.num = this.num + 1;
      arr[index] = val;
      return true;
   }
}

class Main {
  public static void main(String[] args) {
    MyArray arr = new StringArray(100);
    arr.set("a", 0);
    arr.set("b", 1);
    arr.set("c", 2);
    System.out.println(arr.get_remove(0));//a
    System.out.println(arr.get_remove(0));//b
    
  }
}