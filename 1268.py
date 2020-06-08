# -*- coding: utf-8 -*-


class Solution(object):
    def __init__(self):
        self.root = dict()
        self.tempResult = list()

    def prefixDict(self, products):
        for word in products:
            node = self.root
            for i in word:
                node[i] = node.get(i, dict())
                if not node[i]:
                    node[i]['store'] = list()
                node[i]['store'].append(word)
                node = node[i]

        return self.root

    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        result = list()
        root = self.prefixDict(products)
        for i in searchWord:
            if i in root:
                result.append(sorted(root[i]['store'])[:3])
                root = root[i]
            else:
                result.append(list())

        return result

if __name__ == "__main__":
    products = ["mobile","mouse","moneypot","monitor","mousepad", "mou"]
    products = ["havana"]
    products =["havana"]
    searchWord = "mouse"
    searchWord = "havana"
    searchWord = "tatiana"
    S = Solution()
    print(S.suggestedProducts(products, searchWord))