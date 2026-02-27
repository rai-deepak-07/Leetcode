// Sample Input
// 6
// 2 1 5 6 2 3

import java.util.*;

public class L84 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();   // size of array
        int[] heights = new int[n];

        for(int i = 0; i < n; i++){
            heights[i] = sc.nextInt();
        }

        System.out.println(largestRectangleArea(heights));
    }

    public static int largestRectangleArea(int[] heights) {
        int n = heights.length;
        int[] PSE = new int[n];
        int[] NSE = new int[n];

        Stack<Integer> st = new Stack<>();
        
        // Previous Smaller Element or Left Smallest Element 
        for(int i = 0; i < n; i++){  // Left to Right
            while(!st.isEmpty() && heights[st.peek()] >= heights[i]){
                st.pop();
            }
            PSE[i] = (st.isEmpty()) ? -1 : st.peek();
            st.push(i);
        }
        st.clear();

        // Next Smaller Element / Right Smallest Element
        for(int i = n-1; i >= 0; i--){ // Right to Left
            while(!st.isEmpty() && heights[st.peek()] >= heights[i]){
                st.pop();
            }
            NSE[i] = (st.isEmpty()) ? n : st.peek();
            st.push(i);
        }

        int maxArea = 0;
        for(int i = 0; i < n; i++){
            int height = heights[i];
            int width = NSE[i] - PSE[i] - 1;
            maxArea = Math.max(maxArea, height * width);
        }

        return maxArea;
    }
}