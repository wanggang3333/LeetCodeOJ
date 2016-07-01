public class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> ans = new ArrayList<Integer>();
        if(rowIndex < 0)
            return ans;
        
        ans.add(1);
        for(int i = 1; i <= rowIndex; i++) {
            for(int j = ans.size() - 1; j >= 1; j--) {
                ans.set(j,ans.get(j)+ans.get(j-1));
            }
            ans.add(1);
        }
        return ans;
        
    }
}