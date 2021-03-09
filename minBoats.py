from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # people.sort(reverse=True)
        minBoats = 0
        
        # Strategy: After allowing a person with weight W, we need to try to find a person with weight <=(limit-W), if present, allow, else increase count of Boats.
        
        peopleWeight = {}
        for person in people:
            if person not in peopleWeight:
                peopleWeight[person] = [False]
            else:
                peopleWeight[person].append(False)
        
        # print(peopleWeight)
        for person in peopleWeight:
            while(False in peopleWeight[person]):
                peopleWeight[person].remove(False)
                peopleWeight[person].append(True)
                minBoats += 1
                diff = limit-person
                for i in range(diff,0,-1):
                    if i in peopleWeight and False in peopleWeight[i]:
                        peopleWeight[i].remove(False)
                        peopleWeight[i].append(True)
                        break

                print(peopleWeight)

        print(minBoats)
        # print(peopleWeight)
                    

s = Solution()
s.numRescueBoats([1,3,5,5], 7)