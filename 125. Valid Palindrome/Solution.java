public class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        int lens = s.length();
        if (lens < 2)
            return true;
        int i = 0;
        Stack<Character> stack = new Stack<Character>();
        while(i < lens/2) {
            stack.push(s.charAt(i));
            i++;
        }
        if(lens%2 == 1)
            i++;
        
        while(i < lens) {
            if(stack.isEmpty())
                return false;
            char c = stack.pop();
            if(s.charAt(i) != c) {
                return false;
            } else {
                i++;
            }
        }
        return true;
    }
}