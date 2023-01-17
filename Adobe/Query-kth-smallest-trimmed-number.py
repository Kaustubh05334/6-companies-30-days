from heapq import heapify,heappop,heappush
def smallestTrimmedNumbers(nums,queries):
        answer = []
        for x,y in queries:
            li = []
            heapify(li)
            for i in range(len(nums)):
                
                n1 = nums[i][len(nums[i])-y:len(nums[i])]
                n1 = int(n1)
                
                if len(li) < x:
                    heappush(li,[-1*n1,-1*i])
                
                else:
                    if n1<-1*li[0][0]:
                        heappop(li)
                        heappush(li,[-1*n1,-1*i])
               
            answer.append(-1*heappop(li)[1])       
        return answer