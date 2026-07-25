class Solution {
    public int balancedStringSplit(String s) {
        int balance = 0;
        int count = 0;

        for (char ch : s.toCharArray()) {
            if (ch == 'R') {
                balance++;
            } else {
                balance--;
            }

            // If number of L and R are equal
            if (balance == 0) {
                count++;
            }
        }

        return count;
    }
}