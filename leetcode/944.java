class Solution {
    public int minDeletionSize(String[] A) {
        return numberOfColumnsUnordered(A);
    }

    private int numberOfColumnsUnordered(String[] strings) {       
        int columnsUnordered = 0;
        int stringLength = getStringLength(strings);

        for (int i = 0; i < stringLength; i ++) {
            if (columnIsUnordered(strings, i)) {
                columnsUnordered ++;
            }
        }
        return columnsUnordered;
    }

    private int getStringLength(String[] strings) {
        return strings[0].length();
    }

    private boolean columnIsUnordered(String[] strings, int column) {
        char currentCharacter = Character.MIN_VALUE;
        char previousCharacter = Character.MIN_VALUE;

        for (int i = 0; i < strings.length; i ++) {
            currentCharacter = strings[i].charAt(column);
            if (currentCharacter < previousCharacter) {
                return true;
            }
            previousCharacter = currentCharacter;
        }
        return false;
    }
}