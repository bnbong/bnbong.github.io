/*
**** FoodDecisionMaker ver.JAVA ****
///authorized by bnbong, JJongmen///

/*
Run At JAVA OpenJDK11, Linux
work at Ubuntu 18.04.3 Visual Studio Code 1.41.0
*/

/*
/   *****README*****
/
/
/  
/  
/  
/
*/

import java.util.Scanner;
import java.util.Random;

interface Key { public boolean equals(Key m); }
interface Record { public Key keyOf(); public String KeyOfName();public String KeyOfMenu(); public String KeyOfExpensive(); public String KeyOfDistance(); public String KeyOfRating();}

/*
 / Record에 저장되는 음식점에 관한 데이터는
 / 음식점의 이름, 음식점에서 파는 음식의 종류(양식/한식), 가격의 크기(비싼가 안비싼가), 학교와의 거리(먼가 멀지 않은가), 평점
 / 으로 구성됨.
*/

class StringDoubleKey implements Key {
    private String id_str_restname;
    private String id_str_menukinds; 
    private String expensive;
    private String distance;
    private String rating; 
    
	public StringDoubleKey(String s, String i, String e, String d, String r) {id_str_restname = s; id_str_menukinds = i; expensive = e; distance = d; rating = r;}
	public String getKindString() { return id_str_menukinds; }
    public String getNameString() { return id_str_restname;}
    public String getExpensive() { return expensive;}
    public String getDistance() {return distance; }
    public String getRating() {return rating; }

	public boolean equals(Key m) {
        return id_str_menukinds == ((StringDoubleKey)m).getKindString() && id_str_restname == ((StringDoubleKey)m).getNameString() && expensive == ((StringDoubleKey)m).getExpensive()
        && distance == ((StringDoubleKey)m).getDistance() && rating == ((StringDoubleKey)m).getRating();
    }
    
    public boolean equals_with_menu(Key m) {
        return id_str_menukinds == ((StringDoubleKey)m).getKindString();
    }

    public boolean equals_with_expensive(Key m) {
        return expensive == ((StringDoubleKey)m).getExpensive();
    }

    public boolean equals_with_distance(Key m) {
        return distance == ((StringDoubleKey)m).getDistance();
    }

    public boolean equals_with_rating(Key m) {
        return rating == ((StringDoubleKey)m).getRating();
    }

	public String toString() { return id_str_restname + id_str_menukinds + expensive + distance + rating; }
}


class OtherElements implements Record {
	private StringDoubleKey restaurant_id;
	
	public OtherElements(StringDoubleKey stringDoubleKey) {
        restaurant_id = stringDoubleKey;
    }
    
    public Key keyOf() {
	    return restaurant_id;
    }
    public String KeyOfName() {
        return restaurant_id.getNameString();
    }
    public String KeyOfMenu() {
        return restaurant_id.getKindString();
    }

    public String KeyOfExpensive() {
        return restaurant_id.getExpensive();
    }

    public String KeyOfDistance() {
        return restaurant_id.getDistance();
    }

    public String KeyOfRating() {
        return restaurant_id.getRating();
    }

	public String toString() {
        return restaurant_id.toString();
	}

    
} 


public class FoodDecisionMaker {

   
    public static Record[] shuffle(Record[] db) {
        
        for (int j = 0; j < db.length; j++) {
            
            int i = (int)(Math.random() * db.length - 1);
            Record temp = db[j];
            db[j] = db[i];
            db[i] = temp;
            
        }
        
        return db;
    }

    public static void DecisionRullet() {
        int element = 0;
        System.out.println("Write number of elements to run rullet.");
        Scanner scanner = new Scanner(System.in);
        element = scanner.nextInt();

        String[] rullet = new String[element];

        int i = 0;
        while (i < element) {
            String str_element = "";
            System.out.println("Write element at " + (i + 1));
            Scanner string = new Scanner(System.in);
            str_element = string.nextLine();
            rullet[i] = str_element;
            if (rullet[i] != null)
                i++;
            if (i == element) {
                string.close();
            }
        }
        Random random = new Random();

        System.out.println("Result : " + rullet[random.nextInt(element)]);
        System.out.println("Thank You!");
        scanner.close();
    }

