from datetime import datetime
from pytz import timezone
from utils import config

def currentdatetime():
	'''Function that returns the date and time in format specified in config.'''
	return datetime.now(timezone(config.timezone)).strftime(config.timeformat)