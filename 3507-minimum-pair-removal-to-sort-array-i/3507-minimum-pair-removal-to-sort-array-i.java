class Solution {
    public int minimumPairRemoval(int[] nums) {
        int operations = 0;

        while (!isNonDecreasing(nums)) {

            int minIndex = 0;
            int minSum = nums[0] + nums[1];

            for (int i = 1; i < nums.length - 1; i++) {
                int sum = nums[i] + nums[i + 1];
                if (sum < minSum) {
                    minSum = sum;
                    minIndex = i;
                }
            }

            int[] newNums = new int[nums.length - 1];
            int j = 0;

            for (int i = 0; i < nums.length; i++) {
                if (i == minIndex) {
                    newNums[j++] = nums[i] + nums[i + 1];
                    i++;
                } else {
                    newNums[j++] = nums[i];
                }
            }

            nums = newNums;
            operations++;
        }

        return operations;
    }

    private boolean isNonDecreasing(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < nums[i - 1]) {
                return false;
            }
        }
        return true;
    }
}