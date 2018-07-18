# jinzhi = input('请输入二进制数字')
# sum = 0
# for i in range(len(jinzhi)):
#     if jinzhi[::-1][i] == '1':
#         sum += 2 ** i
# print(sum)

jinzhi = int(input('请输入二进制数字'))
sum = 0
for flag in range(len(str(jinzhi))):
    if jinzhi <= 0:
        break
    sum += (2 ** flag) * (jinzhi % 10)
    jinzhi = int(jinzhi /10)
print(sum)