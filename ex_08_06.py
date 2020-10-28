num_list = list()

while True :
    nums = input("Enter a number: ")
    if nums == "done" : break
    num = float(nums)
    num_list.append(num)

max_num = max(num_list)
min_num = min(num_list)

print(max_num)
print(min_num)
