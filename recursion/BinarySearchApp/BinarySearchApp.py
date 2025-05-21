def binary_search(data, target, low_index, high_index):
    if low_index > high_index:
        return False
    else:
        mid_index = (high_index + low_index) // 2
        if target == data[mid_index]: 
            return True
        elif target > data[mid_index]:
            return binary_search(data, target, mid_index + 1, high_index)
        else:
            return binary_search(data, target, low_index, mid_index - 1)

if __name__ == '__main__':
    itemList = [2,3,5,6,7,8,34,56]
    print(f'Match Found : {binary_search(itemList, 7, 0, 7)}')