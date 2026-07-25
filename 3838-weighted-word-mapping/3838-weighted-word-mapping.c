char* mapWordWeights(char** words, int wordsSize, int* weights, int weightsSize) {
    char* result = (char*)malloc((wordsSize + 1) * sizeof(char));

    for (int i = 0; i < wordsSize; i++) {
        int sum = 0;

        // Calculate weight of current word
        for (int j = 0; words[i][j] != '\0'; j++) {
            sum += weights[words[i][j] - 'a'];
        }

        // Weight modulo 26
        int mod = sum % 26;

        // Reverse mapping:
        // 0 -> z, 1 -> y, ..., 25 -> a
        result[i] = 'z' - mod;
    }

    result[wordsSize] = '\0';
    return result;
}