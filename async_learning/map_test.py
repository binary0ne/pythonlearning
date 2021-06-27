import concurrent.futures
import time

def add_two(number):
	if number == 4:
		return None
	return number + 2

def multithread(func, array, workers):
	with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
		return executor.map(func, array)

if __name__ == '__main__':
	testlist = [1,2,3,4,5,6]
	time_start = time.time()
	new_list = multithread(add_two, testlist, 1)
	duration = time.time() - time_start
	print(testlist)
	print(list(new_list))
	print(duration)