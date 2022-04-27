from datetime import datetime
from pytz import timezone
from utils import config

def currentdatetime():
	return datetime.now(timezone(config.timezone)).strftime(config.timeformat)