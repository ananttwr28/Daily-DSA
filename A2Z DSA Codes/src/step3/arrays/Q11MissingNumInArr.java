/*
Find the missing number in an array 17/5/25
https://takeuforward.org/arrays/find-the-missing-number-in-an-array/
*/

package step3.arrays;
//import java.util.HashMap;
//import java.util.Map;


/*
------------ Brute Force -------------- TC - O(N^2), SC - O(1)

approach -
iterate from 0 to N, the original non-missing range and check if each i exist in arr if not return
*/

/*

public class Q11MissingNumInArr {
    public int missingNumber(int[] nums) {
        for(int i = 0; i <= nums.length; i++) {
            boolean found = false;
            for(int j = 0; j < nums.length; j++) {
                if(i == nums[j]) {
                    found = true;
                    break;
                }
            }
            if(!found) {
                return i;
            }
        }
        return -1;          // return here also, as java thinks return i, is not always executed so to avoid warnings
    }

    public static void main(String[] args) {
        Q11MissingNumInArr obj = new Q11MissingNumInArr();
        int[] input = {0, 1, 2, 4, 5};
        int missing = obj.missingNumber(input);
        System.out.println("Missing number: " + missing);
    }
}

*/

/*
------------ Brute Force 2 -------------- TC - O(NlogN+ N), SC - O(1)

approach -
sort the arr if not mentioned, run loop from 0 to n-1 check if i != arr[i] return i, else return n
*/

/*
public class Q11MissingNumInArr {
    public int missingNumber(int[] nums) {
        Arrays.sort(nums);      // TC O(NlogN), SC O(logN)

        for(int i = 0; i < nums.length; i++) {
            if(i != nums[i]) {
                return i;
            }
        }
        return nums.length;          // return n as loop only ran till n-1
    }

    public static void main(String[] args) {
        Q11MissingNumInArr obj = new Q11MissingNumInArr();
        int[] input = {0, 1, 2, 4, 5};
        int missing = obj.missingNumber(input);
        System.out.println("Missing number: " + missing);
    }
}
*/

/*
------------ Better -------------- TC - O(2N), SC - O(N)

approach - using hash map
store the count of each arr elt in map,
iterate from 0 to N and check if any elt freq is 0 return that

hashmap is unordered in java TC for operations is O(1) and SC of map is O(size)
*/

/*
public class Q11MissingNumInArr {
    public int missingNumber(int[] nums) {
        Map<Integer, Integer> mp = new HashMap<>();         // Map tells that create a structure where key and value are int,
        // new HashMap tells that create it of type Hashmap other types are linkedmap and tree..
        // <> shorthand for type of key and value in hashmap will be same as left hand side
        for(int i = 0; i < nums.length; i++) {
            if(mp.containsKey(nums[i])) {
                mp.put(nums[i], mp.get(nums[i])+1);
            }
            else {
                mp.put(nums[i], 1);
            }
        }
        for(int i = 0; i <= nums.length; i++) {
            if(!mp.containsKey(i)) {            // we have to check if not in map, initially if contains == false means condition is true and if block
                // will get executed, ! does same thing, if contains return false then negates and make true, true meaning goes inside if,
                // true negates to false so not going inside the if block
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        Q11MissingNumInArr obj = new Q11MissingNumInArr();
        int[] input = {0, 1, 2, 4, 5};
        int missing = obj.missingNumber(input);
        System.out.println("Missing number: " + missing);
    }
}
*/


/*
------------ Optimal 1 -------------- TC - O(N), SC - O(1)

approach - diff of sum of first n whole nums and actual arr sum
not suitable for long values as int cant hold large values
*/


/*
public class Q11MissingNumInArr {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int act_sum = 0;
        int org_sum = (n*(n+1))/2;

        for(int i = 0; i < nums.length; i++) {
            act_sum += nums[i];
        }

        return org_sum-act_sum;
    }

    public static void main(String[] args) {
        Q11MissingNumInArr obj = new Q11MissingNumInArr();
        int[] input = {0, 1, 2, 4, 5};
        int missing = obj.missingNumber(input);
        System.out.println("Missing number: " + missing);
    }
}
*/


/*
------------ Optimal 2 -----  XOR  ----- TC - O(N), SC - O(1)

approach - xor of same nums is 0 and 0 ^ num = num
*/


public class Q11MissingNumInArr {
    public int missingNumber(int[] nums) {
        int idx_xor = 0;
        int arr_xor = 0;

        for(int i = 0; i < nums.length; i++) {
            idx_xor ^= i;
            arr_xor ^= nums[i];
        }
        idx_xor ^= nums.length;         // xorred with n as it was not included in loop

        return idx_xor^arr_xor;
    }

    public static void main(String[] args) {
        Q11MissingNumInArr obj = new Q11MissingNumInArr();
        int[] input = {0, 1, 2, 4, 5};
        int missing = obj.missingNumber(input);
        System.out.println("Missing number: " + missing);
    }
}
