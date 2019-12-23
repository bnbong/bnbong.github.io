public class City {
  // 도시 이름
  private String cityName;
  // 도시 인구
  private int population;
  // 도시의 인구 증가율 (%)
  private double growthRate;
  
  public City(int populationIn, double growthRateIn, String cityNameIn) {
    population = populationIn;
    growthRate = growthRateIn; 
    cityName = cityNameIn;
  }
  
  
  // 주어진 연도 후의 예상 인구를 계산한다
  public int computeFuturePopulation(int years) {
    // 예상 인구
    double populationAmount = population;
    // 연도
    int count = years;
    // 주어진 연도 후의 예상 인구를 계산한다 
    populationAmount = populationAmount * (Math.pow(((100.0+growthRate)/100.0),(double)count));
    // 예상 인구를 반환한다
    return (int)populationAmount;
      
  }
  // 도시 이름을 주어진 값으로 변경한다 
  public void setName(String newName) {
    cityName = newName;
  }
  public void setpopulation(int newpopulation){
    population = newpopulation;
  }
  public void setgrowthrate(int newgrowthrate){
    growthRate = newgrowthrate;
  }
  // 도시 인구를 주어진 값으로 변경 
  // 도시 인구 증가율을 주어진 값으로 변경 
  // 도시 이름을 반환한다 
  public String getName() {
    return cityName;
  }
  // 도시 인구를 반환한다
  public int getPopulation() {
    return population;
  }
  // 도시 인구 증가율을 반환한다 
  public double getGrowthRate() {
    return growthRate;
  }
  
}
/*
class Main {
	  
	  public static void main(String[] args) {
	    // 도시 인구, 도시의 인구 증가율 (%), 도시 이름
	    City aCity = new City(500000, 1.5, "Ansan");
	    int newPopulation;
	    int years = 10;
	    newPopulation = aCity.computeFuturePopulation(years);
	    System.out.println(newPopulation);
	  }
	  
	}
*/