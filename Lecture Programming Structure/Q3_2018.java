
public class Q3_2018 {
	public static int search(int key, int[] a) {
		return search(key, a, 0, a.length);
	}
	public static int search(int key, int[] a, int lo, int hi) {
		//fill here!
		lo = 0;
		hi = a.length;
		for(int i = 0; i < hi; i++) {
			if (a[i] == key) {
				break;
			}
			else {
				lo++;
			}
		}
		return lo;
	}
	class Q3answer {

		public static int search(char key, String a, int lo, int hi)

		{

			if (hi <= lo) return -1;

		   int mid = lo + (hi - lo) / 2;

		   int cmp = a.charAt(mid) == key ? 0 : (a.charAt(mid) < key ? -1 : 1); 

		   if      (cmp > 0) return search(key, a, lo, mid);

		   else if (cmp < 0) return search(key, a, mid+1, hi);

		   else              return mid;

		}

		public static int findChar(char c, String s) { 

			return search(c, s, 0, s.length()); 

		}

	}
	
	public static void main(String[] args) {
		int[] arr = new int[4];
		arr[0] = 1; arr[1] = 2; arr[2] = 3; arr[3] = 4;
		System.out.println(search(3,arr)); //should print 2
	}
}
