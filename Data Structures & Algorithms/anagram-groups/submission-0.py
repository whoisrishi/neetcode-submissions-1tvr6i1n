
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    	
        # groups = {}
    	
    	# for word in strs:
    	# 	signature = "".join(sorted(word))
    	# 	groups.setdefault(signature,[]).append(word)
    	# return list(groups.values())
    	
    	#OR
    	
    	counter = {}
    	
    	for word in strs:
    		word_key= [0]*26
    		for char in word:
    			word_key[ord(char)-ord('a')] +=1
    		immutable_key=tuple(word_key)
    		counter.setdefault(immutable_key,[]).append(word)
    	return list(counter.values())
    	