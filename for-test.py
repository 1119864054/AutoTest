if __name__ == '__main__':

    a = [1, 2, 3, 4, 5, 6, 7]
    b = ['a', 'b', 'c', 'd']

    for index, (value1, value2) in enumerate(zip(a[1:], b[1:])):
        print(index, value1, value2)
