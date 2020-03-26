import time
import threading


def run():
    print(threading.current_thread().getName(), "开始工作")
    time.sleep(2)  # 子线程停2s
    print("子线程工作完毕", time.ctime())


for i in range(3):
    t = threading.Thread(target=run, )
    t.setDaemon(True)  # 把子线程设置为守护线程，必须在start()之前设置
    t.start()

if __name__ == '__main__':
    time.sleep(1)  # 主线程停1秒
    t.join()
    print("主线程结束了！")
    print(threading.active_count())  # 输出活跃的线程数
