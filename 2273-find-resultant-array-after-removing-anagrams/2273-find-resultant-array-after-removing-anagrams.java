class Solution {
    public List<String> removeAnagrams(String[] words) {
        List<String> ans = new ArrayList<>();
        String prev = "";

        for (String word : words) {
            char[] ch = word.toCharArray();
            Arrays.sort(ch);
            String sorted = new String(ch);

            if (!sorted.equals(prev)) {
                ans.add(word);
                prev = sorted;
            }
        }

        return ans;
    }
}