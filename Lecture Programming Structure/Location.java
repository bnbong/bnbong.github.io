public class Location {

  private double latitude;   // 위도 
  private double longitude;   // 경도 
  public Location (double lat, double lon) {
    this.latitude = lat;
    this.longitude = lon;
  }
  public double getLatitude() { 
    return this.latitude;
  }
  public double getLongitude() {
    return this.longitude; 
  }
  public double distance (Location other) {
    double RADIUS_EARTH = 6371.0;   // 지구의 반지름
    //return this.latitude - other.latitude;
    return RADIUS_EARTH * Math.acos(Math.cos(Math.toRadians(90.0-this.latitude)) * Math.cos(Math.toRadians(90.0-other.latitude)) + Math.sin(Math.toRadians(90.0-this.latitude)) * Math.sin(Math.toRadians(90.0-other.latitude)) * Math.cos(Math.toRadians(this.longitude - other.longitude)));
    
    // fill here!
  }
}
/*
class Main {
	  public static void main(String[] args) {
	    Location loc1 = new Location(37.567, 126.978); 
	    Location loc2 = new Location(35.179,129.076); 
	    System.out.println(loc1.distance(loc2)); // 325.23184366269084 출력
	  }
	}
*/