//counting readable alphabet(Capital)

class Main9_2 {
  
    public static int[] get_word_count(String word) {
            int[] word_count = new int[26];
              // fill here!
              for(int k = 0; k < 26; k++){
                word_count[k] = 0;
              }
              String words = word.toUpperCase();
              for(int j = 0; j < words.length(); j++) {
                  int todigit = (char)(words.charAt(j)) - 'A';
                  if(todigit < 0 || todigit > 25) {
                    System.out.println("Not lowercase / uppercase");
                    
                  }
                  else {
                    word_count[todigit]++;
                    
                  }
                
              }
              return word_count;
      }
      
      public static void main(String[] args) {
          int[] word_count = get_word_count("AB-++d");
          for (int i = 0; i < word_count.length; i++)
              System.out.print((char) ('A' + i) + ":" + word_count[i] + " ");
      //A:1 B:1 C:0 D:1 E:0 F:0 G:0 H:0 I:0 J:0 K:0 L:0 M:0 N:0 O:0 P:0 Q:0 R:0 S:0 T:0 U:0 V:0 W:0 X:0 Y:0 Z:0 
  
      }
  }