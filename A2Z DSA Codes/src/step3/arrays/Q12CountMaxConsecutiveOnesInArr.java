/*
Count Max Consecutive Ones in an array 18/5/25
https://takeuforward.org/data-structure/count-maximum-consecutive-ones-in-the-array/
*/

package step3.arrays;

public class Q12CountMaxConsecutiveOnesInArr {
    public int findMaxConsecutiveOnes(int[] nums) {
        /*
        ------------ Brute Force -------------- TC - O(N^2), SC - O(1)
        */

        /*

        int maxOnesCount = 0;

        for(int i = 0; i < nums.length; i++) {
            if(nums[i] == 1) {
                int count = 0;
                int j = i;

                while(j < nums.length && nums[j] == 1) {
                    count++;
                    j++;
                }
                maxOnesCount = Math.max(count, maxOnesCount);
                i = j-1;        // skip checked ones j-1 bcz after initialisation loop will do i++, if done i=j, then i++ will move one more step further which is wrong

            }
        }
        return maxOnesCount;

         */

        /*
        ------------ Optimised -------------- TC - O(N), SC - O(1)
        */


        int maxOnesCount = 0;
        int count = 0;

        for(int i = 0; i < nums.length; i++) {
            if(nums[i] == 1) {
                count++;
            }
            else {
                count = 0;
            }
            maxOnesCount = Math.max(count, maxOnesCount);
        }
        return maxOnesCount;

    }

    public static void main(String[] args) {
        Q12CountMaxConsecutiveOnesInArr obj = new Q12CountMaxConsecutiveOnesInArr();
        int[] input = {0, 0, 1, 1, 1, 0, 0, 1, 1};
        int ans = obj.findMaxConsecutiveOnes(input);
        System.out.println("Max consecutive 1's is: " + ans);
    }
}
