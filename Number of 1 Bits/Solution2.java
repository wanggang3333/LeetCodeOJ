//�Ƚ�����Ľⷨ���Խ�ѭ���������ٵ���1�ĸ���һ����
//���õ����ʾ���n��1֮��n���λ��1֮�󣨰����䱾��������bits��ת��
//http://www.danielbit.com/blog/puzzle/leetcode/leetcode-number-of-1-bits
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        if(n == 0)
            return 0;
        int i = 0;
        while(n != 0) {
            n = n & (n-1);
            i++;
        }
        return i;
    }
}