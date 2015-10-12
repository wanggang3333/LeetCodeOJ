public class Solution {
    public String getPermutation(int n, int k) {
        int[] fac = new int[n];
        ArrayList<Integer> nums = new ArrayList<Integer>();
        fac[0] = 1; nums.add(1);
        for (int i = 1;i < n; ++i) {
            fac[i] = i * fac[i-1];
            nums.add(i+1);
        }
        String s = "";
        int con = 0;
        for(int j = n-1; j >= 0; --j) {
            con = (k-1) / fac[j];
            s += nums.get(con);
            k = k -con * fac[j]; 
            nums.remove(con);
            
        }
        return s;
    }
    
}