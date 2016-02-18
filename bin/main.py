import primitive_types as PT
import modern_types as MT	

print PT.types
print MT.types

print PT.is_primitive_type("int")
print PT.is_primitive_type("INTEGER")

print MT.is_modern_type("comp")
print MT.is_modern_type("COMPLEX")