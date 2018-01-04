import logging
import os

class log_captcha:

	def __init__(self, module_name, loglevel=logging.INFO):
		self.log_creation(module_name + '.log', loglevel, module_name)
		self.log = logging.getLogger(module_name)

	def log_creation(self, filename, level, logger):
		
		#find the project path and base dir
		PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
		BASE_DIR = os.path.dirname(PROJECT_PATH)
		
		#base dir doesn't exist then create new base dir
		if not os.path.exists(BASE_DIR):
			os.makedirs(BASE_DIR)

		log = logging.getLogger(logger)
		
		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		loglocation = BASE_DIR+"/log/"+filename
		filehandler = logging.FileHandler(loglocation, mode='a')
		filehandler.setFormatter(formatter)

		log.setLevel(level)
		log.addHandler(filehandler)

