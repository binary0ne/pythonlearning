import concurrent.futures


counter = 0
counter_list = []
active_threads = 2
attempts = 0
attempts_limit = 10000
increment_length = 1000
test_result = 10000 * active_threads

def increment_counter(fake_value):
	global counter
	for _ in range(10000):
		counter += 1
		counter_list.append(counter)

if __name__ == "__main__":
	counter = test_result
	while counter == test_result:
		fake_data = [x for x in range(active_threads)]
		counter = 0
		counter_list = []
		with concurrent.futures.ThreadPoolExecutor(max_workers=active_threads) as executor:
			executor.map(increment_counter, fake_data)
		attempts += 1
		if attempts >= attempts_limit:
			break

	if attempts != attempts_limit:
		print(f"Miscalculation happened on the attempt {attempts} with count result {counter}")

		sample = 1
		for number in counter_list:
			if sample != number:
				print(f"Expected {sample}, but got {number}")
				break
			sample += 1
	else:
		print(f"{attempts} attempt(s) were OK")
