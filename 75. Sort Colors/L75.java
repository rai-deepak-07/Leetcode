// Input:
// 6
// 2 0 2 1 1 0

// Output:
// 0 0 1 1 2 2 

import java.util.*;

public class L75 {

    static void swap(int[] nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    static void sortColors(int[] nums){
        int low = 0, mid = 0;
        int high = nums.length - 1;

        while(mid <= high){
            if(nums[mid] == 0){
                swap(nums, low, mid);
                low++;
                mid++;
            }
            else if(nums[mid] == 1){
                mid++;
            }
            else{
                swap(nums, mid, high);
                high--;
            }
        }
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] nums = new int[n];

        for(int i = 0; i < n; i++){
            nums[i] = sc.nextInt();
        }

        sortColors(nums);

        for(int i = 0; i < n; i++){
            System.out.print(nums[i] + " ");
        }
    }
}