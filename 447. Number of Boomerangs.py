class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = 0
        for p in points:
            dic = {}
            for q in points:
                x = q[0]-p[0]
                y = q[1]-p[1]
                l = x*x+y*y
                dic[l] = dic.get(l,0)+1
            for key in dic:
                result += dic[key]*(dic[key]-1) # for each hashset k(k-1)
        return result
