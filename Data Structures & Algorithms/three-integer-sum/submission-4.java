

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        HashMap<Integer, Integer> complement = new HashMap<>();
        Arrays.sort(nums);

        List<List<Integer>> output = new ArrayList<>();

        for (int i=0; i<nums.length; i++) {
            int curr = nums[i];

            if (i > 0 && nums[i] == nums[i-1]) continue;

            int left = i+1;
            int right = nums.length-1;

            while (left < right) {
                int total = curr + nums[left] + nums[right];
                if (total == 0) {
                    output.add(Arrays.asList(curr, nums[left], nums[right]));

                    left += 1;
                    right -= 1;
                    while (left < right && nums[left] == nums[left-1]) left+=1;
                    while (left < right && nums[right] == nums[right+1]) right -= 1;

                } else if (total > 0) {
                    right -= 1;

                } else {
                    left += 1;
                }
            }

        }


        return output;
        }
}