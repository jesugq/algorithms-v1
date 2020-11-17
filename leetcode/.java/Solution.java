// commonNumbers    [8, 1, 2, 2, 3]

// sortedNumbers    [1, 2, 2, 3, 8]
// repeatedNumbers  [0, 1, 1, 0, 0]
// smallerNumbers   [0, 1, 1, 3, 4]

// smallerNumbers   Highest Index on SortedNumbers - repeatedNumbers[i]
// smallerNumbers   [0-0, 1-1, 1-1, 3-0, 8-0]

// smallerNumbers   Lowest Index on SortedNumbers
// smallerNumbers   [0, 1, 1, 3, 4]
import java.util.Arrays;
class Solution {
    public static final int NO_INSTANCES = 0;

    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] sortedNumbers = getSortedNumbers(nums);
        return getSmallerNumbers(nums, sortedNumbers);
    }

    public int[] getSortedNumbers(int[] commonNumbers) {
        int[] sortedNumbers = commonNumbers.clone();
        Arrays.sort(sortedNumbers);
        return sortedNumbers;
    }

    public int[] getSmallerNumbers(int[] commonNumbers, int[] sortedNumbers) {
        int[] smallerNumbers = new int[commonNumbers.length];
        for (int i = 0; i < commonNumbers.length; i ++){
            try {
                smallerNumbers[i] = lowestIndexOfNumber(commonNumbers[i], sortedNumbers);
            } catch (NoSuchFieldException notFoundException) {
                smallerNumbers[i] = NO_INSTANCES;
            }
        }
        return smallerNumbers;
    }

    public int lowestIndexOfNumber(int targetNumber, int[] sortedNumbers) throws NoSuchFieldException {
        for (int i = 0; i < sortedNumbers.length; i++) {
            if (sortedNumbers[i] == targetNumber)
                return i;
        }
        throw new NoSuchFieldException("The lowest index of the number was not found.");
    }
}