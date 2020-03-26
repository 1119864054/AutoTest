def test():
    try:
        a = "aaaa"
        b = "bbbb"
        raise Exception("自定义异常 %s <=> %s" % (a, b))
    except Exception as e:
        print("exception 1", e)
        raise


if __name__ == '__main__':
    try:
        test()
    except Exception as e:
        print("exception 2", e)
