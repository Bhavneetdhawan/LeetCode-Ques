class Solution {
    public int uniqueMorseRepresentations(String[] words) {

        String[] code = {
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        };

        String[] arr = new String[words.length];
        int count = 0;

        for (int i = 0; i < words.length; i++) {

            String morse = "";

            for (char ch : words[i].toCharArray()) {
                morse += code[ch - 'a'];
            }

            boolean found = false;

            for (int j = 0; j < count; j++) {
                if (arr[j].equals(morse)) {
                    found = true;
                    break;
                }
            }

            if (!found) {
                arr[count] = morse;
                count++;
            }
        }

        return count;
    }
}