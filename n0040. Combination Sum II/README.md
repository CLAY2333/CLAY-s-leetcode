
### Combination Sum II :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/combination-sum-ii](https://leetcode-cn.com/problems/combination-sum-ii)
- 执行时间/Runtime: 636 ms 
- 内存消耗/Mem Usage: 13.2 MB
- 通过日期/Accept Datetime: 2019-04-10 15:45
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def Loop(self,candidates,target,now_index,re:list,now_list:list):
        if(target==0):
            if not sorted(now_list) in re:
                re.append(sorted(now_list.copy()))
        if(len(candidates)==0 or target<candidates[0]):
            return 0
        for index,value in enumerate(candidates):
            if(value>target):
                break
            #if(value<candidates[now_index]):
                #continue
            now_list.append(value)
            candidates.pop(index)
            self.Loop(candidates,target-value,index,re,now_list)
            candidates.insert(index,value)
            now_list.pop()

    def combinationSum2(self, candidates: list, target: int) -> list:
        if len(candidates)==0:
            return []
        candidates=sorted(candidates)
        now_list=[]
        index=0
        re=[]
        self.Loop(candidates,target,index,re,now_list)
        return re

```