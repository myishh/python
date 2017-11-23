def isodd(n):
	return n % 2 == 1

res = list(filter(isodd, [1,2,3,4,5,6,9,10,15]))
print(res)

def not_empty(s):
	return s and s.strip()

res = list(filter(not_empty, ['A', '', 'B', None, 'C', 'e', '  ']))
print(res)


#用Python来实现埃氏筛法算法，可以先构造一个从3开始的奇数序列：
def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

#注意这是一个生成器，并且是一个无限序列
#然后定义一个筛选函数
def _not_divisible(n):
	return lambda x: x % n > 0

#最后，定义一个生成器，不断返回下一个素数：
def primes():
	yield 2
	it = _odd_iter()	#初始序列
	while True:
		n = next(it)	#返回序列的第一个数
		yield n
		it = filter(_not_divisible(n), it)	#构造新序列

#这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列
#由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
#打印1000以内的素数
for n in primes():
	if n < 1000:
		print(n)
	else:
		break

#注意到Iterator是惰性计算的序列，所以我们可以用Python表示“全体自然数”，“全体素数”这样的序列，而代码非常简洁
