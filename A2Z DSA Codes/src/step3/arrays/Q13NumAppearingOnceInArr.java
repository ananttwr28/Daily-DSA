/*
Find the Num that appears once in an array 19/5/25
https://takeuforward.org/arrays/find-the-number-that-appears-once-and-the-other-numbers-twice/
*/

package step3.arrays;

public class Q13NumAppearingOnceInArr {
    public int findNumAppearsOnce(int[] nums) {
    /*
    ------------ Brute Force -------------- TC - O(N^2), SC - O(1)
    Approach - iterate over arr, check if the element exist other than that idx if not return that element
    */

    /*
        for(int i = 0; i < nums.length; i++) {
            boolean found = false;
            int key = nums[i];
            for(int j = 0; j < nums.length; j++) {
                if(j != i) {
                    if(nums[j] == key) {
                        found = true;
                        break;
                    }
                }
            }
            if(!found) {
                return key;
            }
        }
        return -1;      // avoiding error
    }
    */





    /*
    ------------ Better 1 -------------- TC - O(NlogN+N), SC - O(logN)
    approach - sort and check if prev and next elt is not equal to curr elt, return curr elt
    */

    /*
        Arrays.sort(nums);      // TC O(NlogN), SC O(logN)

        for(int i = 0; i < nums.length; i++) {          // TC O(N)
            if (i == 0) {
                if (nums[i] != nums[i + 1]) {
                    return nums[i];
                }
            } else if (i == nums.length - 1) {
                if (nums[i] != nums[i - 1]) {
                    return nums[i];
                }
            } else {      // 1 <= i <= n-2
                if (nums[i] != nums[i - 1] && nums[i] != nums[i + 1]) {
                    return nums[i];
                }
            }
        }
        return -1;      // avoiding error
    }
    */






    /*
    ------------ Better 2 -------------- TC - O(2N), SC - O(N)
    approach - store freq in map return element whose freq is 1
    */

    /*
        Map<Integer, Integer> mp = new HashMap<>();         // SC O(N)

        for(int i = 0; i < nums.length; i++) {          // TC O(N)
            if(mp.containsKey(nums[i])) {
                mp.put(nums[i], mp.get(nums[i])+1);
            }
            else {
                mp.put(nums[i], 1);
            }
        }
        // TODO: Read more about this after watching lec, or ask someone 19/5
        // Iterating through the Map using entrySet()

        for (Map.Entry<Integer, Integer> entry : mp.entrySet()) {       // TC O(Size of Map)
            Integer key = entry.getKey();   // Accessing the key
            Integer value = entry.getValue();  // Accessing the value

            if(value == 1) {
                return key;
            }
        }
        return -1;      // avoiding error

    */





    /*
    ------------ Optimised -------------- TC - O(2N), SC - O(N)
    approach - xor of elements occuring twice will become 0 (as xor of same elts is 0) and 0 xor the elt occuring once will be the elt itself
    */
        int reqNum = 0;

        for (int i = 0; i < nums.length; i++) {          // TC O(N)
            reqNum ^= nums[i];
        }
        return reqNum;
    }

    public static void main(String[] args) {
        Q13NumAppearingOnceInArr obj = new Q13NumAppearingOnceInArr();
        int[] input = {0, 1, 1, 5, 6, 5, 6};
        int ans = obj.findNumAppearsOnce(input);
        System.out.println("Num Appearing once is: " + ans);
    }
}
