public class Solution {
    public boolean isPalindrome(int x) {
        if( x < 0)
            return false;
            
        int lens = 0;
        List<Integer> list = new ArrayList<Integer>();
        while(x != 0) {
            list.add(x%10);
            x = x / 10;
            lens++;
        }
        int i = 0;
        while(i < lens/2) {
            if(list.get(i) != list.get(lens-i-1))
                return false;
            i++;
        }
        
        return true;
    }
}