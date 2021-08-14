public class RTSlabsCodeExercises {

    // O(arr.length) time complexity - O(1) space complexity
    public static String elementsAboveAndBelowN(int[] arr, int n) {
        int above = 0;
        int below = 0;
        
        for (int num : arr) {
            if (num > n) {
                above++;
            } else if (num < n) {
                below++;
            }
        }

        return "above: " + above + ", below: " + below;
    }

    // O(s.length()) time complexity and space complexity
    public static String rotateByN(String s, int n) {

        int rotation = n % s.length();

        if (rotation < 0) rotation += s.length();

        int overFlowPoint = s.length() - rotation;

        String rotatedString = s.substring(overFlowPoint) + s.substring(0, overFlowPoint);

        return rotatedString;

    }

    public static void main(String[] args) {
        int[] arr = {46,9,-23,0,-45,88,12};
        System.out.println(elementsAboveAndBelowN(arr, 0));

        System.out.println(rotateByN("Pittsburgh Steelers", 6));
    }

}