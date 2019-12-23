interface Key1 { public boolean equals(Key1 m); }
interface Record1 { public Key1 keyOf(); }
class DataBase {
	private Record1[] base;
	public DataBase(int initial_size) {
		if (initial_size < 0) initial_size = 1;
		base = new Record1[initial_size];
	}
	public Record1 find(Key1 k) {
		for (int i = 0; i < base.length; i++) 
			if (base[i] != null && base[i].keyOf().equals(k)) 
				return base[i];
		return null;
	}
	public boolean insert(Record1 r) {
		int i; 
		if (find(r.keyOf()) != null) return false;
		for (i = 0; i < base.length; i++) 
			if (base[i] == null) {
				base[i] = r; return true; 
			}
		Record1[] base_new = new Record1[base.length * 2];
		for (i = 0; i < base.length; i++)  
			base_new[i] = base[i];
		base = base_new; 
		base[i] = r;
		return true; 
	}
	public boolean delete(Key1 k) {
		for (int i = 0; i < base.length; i++) 
			if (base[i] != null && base[i].keyOf().equals(k)) {
				base[i] = null; return true;
			}
		return false;
	}	
}
class StringDoubleKey1 implements Key1 { 
	private String id_str; 
	private double id_double; 
		// fill here!
	public StringDoubleKey1(String s, double i) {id_str = s; id_double = i;}
	public double getDouble() { return id_double; }
	public String getString() { return id_str;}
	public boolean equals(Key1 m) {
		return id_double == ((StringDoubleKey1)m).getDouble() && id_str == ((StringDoubleKey1)m).getString();
	}
	public String toString() { return id_str + id_double; }
}
class Class implements Record1 {
	 private StringDoubleKey1 class_id;
	 private String name; 
		 // fill here!
	 public Class(StringDoubleKey1 k, String s) {class_id = k; name = s;}
	 public Key1 keyOf() {
		 return class_id;
	 }
	 public String toString() {
		 return class_id.toString() + " " + name;
	 }
} 
public class Q5 {
	public static void main(String[] args) {
		DataBase db = new DataBase(100) ;
		Record1 r1 = new Class(new StringDoubleKey1("CS", 2016), "Programming"); 
		Record1 r2 = new Class(new StringDoubleKey1("CS", 664.18), "Security"); 
		db.insert(r1); db.insert(r2); db.delete(r1.keyOf());
		Record1[] ab = new Record1[100];
		ab[0] = r1; ab[1] = r2;
		System.out.println(ab);
		System.out.println(ab[0]);
		System.out.println(ab[1]);
		System.out.println(db.find(r1.keyOf())); // null
		System.out.println(db.find(r2.keyOf())); // CS664.18 Security
	}
}
