import datetime


def count_time(func):
    def int_time(*args, **kwargs):
        start_time = datetime.datetime.now()  # 程序开始时间
        func()
        over_time = datetime.datetime.now()   # 程序结束时间
        total_time = (over_time-start_time).total_seconds()
        print('程序共计%s秒' % total_time)
    return int_time


@count_time
def main():
    print('>>>>开始计算函数运行时间')
    for i in range(1, 100):
        for j in range(i):
            print(j)


if __name__ == '__main__':
    main()
