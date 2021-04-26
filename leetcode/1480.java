import java.util.Queue;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.NoSuchElementException;

class Solution {
    public int[] runningSum(int[] nums) {
        int accumulator = 0;
        int arrayLength = nums.length;
        int[] runningSumArray = new int[arrayLength];

        for (int i = 0; i < arrayLength; i ++) {
            accumulator += nums[i];
            runningSumArray[i] = accumulator;
        }

        return runningSumArray;
    }
}

class Test {
    final private static int exampleCount = 3;

    public static void main(String[] args) {
        Solution solution = new Solution();
        Queue<int[]> answers = getAnswers();
        Queue<int[]> tests = getTests();
        
        for (int i = 0; i < exampleCount; i ++) {
            int[] answer = {};
            int[] test = {};
            try {
                answer = answers.poll();
                test = tests.poll();
            } catch (NoSuchElementException exception) {
                System.out.println("Answers and Tests Queues are not of equal size.");
                System.exit(0);
            }

            int[] execution = solution.runningSum(test);
            
            System.out.printf(
                "%5b \t %s | %s\n",
                Arrays.equals(execution, answer),
                Arrays.toString(execution),
                Arrays.toString(answer)
            );
        }
    }

    private static Queue<int[]> getAnswers() {
        Queue<int[]> answers = new LinkedList<int[]>();
        answers.add(new int[]{1,3,6,10});
        answers.add(new int[]{1,2,3,4,5});
        answers.add(new int[]{3,4,6,16,17});
        return answers;
    }

    private static Queue<int[]> getTests() {
        Queue<int[]> tests = new LinkedList<int[]>();
        tests.add(new int[]{1,2,3,4});
        tests.add(new int[]{1,1,1,1,1});
        tests.add(new int[]{3,1,2,10,1});
        return tests;
    }
}