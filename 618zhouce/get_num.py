"""
长度为n的数组，其中有一个数字出现大于n/2次，快速找到这个数字
"""

list_nums = [0, 1, 1, 1, 1, 3, 4, 1, 6, 1]



def get_nums(target):
    return sorted(target)[len(target)//2]

print(get_nums(list_nums))

def get_num(target):
    for i in target:
        if target.count(i) >= len(target) / 2:
            return i


# 假设100层阶梯，两个鸡蛋，设计第几层鸡蛋会碎
def func01():
    egg = True  # 假设鸡蛋没碎为真，鸡蛋碎了为假
    count = 0
    while egg:
        if egg:
            count += 1
            print('第%d层鸡蛋没碎' % count)
        else:
            if count > 100:
                print('鸡蛋不会碎')
            else:
                egg = False
                print('第%d层鸡蛋碎了' % count)


# 输入一个正数n，输出所有和为n连续正数序列。
def func02(n):
    m = n // 2
    list_max = []
    for r in range(1, m + 1):
        number = 0
        list_number = []
        for c in range(r, m + 2):
            number += c
            list_number.append(c)
            if number == n:
                list_max.append(list_number)
                break
            elif number > n:
                break
    return list_max


print(func02(15))
#
# # 4.找最长公共子串
# str1 = 'BDCABA'
# str2 = 'BCBABDA'
#
#
# def func03(str1, str2):
#     new_str = []
#     n = 0
#     m = 0
#     if len(str1) < len(str2):
#         for r in range(len(str1)-1,-1,-1):
#             for c in range(len(str2)-1,-1,-1):
#                 if str1[r] == str2[c]:
#                     m = r
#                     n = c + 1
#                     new_str.append(str1[r])
#                     break
#         return new_str, len(new_str)
#
#
# print(func03(str1, str2))
