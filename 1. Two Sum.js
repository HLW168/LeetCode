var twoSum = function(nums, target) {
	if (nums.length === 2 ) return [0,1];
	const len = nums.length;
	// 利用 map 紀錄
	let map = {};
	for (let i = 0; i < len; i++) {
		let n = target - nums[i];
		let find = map[n]; // 和 i 互補的數字
		if(find != undefined) return [find, i];
		else map[nums[i]] = i; // i 是 index
	}
}
