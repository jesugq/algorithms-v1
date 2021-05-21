import java.util.Set;
import java.util.HashMap;
import java.util.Map.Entry;
import java.util.ArrayList;

public class Solution {
    public String shortestCompletingWord(String licensePlate, String[] words) {
        HashMap<Character, Integer> licenseCharacterInstances = extractCharactersFromString(licensePlate);
        HashMap<Character, Integer> wordCharacterInstances = new HashMap<Character, Integer>();
        ArrayList<String> answers = new ArrayList<String>();
        int wordsLength = words.length;
        String currentWord;
        
        for (int i = 0; i < wordsLength; i ++) {
            currentWord = words[i];
            wordCharacterInstances = extractCharactersFromString(currentWord);
            if (hashMapEntriesMatchFromIn(licenseCharacterInstances, wordCharacterInstances)) {
                answers.add(currentWord);
            }
        }
        
        if (answers.size() == 0) {
            return "";
        } else {
            return findShortestWord(answers);
        }
    }

    private HashMap<Character, Integer> extractCharactersFromString(String string) {
        HashMap<Character, Integer> characterInstances = new HashMap<Character, Integer>();
        String lowercaseString = string.toLowerCase();
        int stringLength = string.length();
        char character;
        int instances;

        for (int i = 0; i < stringLength; i ++) {
            character = lowercaseString.charAt(i);
            instances = 0;
            if (Character.isAlphabetic(character)) {
                if (!characterInstances.containsKey(character)) {
                    characterInstances.put(character, 0);
                }
                instances = characterInstances.get(character) + 1;
                characterInstances.put(character, instances);
            }
        }
        return characterInstances;
    }

    private boolean hashMapEntriesMatchFromIn(HashMap<Character, Integer> target, HashMap<Character, Integer> subject) {
        Set<Entry<Character, Integer>> set = target.entrySet();
        char targetKey;
        int targetValue;
        int subjectValue;

        for (Entry<Character, Integer> entry : set) {
            targetKey = entry.getKey();
            targetValue = entry.getValue();
            subjectValue = subject.getOrDefault(targetKey, -1);
            if (subjectValue < targetValue) {
                return false;
            }
        }
        return true;
    }

    private String findShortestWord(ArrayList<String> words) {
        String currentWord;
        int currentWordLength;
        int shortestLength = Integer.MAX_VALUE;
        int wordsLength = words.size();
        
        for (int i = 0; i < wordsLength; i ++) {
            currentWord = words.get(i);
            currentWordLength = currentWord.length();
            if (currentWordLength < shortestLength) {
                shortestLength = currentWordLength;
            }
        }

        for (int i = 0; i < wordsLength; i ++) {
            currentWord = words.get(i);
            currentWordLength = currentWord.length();
            if (currentWordLength == shortestLength) {
                return currentWord;
            }
        }
        return "";
    }
}

// import java.util.LinkedList;

// public class Main {
//     private static LinkedList<String> parameterA = new LinkedList<String>();
//     private static LinkedList<String[]> parameterB = new LinkedList<String[]>();
//     private static LinkedList<String> parameterC = new LinkedList<String>();

//     public static void main(String args[]) {
//         createTestSuite();
//         testSolutionClass();
//     }

//     private static void createTestSuite() {     
//         parameterA.add("1s3 PSt");
//         parameterB.add(new String[]{"step","steps","stripe","stepple"});
//         parameterC.add("steps");

//         parameterA.add("1s3 456");
//         parameterB.add(new String[]{"looks","pest","stew","show"});
//         parameterC.add("pest");

//         parameterA.add("Ah71752");
//         parameterB.add(new String[]{"suggest","letter","of","husband","easy","education","drug","prevent","writer","old"});
//         parameterC.add("husband");

//         parameterA.add("OgEu755");
//         parameterB.add(new String[]{"enough","these","play","wide","wonder","box","arrive","money","tax","thus"});
//         parameterC.add("enough");

//         parameterA.add("iMSlpe4");
//         parameterB.add(new String[]{"claim","consumer","student","camera","public","never","wonder","simple","thought","use"});
//         parameterC.add("simple");

//         parameterA.add("GrC8950");
//         parameterB.add(new String[]{"measure","other","every","base","according","level","meeting","none","marriage","rest"});
//         parameterC.add("according");
//     }

//     private static void testSolutionClass() {
//         Solution solution = new Solution();
//         String licensePlate;
//         String[] words;
//         String expected;
//         String actual;

//         while(true) {
//             licensePlate = parameterA.poll();
//             words = parameterB.poll();
//             expected = parameterC.poll();
//             if (licensePlate == null || words == null || expected == null) {
//                 return;
//             }
            
//             actual = solution.shortestCompletingWord(licensePlate, words);
//             System.out.format("%s %s %s\n", actual.equals(expected), actual, expected);
//         }
//     }
// }