# coding:utf-8

"""
    进程：
        操作系统中执行的一个程序，操作系统以进程为单位分配存储空间。
        每个进程都有自己的地址空间、数据栈以及其它用于跟踪进程执行的辅助数据。
        操作系统管理所有进程的执行，为它们合理地分配资源。

    Python 实现并发编程的3 种方式：
        多进程、多线程、多进程 + 多线程
"""


import sys

print("Script name:", sys.argv[0])
print("Arguments:", end=" ")

for arg in sys.argv[1:]:
    print(arg, end=" ")

print()
