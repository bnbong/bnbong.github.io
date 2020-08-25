class stringLength{
  public static int longest_incseq(int[] arr) {
    // fill here! 
    int count = 0;
    int temp = arr[0];
    for(int i = 0; i < arr.length; i++) {
      if (temp < arr[i]) {
        temp = arr[i];
        count++;
      }
    }
    return count+1;
  }
  public static void main(String[] args) {
    int[] arr = {10, 20, 10, 30, 20, 50};
    System.out.println(longest_incseq(arr)); // 4
  }
}