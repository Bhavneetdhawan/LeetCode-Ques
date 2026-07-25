int maxIceCream(int* costs, int costsSize, int coins) {
    int maxCost = 0;

    // Find maximum cost
    for (int i = 0; i < costsSize; i++) {
        if (costs[i] > maxCost)
            maxCost = costs[i];
    }

    // Frequency array
    int freq[maxCost + 1];
    for (int i = 0; i <= maxCost; i++)
        freq[i] = 0;

    for (int i = 0; i < costsSize; i++)
        freq[costs[i]]++;

    int count = 0;

    // Buy cheapest bars first
    for (int cost = 1; cost <= maxCost; cost++) {
        if (freq[cost] == 0)
            continue;

        int canBuy = coins / cost;

        if (canBuy >= freq[cost]) {
            count += freq[cost];
            coins -= freq[cost] * cost;
        } else {
            count += canBuy;
            break;
        }
    }

    return count;
}