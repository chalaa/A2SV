class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> vec;
        for(int i=0;i<nums.size();i++){
            int cn=0;
            for(int j=0;j<nums.size();j++){
                if(nums[i]>nums[j]){
                    cn++;
                }
            }
            vec.push_back(cn);
        }
        return vec;
    }
};