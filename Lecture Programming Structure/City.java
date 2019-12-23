public class City {
  // ���� �̸�
  private String cityName;
  // ���� �α�
  private int population;
  // ������ �α� ������ (%)
  private double growthRate;
  
  public City(int populationIn, double growthRateIn, String cityNameIn) {
    population = populationIn;
    growthRate = growthRateIn; 
    cityName = cityNameIn;
  }
  
  
  // �־��� ���� ���� ���� �α��� ����Ѵ�
  public int computeFuturePopulation(int years) {
    // ���� �α�
    double populationAmount = population;
    // ����
    int count = years;
    // �־��� ���� ���� ���� �α��� ����Ѵ� 
    populationAmount = populationAmount * (Math.pow(((100.0+growthRate)/100.0),(double)count));
    // ���� �α��� ��ȯ�Ѵ�
    return (int)populationAmount;
      
  }
  // ���� �̸��� �־��� ������ �����Ѵ� 
  public void setName(String newName) {
    cityName = newName;
  }
  public void setpopulation(int newpopulation){
    population = newpopulation;
  }
  public void setgrowthrate(int newgrowthrate){
    growthRate = newgrowthrate;
  }
  // ���� �α��� �־��� ������ ���� 
  // ���� �α� �������� �־��� ������ ���� 
  // ���� �̸��� ��ȯ�Ѵ� 
  public String getName() {
    return cityName;
  }
  // ���� �α��� ��ȯ�Ѵ�
  public int getPopulation() {
    return population;
  }
  // ���� �α� �������� ��ȯ�Ѵ� 
  public double getGrowthRate() {
    return growthRate;
  }
  
}
/*
class Main {
	  
	  public static void main(String[] args) {
	    // ���� �α�, ������ �α� ������ (%), ���� �̸�
	    City aCity = new City(500000, 1.5, "Ansan");
	    int newPopulation;
	    int years = 10;
	    newPopulation = aCity.computeFuturePopulation(years);
	    System.out.println(newPopulation);
	  }
	  
	}
*/