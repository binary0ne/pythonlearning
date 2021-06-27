import concurrent.futures

tasks = ['daemon', 'programm']
state = {'daemon':'', 'programm':''}
iter_number = 0

def execute_task():
	global iter_number
	for x in range(100000000):
		iter_number += 1
	state['programm'] = 'done'

def execute_daemon():
	global iter_number
	while state['programm'] != 'done':
		if iter_number % 200 == 0:
			print(iter_number)
	state['daemon'] = 'done'

def hypervisor(task_type):
	if task_type == 'programm':
		execute_task()
	elif task_type == 'daemon':
		execute_daemon()

with concurrent.futures.ThreadPoolExecutor(max_workers=len(tasks)) as executor:
	executor.map(hypervisor, tasks)

print(state)