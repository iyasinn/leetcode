class Solution:
    def countSeniors(self, details: List[str]) -> int:

        count = 0
        for data in details: 
            age = int(data[11:13])
            count += int(age > 60)
        return count

        