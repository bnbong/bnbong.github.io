//using try, catch

class Main9_4 {
    public static int fact(int n) {
          
          try {
            // fill here!
            if (n < 0) {
              throw new IllegalArgumentException("Negative numbers cannot be calculated");
            }
            else if(n == 0){
              n = 1;
            }
            else {
              n = n * fact(n-1);
            }
          } 
          catch (IllegalArgumentException e) {
            // fill here!
            System.out.println(e.getMessage());
          }
          
          return n;
      }
  
      public static void main(String[] args) {
        System.out.println(fact(5));
        //120
        
        System.out.println(fact(-5));
          //Negative numbers cannot be calculated
      //-5
  
  
      }
  }