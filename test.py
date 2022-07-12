with open('to_send.txt', mode='r', encoding='utf-8') as f:
    for item in f:
        # 将名字筛选出来
        print(item)
        name = item.split(' ')[1].split(',')[-1].replace(']', "")
        print(name)

