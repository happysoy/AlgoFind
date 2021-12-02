def comparePattern(string, target):
    cnt=0
    loc = 0
    for i in range(len(string) - len(target)+1):
        loc += 1
        for j in range(len(target)):
            cnt += 1
            if string[i+j] != target[j]:
                break
        else:
            print('matched')
            print(f'{cnt} times')
            break
    else:
        print('not matched')
        print(f'{cnt} times')

    if(cnt == len(target)):
        return 1
    else:
        return -1