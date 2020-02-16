public class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> set = new HashSet<Integer>();
        while(!set.contains(n)) {
            set.add(n);
            n = getSquSum(n);
            if(n == 1) {
                return true;
            }
        }
        return false;
    }
    public int getSquSum(int n) {
        int sum = 0;
        int t;
        while(n != 0){
           t = n % 10;
           sum += t * t;
           n = n / 10;
        }
        return sum;
    }
}