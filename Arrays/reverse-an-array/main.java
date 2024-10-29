// Java Program to reverse an array using Two Pointers

import java.util.Arrays;

class GfG {
    
    // function to reverse an array
    static void reverseArray(int[] arr) {
        
        // Initialize left to the beginning and right to the end
        int left = 0, right = arr.length - 1;

        // Iterate till left is less than right
        while (left < right) {
            
            // Swap the elements at left and right position
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;

            // Increment the left pointer
            left++;

            // Decrement the right pointer
            right--;
        }
    }

    public static void main(String[] args) {
        int[] arr = { 1, 4, 3, 2, 6, 5 };

        reverseArray(arr);

        for (int i = 0; i < arr.length; i++) 
            System.out.print(arr[i] + " ");
    }
}
