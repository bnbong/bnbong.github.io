//using array

class Main6_3 {
    public static int[] merge(int[] arr1, int[] arr2) {
      // fill here! 
      int[] merged = new int[arr1.length + arr2.length];
      System.arraycopy(arr1, 0, merged, 0, arr1.length);
      System.arraycopy(arr2, 0, merged, arr1.length, arr2.length);
      int i = 1;
      while (i <= merged.length) {
        for (int j = 0; j < merged.length - 1; j++) {
          if (merged[j] > merged[j+1]) {
            int temp = merged[j];
            merged[j] = merged[j+1];
            merged[j+1] = temp;
          }
        }
        i += 1;
      }
      return merged;
      
    }
    public static void main(String[] args) {
      int[] arr1 = {1, 2, 4, 8, 16};
      int[] arr2 = {3, 6, 9, 12}; 
      int[] merged = merge(arr1, arr2); 
      for (int i = 0 ; i < merged.length; i++) {
        System.out.println(merged[i]); 
        // 1 2 3 4 6 8 9 12 16
      }
    }
  }