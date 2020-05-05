//using classes

class Pen { // 모든 펜의 공통 속성
    private int amount; // 남은 량
    public int getAmount() { return amount; }
    public void setAmount (final int amount) { this.amount = amount; }
 }
 class SharpPencil extends Pen{ // 샤프펜슬
    // fill here!  
    public SharpPencil(){
      super();
    }
    private int width;
 } 
 
 class Ballpen extends Pen { // 볼펜
    // fill here!  
    public Ballpen() {
      super();
    }
    private String color;
    public String getColor() {return color;}
    public void setColor(final String color) {this.color = color;}
    
 }
 class FountainPen extends Ballpen{ // 만년필
    // fill here!  
    public FountainPen() {
      super();
    }
    public void refill(final int n) {super.setAmount(n);}
 }
 
 class Main8_1 {
   public static void main(final String[] args) {
     final Pen fp = new FountainPen();
     fp.setAmount(1);
     System.out.println(fp.getAmount()); // 1 
   }
 }