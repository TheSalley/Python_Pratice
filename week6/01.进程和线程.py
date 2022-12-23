# coding:utf-8

"""
    进程：
        操作系统中执行的一个程序，操作系统以进程为单位分配存储空间。
        每个进程都有自己的地址空间、数据栈以及其它用于跟踪进程执行的辅助数据。
        操作系统管理所有进程的执行，为它们合理地分配资源。

    Python 实现并发编程的3 种方式：
        多进程、多线程、多进程 + 多线程
"""

from random import randint
from time import time, sleep

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
from multiprocessing import Process
from os import getpid


def downLoad_task1(filename):
    print(f'启动下载进程，进程号{getpid()}.')
    print(f'开始下载{filename}...')
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print(f'{filename}下载完成！耗费了{time_to_download}秒')


if __name__ == '__main__':
    start = time()
    p1 = Process(target=downLoad_task1, args=('JavaScript入门.pdf',))
    p1.start()
    p2 = Process(target=downLoad_task1, args=('JavaScript进阶.pdf',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print(f'一共耗费了{end - start}秒')
