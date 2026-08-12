class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer , Integer > hash = new HashMap<>();
        int i = 0;
        for (int n : nums){
            int total = target - n;
            if(hash.containsKey(total)){
                return  new int[]{hash.get(total),i};
            }
            hash.put(n,i);
            i++;
        }
        return new int[] {};
    } 
}
