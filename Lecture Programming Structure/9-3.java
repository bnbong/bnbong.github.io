//using try, catch

class Main9_3 {
    public static int string_sum(String str) {
      // fill here! 
      int sum = 0;
      try{
        String[] array = str.split(" ");
        for(int j = 0; j < array.length; j++) {
          Double.parseDouble(array[j]);
          int integer = Integer.parseInt(array[j]);
          sum += integer;
  
        }
        return sum;
      }
      catch(NumberFormatException e){
        return 0;
      }
      }
  
      public static void main(String[] args) {
          System.out.println(string_sum("100 q 300")); // 0
          System.out.println(string_sum("100 300")); // 400
      }
  }