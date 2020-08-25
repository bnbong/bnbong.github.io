//using variable problem

class Main1_3 {
    public static void main(String[] args) {
      // 영작문， 프로그래밍, 이산수학 과목의 점수들을 저장하는 
      // 변수들을 선언한다
      int compgrade, proggrade, mathgrade;
      // 과목 접수들의 평균을 저장하는 변수를 선언한다 
      double average; 
      
      // 영작문 과목의 점수를 88로 한다. 
      compgrade = 88; 
      // 프로그래밍 과목의 점수를 92점으로 한다
      proggrade = 92;
      // 이산수학 과목의 점수를 79점으로 한다
      mathgrade = 79;
      // 과목 점수들의 평균을 계산한다
      average = (double)(compgrade + proggrade + mathgrade)/3;
        // 여기에 코드를 삽입하세요 
        
      // 평균점수를 출력한다 
      System.out.println(average);
    }
  }