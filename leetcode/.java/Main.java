import java.util.Arrays;
class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] unsortedNumbers = {8, 1, 2, 2, 3};
        int[] smallerNumbers = solution.smallerNumbersThanCurrent(unsortedNumbers);
        System.out.println(Arrays.toString(smallerNumbers));
    }
}