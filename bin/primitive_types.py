types = ["int", "+int", "char", "float", "string", "bool" ]

def is_primitive_type(token):

	for str in types:
		if str == token:
			return True
	return False