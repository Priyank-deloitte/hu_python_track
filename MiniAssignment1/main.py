import ClassString
import Pairs
import SearchElement
import equalSumPair

if __name__ == '__main__':
    stringClassobj = ClassString.StringClass
    stringClassobj.LengthOfString("12345678")
    stringClassobj.ListOfChar("12345678")

    pairObj = Pairs.PairsPossible
    pairObj.pairs("13246587")

    commonEleObj = SearchElement.searchCommonElement
    commonEleObj.commonElement("12345678", "13246587")

    equalSumPairObj = equalSumPair.EqualSumPairs
    equalSumPairObj.equal_Sum("1212")
