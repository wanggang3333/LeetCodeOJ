public class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        ArrayList<Integer> temp = new ArrayList<Integer>();
        
        if(numRows == 0)
            return res;

        for(int i = 0; i < numRows; ++i) {
            ArrayList<Integer> item = new ArrayList<Integer>();
            item.add(1);
            for(int j = 0; j < temp.size() - 1; ++j) {
                int sum = temp.get(j) + temp.get(j+1);
                item.add(sum);
            }
            if(i >= 1)
                item.add(1);
                
            res.add(item);
            temp = item;
        }
        return res;
    }
}