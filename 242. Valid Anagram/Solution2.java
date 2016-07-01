public class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) {
            return false;
        }

        int[] sum = new int[26];
        for(int i = 0; i < s.length(); ++i) {
            sum[s.charAt(i)-'a']++;
        }
        for(int j = 0; j < t.length(); ++j) {
            --sum[t.charAt(j)-'a'];
            if(sum[t.charAt(j)-'a'] < 0) {
                return false;
            }
        }
        
        return true;
    }
}