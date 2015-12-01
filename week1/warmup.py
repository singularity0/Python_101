def factorial(n):
	fact = 1
	for i in range(1, n+1):
		fact *= i
	return fact
# print(factorial(0))
# print(factorial(1))
# print(factorial(5))

def fibonacci(n):
	seq = [0 , 1]
	for i in range(0, n-1):
		seq.append(seq[i] + seq[i+1])
	return seq[1:]
# print(fibonacci(3))


def sum_of_digits(n):
    sum = 0
    n = abs(n)
    n = str(n)
    for i in n:
         sum += int(i)
    return sum
# print(sum_of_digits(1325132435356))
# print(sum_of_digits(-10))

def fact_digits(n):
	sum = 0
	while n > 0:
		sum += factorial(n % 10)
		n = n //10
	return sum
# print(fact_digits(999))

def palindrome(obj):
	obj = str(obj)
	for i in range(0, len(obj)//2):
		if obj[i] != obj[(len(obj))-1-i]:

			return False
	return True
# print(palindrome('kapak'))
# print(palindrome(121))

def to_digits(n):
	n = list(str(n))
	return n
# print(to_digits(999))


def to_number(digits):
	result = ''
	for i in digits:
		result += str(i)
	return int(result)
# print(to_number([1,2,3,0,2,3]))

def fib_number(n):
	return to_number(fibonacci(n))
# print(fib_number(3))
# print(fib_number(10))

def count_vowels(st):
	vowels = 'aeiouy'
	counter = 0
	st = st.lower()
	for i in st:
		if i in vowels:
			counter += 1
	return counter
# print(count_vowels('Theistareykjarbunga'))
# print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!")

def count_consonants(st):
	cons = 'bcdfghjklmnpqrstvwxz'
	counter = 0
	st = st.lower()
	for i in st:
		if i in cons:
			counter += 1
	return counter
# print(count_consonants("A nice day to code!"))

def char_histogram(string):
	d = {}
	for i in string:
		if i not in d:
			d[i] = 1
		else:
			d[i] += 1
	return d
# print(char_histogram("AAAAaaa!!!"))

def p_score(n):
	total = 0
	n_rev = 0
	if palindrome(n) == True:
		return 1
	else:
		n = str(n)
		n_rev = int(n[::-1])
		n = int(n)
		total = 1 + p_score((n + n_rev))
	return total
# print(p_score(48))
# print(p_score(198))


def is_increasing(seq):
	for i in range(0, len(seq)-1):
		if seq[i+1] < seq[i]:
			return False
		if seq[i+1] == seq[i]:
			return False
	return True
# print(is_increasing([1,2,3,4,5]))
# print(is_increasing([1,1,1,1]))
# print(is_increasing([5,6,-10]))
# print(is_increasing([1]))

def is_decreasing(seq):
	rev = []
	for i in range(0, len(seq)):
		rev.append(seq[len(seq)-1-i])
	return is_increasing(rev)

# print(is_decreasing([5,4,3,2,1]))
# print(is_decreasing([1,2,3]))
# print(is_decreasing([100, 50, 20]))
# print(is_decreasing([1,1,1,1]))

def next_hack(n):
	number = ''
	counter1s = 0
	is_odd = True
	n_val = n
	while n > 0:
		number = str(n % 2) + number
		n = n//2
	for i in number:
		if i == '1':
			counter1s += 1
	if (counter1s % 2) == 0:
		is_odd = False
	return is_odd and palindrome(number)
print (next_hack(7))


