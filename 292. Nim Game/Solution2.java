//�ҹ���
// n =1,2,3 Ϊ true,n = 4 ʱ��Ϊfalse
// n = 5,6,7ʱ��ͨ����1~3�ţ�ת��Ϊn = 4���������Ϊ true��
// n = 8 ʱ���������ü��ţ����ֲ�ȡ��Ӧ��ʩ��ת��Ϊn = 4�������Ϊfalse

public class Solution {
    public boolean canWinNim(int n) {
        return n%4 > 0;
    }
}