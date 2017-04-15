public class Solution {
    public String findLongestWord(String s, List<String> d) {
        //redefine comparator by length, if same length then by alpha
        //sort list use Collections.sort()
        Comparator<String> comp = new Comparator<String>(){
            @Override
            public int compare(String str1, String str2){
                if(str1.length() != str2.length()){
                    return str2.length()-str1.length(); //s2 > s1 -> return + -> s1>s2 -> s2 in front of s1 in list
                }else{
                    return str1.compareTo(str2); // s2-a s1-z -> return + -> s1>s2 -> s2 in front of s1 in list
                }
            }
        };
        Collections.sort(d, comp);
        
        //now the first element in list that satisty is the one we want to return
        //use two pointers to determine if the word is in String s
        //s = "abpcplea" w = "apple"
        //(i->a)bpcplea
        //(j->a)pple   i++ j++
        //a(i->b)pcplea
        //a(j->p)ple  i++
        //ab(i->p)cplea  
        //a(j->p)ple    i++ j++
        //return when j=w.length
        for(String w : d){
            if(w.length()>s.length()) continue;
            int i=0;
            int j=0;
            while(i<s.length() && j<w.length()){
                if(s.charAt(i)==w.charAt(j)){
                    j++;
                }
                i++;
            }
            if(j==w.length()) return w;
        }
        return "";
    }
}
