//找规律
// n =1,2,3 为 true,n = 4 时，为false
// n = 5,6,7时，通过拿1~3颗，转换为n = 4的情况，即为 true；
// n = 8 时，无论先拿几颗，对手采取相应措施，转换为n = 4的情况，为false

public class Solution {
    public boolean canWinNim(int n) {
        return n%4 > 0;
    }
}