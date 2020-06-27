int check()
{
	rbp-0x1 1
	rbp-0x8 i

	for(i=0;i<=8;){
		if(nums[i]<=nums[i+1]){
			i++;
			if(i<=8) continue;
			return i;
		} else{
			return 0;
		}
	}
}
