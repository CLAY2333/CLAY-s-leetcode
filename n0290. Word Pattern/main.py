// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def listtoint(self,List):
        List_set=[]
        for i in List:
            if i not in List_set:
                List_set.append(i)
        List_dict={}
        index=1
        for i in List_set:
            List_dict[i]=index
            index+=1
        Str=''
        for i in List:
            Str+=str(List_dict[i])
        return int(Str)
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern_list=list(pattern)
        str_list=str.split(' ',str.count(' '))
        if(len(pattern_list)!=len(str_list)):
            return False
        else:
            str_int=self.listtoint(str_list)
            pattern_int = self.listtoint(pattern_list)
            if(pattern_int==str_int):
                return True
            else:
                return False
