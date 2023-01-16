# coding:utf-8

"""
    进程：
        操作系统中执行的一个程序，操作系统以进程为单位分配存储空间。
        每个进程都有自己的地址空间、数据栈以及其它用于跟踪进程执行的辅助数据。
        操作系统管理所有进程的执行，为它们合理地分配资源。
        每一个进程都像人一样需要吃饭，它的粮食就是：cpu和内存。
        进程的创建模块：multiprocessing
        主进程与子进程互不影响。


    线程：
        进程提供线程执行程序的前置要求，线程在重组的资源配备下，去执行程序

    Python 实现并发编程的3 种方式：
        多进程、多线程、多进程 + 多线程

    多进程的问题：
        通过多进程模块执行的函数无法获取返回值
        多个进程同时修改文件可能会出现错误
        进程数量太多可能会造成资源不足
"""

import time
import os
from multiprocessing import Process


def work_a():
    for i in range(10):
        print(i, 'a', os.getpid())
        time.sleep(1)


def work_b():
    for i in range(10):
        print(i, 'b', os.getpid())
        time.sleep(1)


if __name__ == '__main__':
    start = time.time()  # 主进程代码1
    a_p = Process(target=work_a)  # 子进程1
    a_p.start()  # 子进程1执行
    b_p = Process(target=work_b)  # 子进程2
    b_p.start()  # 子进程2执行

    for p in (a_p, b_p):
        p.join()
    print(time.time() - start)  # 主进程代码2
    print('parent pid is %s' % os.getpid())  # 主进程代码3

# from random import randint

# def download_task(filename):
#     print(f'开始下载{filename}...')
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print(f'{filename}下载完成！耗费了{time_to_download}秒')
#
#
# start = time()
# download_task('Python入门.pdf')
# download_task('Python高级.pdf')
# end = time()
# print(f'一共耗费了{end - start}秒')

# 开启多进程
# from multiprocessing import Process
# from os import getpid
#
#
# def downLoad_task1(filename):
#     print(f'启动下载进程，进程号{getpid()}.')
#     print(f'开始下载{filename}...')
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print(f'{filename}下载完成！耗费了{time_to_download}秒')
#
#
# if __name__ == '__main__':
#     start = time()
#     p1 = Process(target=downLoad_task1, args=('JavaScript入门.pdf',))
#     p1.start()
#     p2 = Process(target=downLoad_task1, args=('JavaScript进阶.pdf',))
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time()
#     print(f'一共耗费了{end - start}秒')
