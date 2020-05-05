public class Q5_2018 {
   public static void sort(String[] a) {
      int N = a.length;
      for (int i = 1; i < N; i++)
         for (int j = i; j > 0; j--)
            if (a[j-1].compareTo(a[j]) > 0) 
               exch(a, j-1, j);
            else break;
   }
   private static void exch(String[] a, int i, int j) {
      String swap = a[i];
      a[i] = a[j];
      a[j] = swap;
   }
   public static void main(String[] args) {
       String[] arr = new String[4];
        arr[0] = "d"; arr[1] = "a"; arr[2] = "c"; arr[3] = "b";
        sort(arr);
        for (int i = arr.length-1; i>=0; i--) 
            System.out.print(arr[i] + " ");
        // should print d c b a
   }
}
