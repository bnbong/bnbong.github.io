//using variable with Scanner

import java.util.*;

class Main1_4 {
  public static void main(String[] args) {
    //  화씨 온도를 저장하는 실수형 변수를 선언한다
    double F; 
    // 섭씨 온도를 저장하는 실수형 변수를 선언한다 
    double C; 
    // Scanner 객체를 생성하고 변수 scan 이 그 객체를 가리키게 한다
    Scanner scan = new Scanner(System.in);
    
    // 화씨 온도를 키보드를 통해 읽어 들인다
    System.out.print("화씨 온도를 입력하세요: ");
    F = scan.nextDouble();
    C = (F-32.0)*(5.0/9.0);
    
    // 화씨 온도를 섭씨 온도로 바꾸고 그 값을 섭씨 온도를 나타내는 변수에 저장한다
    // 참고: 화씨 온도를 섭씨 온도로 변환하는 공식은 C = (5/9)(F - 32) 이다. 

    // 화씨 온도와 대응하는 섭씨 온도를 출력한다
    System.out.println(C);
    scan.close();
  }
}