#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;



class Solution {
public:
	vector<int> twoSum(vector<int>& nums, int target) {
		unordered_map<int, int> mapping;
		vector<int> result;
		for (int i = 0; i < nums.size(); i++)
		{
			mapping[nums[i]] = i;
		}
			
	
		for (int i = 0; i < nums.size(); i++)
		{
			const int gap = target - nums[i];
			if (mapping.find(gap) != mapping.end() && mapping[gap] > i)
			{
				result.push_back(i);
				result.push_back(mapping[gap]);
				break;
			}
		}
		return result;
	}
};

int main()
{	
	vector<int>temp;
	temp.push_back(1);
	temp.push_back(2);
	temp.push_back(2);
	temp.push_back(4);
	Solution S;
	vector<int>result;
	result = S.twoSum(temp, 4);
	
	for (int i = 0; i < result.size(); i++)
	{
		cout << result[i] << endl;
	}
	return 0;
}