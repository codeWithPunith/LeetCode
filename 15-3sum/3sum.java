class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        int l=0,r=nums.length;
        int n =nums.length;
       for (int i = 0; i < n - 2; i++){
         if (i > 0 && nums[i] == nums[i - 1]) continue;
            int needed = -nums[i];
            l = i+1;
            r = n-1;
            while(l<r){
                if(nums[l]+nums[r]==needed){
                    res.add(new ArrayList<>(Arrays.asList(nums[l],nums[r],nums[i])));
                     while (l < r && nums[l] == nums[l + 1]) l++;
                     while (l < r && nums[r] == nums[r - 1]) r--;
                     l++;
                     r--;
                }else if(nums[l]+nums[r]<needed) l+=1;
                 else r-=1;
            }
          
      
        }
        return res;
    }
}