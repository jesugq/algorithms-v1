import java.util.ArrayList;
import java.util.Collections;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Solution {
    public int findContentChildren(int[] g, int[] s) {
        if (g == null | s == null) {
            return 0;
        } 

        ArrayList<Integer> greedFactor = IntStream.of(g).boxed().collect(Collectors.toCollection(ArrayList::new));
        ArrayList<Integer> cookieSize = IntStream.of(s).boxed().collect(Collectors.toCollection(ArrayList::new));
        int currentGreed, currentCookie, contentChildren, current;
        
        Collections.sort(greedFactor);
        Collections.sort(cookieSize);
        Collections.reverse(greedFactor);
        Collections.reverse(cookieSize);
        contentChildren = 0;
        current = 0;

        while (!greedFactor.isEmpty() && !cookieSize.isEmpty()) {
            currentGreed = greedFactor.remove(current);
            currentCookie = cookieSize.get(current);
            if (currentGreed <= currentCookie) {
                cookieSize.remove(current);
                contentChildren ++;
            }
        }
        return contentChildren;
    }
}

// import java.util.LinkedList;

// public class Main {
//     private static LinkedList<int[]> greedFactorList = new LinkedList<int[]>();
//     private static LinkedList<int[]> cookieSizeList = new LinkedList<int[]>();
//     private static LinkedList<Integer> contentChildrenList = new LinkedList<Integer>();

//     public static void main(String[] args) {
//         createTestSuite();
//         testSolutionClass();
//     }

//     private static void createTestSuite() {
//         greedFactorList.add(new int[]{1, 2, 3});
//         cookieSizeList.add(new int[]{1, 1});
//         contentChildrenList.add(1);

//         greedFactorList.add(new int[]{1, 2});
//         cookieSizeList.add(new int[]{1, 2, 3});
//         contentChildrenList.add(2);
//     }

//     private static void testSolutionClass() {
//         Solution solution = new Solution();
//         int[] greedFactor, cookieSize;
//         int actual, expected;
        
//         while (greedFactorList.size() != 0 && cookieSizeList.size() != 0 && contentChildrenList.size() != 0) {
//             greedFactor = greedFactorList.poll();
//             cookieSize = cookieSizeList.poll();
//             actual = contentChildrenList.poll();
//             expected = solution.findContentChildren(greedFactor, cookieSize);

//             System.out.printf("%b — %d == %d\n", actual == expected, actual, expected);
//         }
//     }
// }