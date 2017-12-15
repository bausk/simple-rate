def proportional(*args):
	sum_before = sum(args[:-1])
	*params, special, sum_after = args
	coeff = sum_after / sum_before
	new = list(x * coeff for x in params)
	last = sum_after - sum(new)
	return (*new, last)