# https://github.com/Python-World/python-mini-projects/blob/master/projects/Internet_connection_check/internet_connection_check.py

from encodings import utf_8
import requests
from requests.exceptions import ConnectionError

def internet_connection_test():
	url = 'https://www.baidu.com/'
	print(f'Attempting to connect to {url} to determine internet connection status.')
	
	try:
		print(url)
		resp = requests.get(url, timeout = 10)
		resp.text
		resp.status_code
		print(f'{url} is fine!')
		return True
	except ConnectionError as e:
		requests.ConnectionError
		print(f'Failed to connect to {url}.')
		return False
	except:
		print(f'Failed with unparsed reason.')
		return False

internet_connection_test()