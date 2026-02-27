// Inputs
// 5
// 0 1 0 3 12

// O/P: 1 3 12 0 0 

import java.util.*;

public class L283 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] nums = new int[n];

        for(int i = 0; i < n; i++){
            nums[i] = sc.nextInt();
        }

        moveZeroes(nums);

        for(int i = 0; i < n; i++){
            System.out.print(nums[i] + " ");
        }
    }

    public static void moveZeroes(int[] nums) {
        int i = 0;

        for(int j = 0; j < nums.length; j++){
            if(nums[j] != 0){
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                i++;
            }
        }
    }
}