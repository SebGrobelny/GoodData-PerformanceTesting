import csv
import random

with open('masterData.csv', 'a') as fp:

	rand_list = []

	mod_selection = [1,2,5]

	cur_mod = 0
	fact_min = -1000
	fact_max = 1000

	base_num = int(0)
	csv_writer = csv.writer(fp, delimiter = ',')

	for k in range (10000001,20000000):
		exponent = 0
	 	mod_count = 0
	 	rand_list = []
	 	for j in range(1,101):
	 		if j < 51:
	# 		#increase the exponent every three columns
		 		if mod_count == 3:
		 			mod_count = 0
		 			exponent+=1
		# 		#	print "In comparison"
				
		 		cur_mod = mod_selection[mod_count]* pow(10,exponent)
		# 		#print 'Row number',k
		# 		#print 'Col number',j
		# 		#print 'Exponent',exponent
		# 		#print 'Cur_mod is',cur_mod

		 		store_num = base_num+k

		# 		#print 'Store_num is', store_num

		 		if j > 1:
		 			store_num = store_num % cur_mod
		# 		#print 'Modded Store_num is',store_num
		# 		#print 'Formatted store_num is',(str(store_num).zfill(12)) 
		 		rand_list.append(str(store_num).zfill(12))

		 		mod_count+=1
		# 		#print mod_count
			else:
			 rand_list.append('{0:.2f}'.format(random.uniform(fact_min,fact_max)))
		csv_writer.writerow(rand_list)
	fp.close()