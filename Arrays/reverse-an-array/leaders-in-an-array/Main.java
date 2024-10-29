import java.util.ArrayList;

class Main {

    // Function to find the leaders in an array
    static ArrayList<Integer> leaders(int[] arr) {
        ArrayList<Integer> result = new ArrayList<>();
        int n = arr.length;
        
        for (int i = 0; i < n; i++) {
            int j;
          
            // Check elements to the right
            for (j = i + 1; j < n; j++) {
              
                // If a larger element is found
                if (arr[i] < arr[j])
                    break;
            }
            
            // If no larger element was found
            if (j == n)
                result.add(arr[i]);
        }
        
        return result;
    }

    public static void main(String[] args) {
        int[] arr = { 16, 17, 4, 3, 5, 2 };
        ArrayList<Integer> result = leaders(arr);
        
        for (int res : result) {
            System.out.print(res + " ");
        }
        System.out.println();
    }
}
