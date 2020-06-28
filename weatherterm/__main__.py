import sys
from argparse import ArgumentParser
from weatherterm.core import Unit
from weatherterm.core import requestForecast
from weatherterm.core import requestCodes

argparser = ArgumentParser(prog='weatherterm',description='Weather info from weather.com on your terminal')
required = argparser.add_argument_group('Required Arguments')

unit_values = [name.title() for name, value in Unit.__members__.items()]

required.add_argument('-s', '--state',
	required=True,
	dest='State',
	help='ex. california, new-york')

required.add_argument('-c', '--city',
	required=True,
	dest='City',
	nargs='+',
	metavar='city',
	help='ex. San Francisco, New York')

argparser.add_argument('-v', '--version',
	action='version',
	version='%(prog)s 1.0')

argparser.add_argument('-C', '--code',
	metavar='code',
	dest='Code',
	help=("You can get the code of the city from the state_codes folder or online"))

args = argparser.parse_args()
city = ' '.join(args.City)
forecast = requestForecast(state=args.State, city=city, code=args.Code)
print(forecast)