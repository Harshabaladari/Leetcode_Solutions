class Solution:
    def reorganizeString(self, s: str) -> str:
        res=""
        count=Counter(s)
        heap=[[-cnt,char] for char,cnt in count.items()]
        heapq.heapify(heap)
        while len(heap)>1:
            ct1,char1=heapq.heappop(heap)
            ct2,char2=heapq.heappop(heap)
            ct1+=1
            ct2+=1
            res+=char1+char2
            if -1*ct1>0:
                heapq.heappush(heap,[ct1,char1])
            if -1*ct2>0:
                heapq.heappush(heap,[ct2,char2])
        if heap:
            ct,char=heapq.heappop(heap)
            if -1*ct>1:
                return ""
            return res+char
        return res
