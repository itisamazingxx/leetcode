"""
order design了一个new pattern (新的字典序)
按这个新的字典序给产品code排序
用哈希表记录新的字典序(char: index)形式
把每个产品的code的新的index顺序记录下来（按这个排序）
返回原先的string
"""

class Solution:
    def sortString(self, productCode, order):

        record = {char: index for index, char in enumerate(order)}

        def convert(code):
            index_list = []
            for char in code:
                index_list.append(record[char])
            return index_list


        sorted_list = [(convert(code), code) for code in productCode]
        sorted_list.sort()
        result = [x[1] for x in sorted_list]
        return result
    
solution = Solution()
print(solution.sortString(["abc", "bca", "cab", "bac"], "hgfedcba"))

