public class Solution {
    public String convertToTitle(int n) {
        char[] cha = new char[]{'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
        String s = "";
        while(n!= 0) {
            int t = (n-1) % 26;
            s = cha[t]+s;
            n = (n-1) / 26;
        }
        return s;
    }
}