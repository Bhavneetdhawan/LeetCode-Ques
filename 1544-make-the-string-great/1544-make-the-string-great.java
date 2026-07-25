class Solution {
    public String makeGood(String s) {

        while (true) {
            boolean found = false;

            for (int i = 0; i < s.length() - 1; i++) {

                if (Math.abs(s.charAt(i) - s.charAt(i + 1)) == 32) {
                    s = s.substring(0, i) + s.substring(i + 2);
                    found = true;
                    break; // Start checking again from the beginning
                }
            }

            if (!found)
                break;
        }

        return s;
    }
}