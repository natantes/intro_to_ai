
def order(current, stats):
	store_set = {}
	most_frequent_number = [-1, -1]
	summ = 0	

	def merge_sort(current):
		if len(current) > 1:
			mid = len(current) // 2
			l, r = current[:mid], current[mid:]
			merge_sort(l)
			merge_sort(r)

			i = j = k = 0

			while i < len(l) and j < len(r):
				if l[i] > r[j]:
					current[k] = r[j]
					j += 1
				else:
					current[k] = l[i]
					i += 1
				k += 1

			while i < len(l):
				current[k] = l[i]
				i += 1
				k += 1
			
			while j < len(r):
				current[k] = r[j]
				j += 1
				k += 1

		if len(current) == 1:
			if current[0] in store_set:
				store_set[current[0]] += 1
			else:
				store_set[current[0]] = 1		
	
	merge_sort(current)

	for n in store_set:
		if store_set[n] > most_frequent_number[1] or store_set[n] == most_frequent_number[1] and n < most_frequent_number[0]:
			most_frequent_number = [n, store_set[n]]
		summ += n * store_set[n]
	
	stats[0] = summ // len(current)
	stats[1] = current[len(current) // 2 - 1] if len(current) % 2 == 0 else current[len(current) // 2]
	stats[2] = most_frequent_number[0]

	return 0