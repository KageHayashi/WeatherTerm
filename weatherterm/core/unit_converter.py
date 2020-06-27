from .unit import Unit

class UnitConverter:
	def __init__(self, from_unit, dest_unit=None):
		self._parser_default_unit = parser_default_unit
		self.dest_unit = dest_unit
		self.convert_functions = {Unit.CELSIUS: self.to_celsius, Unit.FAHRENHEIT: self.to_fahrenheit,}
	
	@property
	def dest_unit(self):
		return self._dest_unit
	
	@dest_unit.setter
	def dest_unit(self, dest_unit):
		self._dest_unit = dest_unit
	
	def convert(self, temp):
		try:
			temperature = float(temp)
		except ValueError:
			return 0
		if (self.dest_unit == self._parser_default_unit or self.dest_unit is None):
			return self._format_results(temperature)
		func = self._convert_functions[self.dest_unit]
		result = func(temperature)
		return self._format_results(result)
	
	def _format_results(self, value):
		return int(value) if value.is_integer() else f'{value:.1f}'
	
	def to_celsius(self, fahrenheit_temp):
		result = (fahrenheit_temp - 32) * 5/9
		return result
	
	def to_fahrenheit(self, celsius_temp):
		result = (celsius_temp * 9/5) + 32
		return result
