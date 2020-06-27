from enum import Enum
class BaseEnum(Enum):
	def generate_next_value_(name, start, count, last_value):
		return name
