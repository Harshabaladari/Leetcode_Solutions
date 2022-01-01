class Solution:
    def reorganizeString(self, s: str) -> str:
        res=""
        count=Counter(s) #creates a dictionary
        # Creating a maxheap by inserting frequency(-ve values as maxheap is not available in python) and char
        heap=[[-cnt,char] for char,cnt in count.items()]
        heapq.heapify(heap)
        # Until heap contains atleast one element
        while len(heap)>1:
            # heapop - pops minimum zero based index value
            ct1,char1=heapq.heappop(heap)
            ct2,char2=heapq.heappop(heap)
            ct1+=1
            ct2+=1
            res+=char1+char2
            # If frequency of char is greater than zero, push it again into heap
            if -1*ct1>0:
                heapq.heappush(heap,[ct1,char1])
            if -1*ct2>0:
                heapq.heappush(heap,[ct2,char2])
        # Check if there is any element left
        if heap:
            ct,char=heapq.heappop(heap)
            # If freq of char is greater than one, return empty string
            if -1*ct>1:
                return ""
            return res+char
        return res
