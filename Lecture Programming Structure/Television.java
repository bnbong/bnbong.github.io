// Television.java
// �ڷ����� ��ü�� ǥ��
public class Television {
  private String BrandName;  // �귣��� 
  private boolean Powered = false;  // �����ִ°�? 
  private int Channel = 1;  // ���� ä�� 
  int Volume = 0;  // ���� ���� 
  // ������ 
  public Television() {
    // �ƹ��͵� ����. 
  }

  public String toString() {
    String str = "Brandname: " + BrandName + "\n";
    str = str + "IsPowered: " + Powered + "\n";
    str = str + "Channel: " + Channel + "\n";
    str = str + "Volume: " + Volume;
    return str;
  }
  
  // ���� �Լ����� �����ϼ���. 
  public int getChannel() {
    return Channel;
  }
  // getChannel : ���� ä���� ��ȯ�Ѵ�. 
  public String getBrandName() {
    return BrandName;
  }
  // getBrandName : �귣����� ��ȯ�Ѵ�. 
  public int getVolume() {
    return Volume;
  }
  // getVolume : ���� ������ ��ȯ�Ѵ�. 
  public boolean getPower() {
    return Powered;
  }
  // getPower : ���� ���� ���¸� ��ȯ�Ѵ�. 
  
  // TV �� ������ �־��� ������ ����. 
  public void setPowered(boolean NewPowered) {
    Powered = NewPowered; 
  }
  
  // ���� �Լ����� �����ϼ���. 
  public void setChannel(int NewChannel) {
    Channel = NewChannel;
  }
  // setChannel : TV�� ä�� ��ȣ�� �־��� ������ ����. 
  public void setBrandName(String NewBrandName) {
    BrandName = NewBrandName;
  }
  // setBrandName : TV�� �귣����� �־��� ������ ����. 
  public void setVolume(int NewVolume) {
    Volume = NewVolume;
  }
  // setVolume : TV�� ������ �־��� ������ ����. 
  public void incrementChannel() {
    Channel += 1;
  }
  // incrementChannel : TV�� ä���� 1��ŭ ������Ų��. 
  public void decrementChannel() {
    Channel -= 1;
  }
  // decrementChannel : TV�� ä���� 1��ŭ ���ҽ�Ų��. 
  public void incrementVolume() {
    Volume += 1;
  }
  public void decrementVolume() {
    Volume -= 1;
  }
  // incrementVolume : TV�� ������ 1��ŭ ������Ų��. 
  // decrementVolume : TV�� ������ 1��ŭ ���ҽ�Ų��. 
}
/*
class Main {
  public static void main(String[] args) {
    Television tv1 = new Television(); 
    tv1.setBrandName("samsung");
    tv1.setPowered(true);
    tv1.setVolume(10);
    tv1.setChannel(11);
    System.out.println(tv1);
  }
}
 */