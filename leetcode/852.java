class Solution {
    public static final int NOT_MOUNTAIN = -1;

    public int peakIndexInMountainArray(int[] arr) {
        if (arrayIsNotMountain(arr)) {
            return NOT_MOUNTAIN;
        }
        return peakIndexInMountain(arr);
    }

    private boolean arrayIsNotMountain(int[] mountain) {
        return mountain.length < 3;
    }

    private int peakIndexInMountain(int[] mountain) {
        int peakValue = Integer.MIN_VALUE;
        int peakIndex = -1;

        for (int i = 0; i < mountain.length; i ++) {
            if (mountain[i] > peakValue) {
                peakValue = mountain[i];
                peakIndex = i;
            }
        }
        return peakIndex;
    }
}
