# -*- coding:utf-8 -*-

file = open('test01.txt', 'w')
file.write('Hello, World!')
file.close()


"""
r : 일기
w : 쓰기 (기존 내용 덮어쓰기)
a : 쓰기 (기존 내용 이어 쓰기)
x : 새로운 파일 만들어서 쓰기
t / b : text / binary (default : t)
"""

