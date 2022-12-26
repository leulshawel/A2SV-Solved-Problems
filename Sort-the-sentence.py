class Solution:
    
    sorter = lambda word: int(word[-1])
    
    def sortSentence(self, s):
        
        listofwords = s.split(" ")
        listofwords.sort(key=Solution.sorter)
        
        sentence = ""
        for word in listofwords:
            actualword = word[:len(word)-1]
            sentence += (actualword + " ")
            
        return sentence.strip()