    public static void DecisionNavigator_f(Record[] db) {
        System.out.println("Which kinds of food do you want? : (Enter w for Western food, k for Korean food)");
        Scanner scanner2 = new Scanner(System.in);
            try{
                char food_response = scanner2.next().charAt(0);
                if(food_response != 'w' && food_response != 'k') {scanner2.close(); throw new Exception();}
                if (food_response == 'w') {
                    int i = 0;
                    while(db[i] != null) {
                        if(db[i].KeyOfMenu() == "Western food") {
                            System.out.println("How about " + db[i].KeyOfName());
                            System.out.println("Price : " + db[i].KeyOfExpensive() + " Distance : " + db[i].KeyOfDistance() + " Rating : " + db[i].KeyOfRating());
                            System.out.println("Thank you!!");
                            break;
                        }
                        i++;
                    }
                } else if(food_response == 'k') {
                    int i = 0;
                    while(db[i] != null) {
                        if(db[i].KeyOfMenu() == "Korean food") {
                            System.out.println("How about " + db[i].KeyOfName());
                            System.out.println("Price : " + db[i].KeyOfExpensive() + " Distance : " + db[i].KeyOfDistance() + " Rating : " + db[i].KeyOfRating());
                            System.out.println("Thank you!!");
                            break;
                        }
                        i++;
                    }
                }
            } catch(Exception e) {
                System.out.println("Something has wrong, Bye!");
                
            }
        
        
        scanner2.close();
    }

    public static void DecisionNavigator_p(Record[] db) {
        System.out.println("Which price do you want? : (Enter c for cheap, e for expensive)");
        Scanner scanner3 = new Scanner(System.in);
            try{
                char price_response = scanner3.next().charAt(0);
                if(price_response != 'c' && price_response != 'e') {scanner3.close(); throw new Exception();}
                if(price_response == 'c') {
                    int i = 0;
                    while(db[i] != null) {
                        if(db[i].KeyOfExpensive() == "Cheap") {
                            System.out.println("How about " + db[i].KeyOfName());
                            System.out.println("Kinds of menu : " + db[i].KeyOfMenu() + " Distance : " + db[i].KeyOfDistance() + " Rating : " + db[i].KeyOfRating());
                            System.out.println("Thank you!!");
                            break;
                        }
                        i++;
                    }
                } else if(price_response == 'e') {
                    int i = 0;
                    while(db[i] != null) {
                        if(db[i].KeyOfExpensive() == "Expensive") {
                            System.out.println("How about " + db[i].KeyOfName());
                            System.out.println("Kinds of menu : " + db[i].KeyOfMenu() + " Distance : " + db[i].KeyOfDistance() + " Rating : " + db[i].KeyOfRating());
                            System.out.println("Thank you!!");
                            break;
                        }
                        i++;
                    }
                }
            } catch(Exception e) {
                System.out.println("Something has wrong, Bye!");
                
            }
        
        
        scanner3.close();
    }

    public static void DecisionNavigator_d(Record[] db) {
        System.out.println("How far restaurant do you want? : (Enter c for close f for far)");
        Scanner scanner4 = new Scanner(System.in);
            try{
                char dis_response = scanner4.next().charAt(0);
                if(dis_response != 'c' && dis_response != 'f') {scanner4.close(); throw new Exception();}
                if(dis_response == 'c') {
                    int i = 0;
                    while(db[i] != null) {
                        if(db[i].KeyOfDistance() == "Close") {
                            System.out.println("How about " + db[i].KeyOfName());
                            System.out.println("Kinds of menu : " + db[i].KeyOfMenu() + " Price : " + db[i].KeyOfExpensive() + " Rating : " + db[i].KeyOfRating());
                            System.out.println("Thank you!!");
                            break;
                        }
                        i++;
                    }
                } else if(dis_response == 'f') {
                    int i = 0;
                    while(db[i] != null) {
                        if(db[i].KeyOfDistance() == "Far") {
                            System.out.println("How about " + db[i].KeyOfName());
                            System.out.println("Kinds of menu : " + db[i].KeyOfMenu() + " Price : " + db[i].KeyOfExpensive() + " Rating : " + db[i].KeyOfRating());
                            System.out.println("Thank you!!");
                            break;
                        }
                        i++;
                    }
                }
            } catch(Exception e) {
                System.out.println("Something has wrong, Bye!");
                
            }
        
        
        scanner4.close();
    }

