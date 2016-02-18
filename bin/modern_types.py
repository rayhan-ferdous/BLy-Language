types = ["frac", "comp"]

def is_modern_type(token):

	for str in types:
		if str == token:
			return True
	return False