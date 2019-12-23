//using abstract method

abstract class Converter {
    abstract protected double convert(double src); // 추상 메소드
    abstract protected String getSrcString(); // 추상 메소드
    abstract protected String getDestString(); // 추상 메소드
    protected double ratio; // 비율
    public double run(double val) {
       System.out.println("convert " + val + " " + getSrcString()+" to "+getDestString());
       double res = convert(val);
       System.out.println(res + " " + getDestString());
       return res; 
    }
 }
 
 class Won2Dollar extends Converter {
    // fill here!
   public Won2Dollar(double won) {
     this.ratio = won;
   }
   @Override
   public double convert(double src) {
     return (src/ratio);
   }
   @Override
   public String getSrcString() {
     return "won";
   }
   @Override
   public String getDestString() {
     return "dollar";
   }
 }
 
 class Km2Mile extends Converter {
    // fill here!
    public Km2Mile(double km) {
      this.ratio = km;
    }
    @Override
    public double convert(double src) {
      return (src/ratio);
    }
    @Override
    public String getSrcString() {
      return "km";
    }
    @Override
    public String getDestString() {
      return "mile";
    }
 }
 
 class Main8_2 {
   public static void main(String[] args) {
     Won2Dollar toDollar = new Won2Dollar(1200); // 1달러는 1200원
     toDollar.run(2400);
     Km2Mile toMile = new Km2Mile(1.6); // 1마일은 1.6km
     toMile.run(3.2);
   }
 }