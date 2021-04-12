def isValseq(arr, seq):
	flag = False
	for i in range(len(seq)):
		flag = seq[i] in arr 
		if (flag == False):
			return flag
		elif (seq[i-1] is not None):
			if (seq[i-1] == seq[i]):
				flag = False
				return flag
		elif (seq[i+1] is not None):
			if (seq[i+1] == seq[i]):
				flag = False
				return flag
	return flag
