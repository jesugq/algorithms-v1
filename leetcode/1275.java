public class Solution {
    private static final int BOARD_SIZE = 3;
    private static final int MOVE_ROW = 0;
    private static final int MOVE_COL = 1;
    
    public String tictactoe(int[][] moves) {
        int currentPlayerIndex = 0;
        
        while (currentPlayerIndex <= 1) {
            String currentPlayerName = currentPlayerIndex == 0 ? "A" : "B";
            int currentPlayerLeftDiagonalsCount = 0;
            int currentPlayerRightDiagonalsCount = 0;
            int[] currentPlayerRowsMarked = new int[BOARD_SIZE];
            int[] currentPlayerColsMarked = new int[BOARD_SIZE];

            for (int i = currentPlayerIndex; i < moves.length; i += 2) {
                if (moves[i][MOVE_ROW] == moves[i][MOVE_COL])
                    currentPlayerLeftDiagonalsCount ++;
                if (moves[i][MOVE_ROW] == BOARD_SIZE - 1 - moves[i][MOVE_COL])
                    currentPlayerRightDiagonalsCount ++;
                currentPlayerRowsMarked[moves[i][MOVE_ROW]] ++;
                currentPlayerColsMarked[moves[i][MOVE_COL]] ++;
            }

            if (currentPlayerLeftDiagonalsCount == BOARD_SIZE) {
                return currentPlayerName;
            }
            if (currentPlayerRightDiagonalsCount == BOARD_SIZE) {
                return currentPlayerName;
            }
            for (int i = 0; i < BOARD_SIZE; i ++) {
                if (currentPlayerRowsMarked[i] == BOARD_SIZE) {
                    return currentPlayerName;
                }
                if (currentPlayerColsMarked[i] == BOARD_SIZE) {
                    return currentPlayerName;
                }
            }
            
            currentPlayerIndex += 1;
        }

        return moves.length == BOARD_SIZE * BOARD_SIZE ? "Draw" : "Pending";
    }
}

// public class Main {
//     public static void main(String[] args) {
//         LinkedList<int[][]> moves = getMoves();
//         LinkedList<String> correct = getCorrect();
//         Solution solution = new Solution();
        
//         int moveLength = moves.size();
//         int correctLength = correct.size();
        
//         if (moveLength != correctLength){
//             System.out.println("Unequal amount of inputs and outputs");
//             return;
//         }
        
//         for (int i = 0; i < correctLength; i ++) {
//             int[][] movesItem = moves.poll();
//             String correctItem = correct.poll();
//             String solutionItem = solution.tictactoe(movesItem);
//             boolean isRight = correctItem.equals(solutionItem);

//             System.out.printf("%5b — Solution:%7s Correct:%7s\n", isRight, solutionItem, correctItem);
//         }
//     }

//     private static LinkedList<int[][]> getMoves(){
//         LinkedList<int[][]> moves = new LinkedList<int[][]>();
//         moves.add(new int[][]{{0,0},{2,0},{1,1},{2,1},{2,2}});
//         moves.add(new int[][]{{0,0},{1,1},{0,1},{0,2},{1,0},{2,0}});
//         moves.add(new int[][]{{0,0},{1,1},{2,0},{1,0},{1,2},{2,1},{0,1},{0,2},{2,2}});
//         moves.add(new int[][]{{0,0},{1,1}});
//         return moves;
//     }

//     private static LinkedList<String> getCorrect(){
//         LinkedList<String> correct = new LinkedList<String>();
//         correct.add("A");
//         correct.add("B");
//         correct.add("Draw");
//         correct.add("Pending");
//         return correct;
//     }
// }