    public static void DecisionNavigator_r(Record[] db) {
        System.out.println("How much rating of restaurant do you want? : (Enter l for low h for high)");
        Scanner scanner5 = new Scanner(System.in);
            try{
                char rat_response = scanner5.next().charAt(0);
                if(rat_response != 'l' && rat_response != 'h') {scanner5.close(); throw new Exception();}
                if(rat_response == 'l') {
                    int i = 0;
                    while(db[i] != null) {
                        if(db[i].KeyOfRating() == "Low") {
                            System.out.println("How about " + db[i].KeyOfName());
                            System.out.println("Kinds of menu : " + db[i].KeyOfMenu() + " Price : " + db[i].KeyOfExpensive() + " Distance : " + db[i].KeyOfDistance());
                            System.out.println("Thank you!!");
                            break;
                        }
                        i++;
                    }
                } else if(rat_response == 'h') {
                    int i = 0;
                    while(db[i] != null) {
                        if(db[i].KeyOfRating() == "High") {
                            System.out.println("How about " + db[i].KeyOfName());
                            System.out.println("Kinds of menu : " + db[i].KeyOfMenu() + " Price : " + db[i].KeyOfExpensive() + " Distance : " + db[i].KeyOfDistance());
                            System.out.println("Thank you!!");
                            break;
                        }
                        i++;
                    }
                }
            } catch(Exception e) {
                System.out.println("Something has wrong, Bye!");
                
            }
        
        
        scanner5.close();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Record[] db = new Record[46]; // change number with amount of Records
        Record r1 = new OtherElements(new StringDoubleKey("SubWay", "Western food", "Expensive", "Close", "Low"));
        Record r2 = new OtherElements(new StringDoubleKey("213 Burger", "Western food", "Cheap", "Close", "High"));
        Record r3 = new OtherElements(new StringDoubleKey("jjigae jjigae", "Korean food", "Cheap", "Close", "High"));
        Record r4 = new OtherElements(new StringDoubleKey("All Chone", "Korean food", "Cheap", "Close", "High"));
        Record r5 = new OtherElements(
                new StringDoubleKey("Bistro Tabom", "Western food", "Expensive", "Close", "High"));
        Record r6 = new OtherElements(new StringDoubleKey("Kimgane", "Korean Food", "Cheap", "Close", "High"));
        Record r7 = new OtherElements(new StringDoubleKey("Bap FULL", "Korean Food", "Cheap", "Close", "Low"));
        Record r8 = new OtherElements(
                new StringDoubleKey("Myungga Tteokbokki", "Korean Food", "Cheap", "Close", "High"));
        Record r9 = new OtherElements(
                new StringDoubleKey("Eunhwasu Restaurant", "Western Food", "Cheap", "Close", "High"));
        Record r10 = new OtherElements(
                new StringDoubleKey("Crazyed Chicken", "Western Food", "Cheap", "Close", "High"));
        Record r11 = new OtherElements(new StringDoubleKey("DosMas", "Western Food", "Cheap", "Close", "High"));
        Record r12 = new OtherElements(new StringDoubleKey("han greut", "Korean Food", "Expensive", "Close", "High"));
        Record r13 = new OtherElements(new StringDoubleKey("Meal Plan B", "Western Food", "Cheap", "Close", "High"));
        Record r14 = new OtherElements(new StringDoubleKey("mat jarang", "Korean Food", "Expensive", "Close", "High"));
        Record r15 = new OtherElements(
                new StringDoubleKey("HanYang Restaurant", "Korean Food", "Cheap", "Close", "Low"));
        Record r16 = new OtherElements(new StringDoubleKey("ilmi dakgalbi", "Korean Food", "Cheap", "Close", "High"));
        Record r17 = new OtherElements(
                new StringDoubleKey("Brown donkkaseu", "Western Food", "Expensive", "Close", "High"));
        Record r18 = new OtherElements(new StringDoubleKey("The Chicken", "Western Food", "Cheap", "Close", "High"));
        Record r19 = new OtherElements(new StringDoubleKey("Cook's vill", "Western Food", "Cheap", "Close", "High"));
        Record r20 = new OtherElements(new StringDoubleKey("Positano", "Western Food", "Expensive", "Close", "High"));
        Record r21 = new OtherElements(new StringDoubleKey("naembi house", "Korean Food", "Cheap", "Close", "High"));
        Record r22 = new OtherElements(new StringDoubleKey("meoggogaja", "Korean Food", "Cheap", "Close", "High"));
        Record r23 = new OtherElements(
                new StringDoubleKey("Seongbuk-dong gyeongyangsik", "Western Food", "Expensive", "Close", "High"));
        Record r24 = new OtherElements(
                new StringDoubleKey("Happy jjamppong", "Western Food", "Cheap", "Close", "High"));
        Record r25 = new OtherElements(
                new StringDoubleKey("Jelly Factory", "Korean Food", "Expensive", "Close", "High"));
        Record r26 = new OtherElements(
                new StringDoubleKey("yume restaurant", "Western Food", "Expensive", "Close", "High"));
        Record r27 = new OtherElements(
                new StringDoubleKey("Dongari restaurant", "Korean Food", "Cheap", "Close", "High"));
        Record r28 = new OtherElements(
                new StringDoubleKey("yetnalhaksa jeyookssambap", "Korean Food", "Cheap", "Close", "High"));
        Record r29 = new OtherElements(new StringDoubleKey("EBISU", "Western Food", "Expensive", "Far", "High"));
        Record r30 = new OtherElements(
                new StringDoubleKey("Brother Steak", "Western Food", "Expensive", "Far", "High"));
        Record r31 = new OtherElements(new StringDoubleKey("StarKebab", "Western Food", "Expensive", "Far", "High"));
        Record r32 = new OtherElements(new StringDoubleKey("O'ZBEK", "Western Food", "Expensive", "Far", "High"));
        Record r33 = new OtherElements(new StringDoubleKey("Mr Pizza", "Western Food", "Expensive", "Close", "High"));
        Record r34 = new OtherElements(new StringDoubleKey("issac toast", "Western Food", "Cheap", "Close", "High"));
        Record r35 = new OtherElements(new StringDoubleKey("yoogane", "Korean Food", "Expensive", "Close", "Low"));
        Record r36 = new OtherElements(
                new StringDoubleKey("cabare restaurant", "Western Food", "Cheap", "Close", "High"));
        Record r37 = new OtherElements(new StringDoubleKey("tomato dosirak", "Korean Food", "Cheap", "Close", "High"));
        Record r38 = new OtherElements(new StringDoubleKey("hansot dosirak", "Korean Food", "Cheap", "Close", "High"));
        Record r39 = new OtherElements(new StringDoubleKey("Pizza School", "Western Food", "Cheap", "Close", "High"));
        Record r40 = new OtherElements(new StringDoubleKey("Anne's Table", "Western Food", "Cheap", "Close", "High"));
        Record r41 = new OtherElements(
                new StringDoubleKey("theBBap house", "Korean Food", "Expensive", "Close", "High"));
        Record r42 = new OtherElements(new StringDoubleKey("kimbbap heaven", "Korean Food", "Cheap", "Close", "High"));
        Record r43 = new OtherElements(new StringDoubleKey("hongdangmu", "Korean Food", "Cheap", "Close", "High"));
        Record r44 = new OtherElements(new StringDoubleKey("handduk", "Korean Food", "Expensive", "Far", "High"));
        Record r45 = new OtherElements(new StringDoubleKey("milsup", "Korean Food", "Cheap", "Far", "High"));
        Record r46 = new OtherElements(new StringDoubleKey("yuwon chicken", "Western Food", "Cheap", "Close", "High"));

        db[0] = r1; // add records at db
        db[1] = r2;
        db[2] = r3;
        db[3] = r4;
        db[4] = r5;
        db[5] = r6;
        db[6] = r7;
        db[7] = r8;
        db[8] = r9;
        db[9] = r10;
        db[10] = r11;
        db[11] = r12;
        db[12] = r13;
        db[13] = r14;
        db[14] = r15;
        db[15] = r16;
        db[16] = r17;
        db[17] = r18;
        db[18] = r19;
        db[19] = r20;
        db[20] = r21;
        db[21] = r22;
        db[22] = r23;
        db[23] = r24;
        db[24] = r25;
        db[25] = r26;
        db[26] = r27;
        db[27] = r28;
        db[28] = r29;
        db[29] = r30;
        db[30] = r31;
        db[31] = r32;
        db[32] = r33;
        db[33] = r34;
        db[34] = r35;
        db[35] = r36;
        db[36] = r37;
        db[37] = r38;
        db[38] = r39;
        db[39] = r40;
        db[40] = r41;
        db[41] = r42;
        db[42] = r43;
        db[43] = r44;
        db[44] = r45;
        db[45] = r46;

        db = shuffle(db); // shuffling db list

        System.out.println(
                "Welcome to Food Decision Maker!! \n\nThis programm will help you to choose where to eat today.\n\n 1. Run Decision Rullet\n\n 2. Run Decision Navigator\n\n 3. Quit");

        System.out.println("Write number to do : (write 1, 2, 3) ");
        try {
            int response = 0;
            response = scanner.nextInt();

            if (response == 1) { // Decision Rullet
                DecisionRullet();
                    }
                    if (response == 2) {//Decision Navigator

                        System.out.println("Enter your preference (Food type, price, distance, rating) : (write f, p, d, r) ");
                        Scanner scanner1 = new Scanner(System.in);
                        try{
                            char navi_response = scanner1.next().charAt(0);
                            if (navi_response != 'f' && navi_response != 'p' && navi_response != 'd' && navi_response != 'r') {scanner1.close(); throw new Exception();}
                            if (navi_response == 'f') {DecisionNavigator_f(db);} //food type (Western food, Korean food)
                            else if(navi_response == 'p') {DecisionNavigator_p(db);} //price (Cheap, Expensive)
                            else if(navi_response == 'd') {DecisionNavigator_d(db);} //distance (Close, Far)
                            else if(navi_response == 'r') {DecisionNavigator_r(db);} //rating (Low, High)
                                
                        } catch(Exception e) {
                            System.out.println("Something has wrong, Bye!");
                            
                        }  
                        scanner1.close();
                    } //if end
                if (response == 3) {
                    System.out.println("Thank You!"); scanner.close(); System.exit(1);
                } 
                
                
            } catch(Exception e){
                System.out.println("Something has wrong, bye!");
            }
        
    }
}