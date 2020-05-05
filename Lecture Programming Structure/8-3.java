//array setting practice

interface MyArray {
    int length(); // 현재 배열에 저장된 개수 리턴
    int capacity(); // 배열의 전체 저장 가능한 개수 리턴
    String get_remove(int index); // index에 해당하는 값 반환후, 배열에서 해당 값 없애기.  
    boolean set(String val, int index); // index에 해당하는 값으로 val 저장
 }
 
 class StringArray implements MyArray {
    private int max_num; // 저장 가능한 값 개수
    private int num; // 저장한 값 개수
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
 
 class Main8_3 {
   public static void main(String[] args) {
     MyArray arr = new StringArray(100);
     arr.set("a", 0);
     arr.set("b", 1);
     arr.set("c", 2);
     System.out.println(arr.get_remove(0));//a
     System.out.println(arr.get_remove(0));//b
     
   }
 }