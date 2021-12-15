import pytest


# if __name__ == '__main__':
    # pytest.main([r"E:\\pythonProject0926\tests\testpytest\test_py.py::TestPractice::test_03"])
    # pytest.main(["-v","-s"])
    # pytest.main(["-v","-s","-k=test and not 02"])
    # pytest.main(["-k=test and TestPractice and not test_02"])

# def reverseStr(s,k):
#     result = ''
#     i = 0
#     while i <= len(s):#当所取长度大于字符串的长度的时候证明字符串已反转完成
#         result +=  s[i:i + k][::-1] + s[i + k:i + 2 * k]#取2k长度字符串，反转前k个，保留后k个顺序不变
#         i += 2 * k#每次迭代取2k长度
#     return result
# print(reverseStr('fhdjsahfjqr',2))
# a = "fhdjsahfjq"
# def re(str,k):
#     i = 0
#     str1 = ""
#     # 判断符合条件，进行循环
#     while i <= len(str):
#         # [::-1]倒序
#         str1 += str[i:i+k][::-1]+str[i+k:i+2*k]
#         i += 2*k
#     return str1
#
# print(re('fhdjsahfjqr',2))

def getmerge(list1,list2):
    list3 = []
    for i in list1:
        for j in list2:
            if i == j:
                list3.append(i)
                list2.remove(j)
                break
    return list3
nums1 = [1,2,4,9,11,15]
nums2 = [1,3,4,7,9,12,15]
print(getmerge(nums1,nums2))