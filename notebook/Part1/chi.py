"""
This module make enable to import text data file from
CHI insrument Potentiostat for Electrochemical Analysis
to IPython environment

by Sung-Ho Lee
"""

import re
import matplotlib.pyplot as plt
import numpy as np
import xlsxwriter, os

class ImportChi:
	"""
	Import CHI datafile (type: txt)
	Need 1 argument : (file_name)
	"""

	def __init__(self, file):
		"""
		Initiate function
		"""
		self.file = file
		self.plot = open(self.file, 'r')
		self.voltage = []
		self.current = []
		self.load_data()

	def load_data(self):
		"""
		Parsing valuavle data from text file
		"""
		self.data = []
		self.header = []

		# Regulat Expression Format for Parsing valuable data from CHI datafile

		find_date = r'(?P<Month>\w{3})\w*\s(?P<Day>\d+),\s(?P<Year>\d{4})\s+(?P<Hour>\d{2}):(?P<Min>\d{2}):\d{2}'
		replace_date = r'\g<Year>/\g<Month>/\g<Day>th \g<Hour>:\g<Min>'
		find_inite = r'Init\sE\s[(]{1}V[)]{1}\s=\s(?P<InitE>[-]?[.0-9]+)'
		replace_inite = r'\g<InitE>'
		find_highe = r'High\sE\s[(]{1}V[)]{1}\s=\s(?P<HighE>[-]?[.0-9]+)'
		replace_highe = r'\g<HighE>'
		find_lowe = r'Low\sE\s[(]{1}V[)]{1}\s=\s(?P<LowE>[-]?[.0-9]+)'
		replace_lowe = r'\g<LowE>'
		find_srate = r'Scan\sRate\s[(]{1}V/s[)]{1}\s=\s(?P<ScanRate>[.0-9]+)'
		replace_srate = r'\g<ScanRate>'
		find_data = r'(?P<Potential>[-]?[.0-9]{5}),\s(?P<Current>[-]?[.0-9]{5}e[-]?\d+),\s[-]?[.0-9]{5}e[-]?\d+'
		replace_data = r'\g<Potential>,\g<Current>'

		for line in self.plot:
			line = line.strip('\r\n')
			if re.match(find_date, line):
				newline = re.sub(find_date, replace_date, line)
				self.header.append(newline)
			elif re.match(find_inite, line):
				self.header.append(re.sub(find_inite, replace_inite, line))
			elif re.match(find_highe, line):
				self.header.append(re.sub(find_highe, replace_highe, line))
			elif re.match(find_lowe, line):
				self.header.append(re.sub(find_lowe, replace_lowe, line))
			elif re.match(find_srate, line):
				self.header.append(re.sub(find_srate, replace_srate, line))
			elif re.match(find_data, line):
				data = re.sub(find_data, replace_data, line)
				temp = data.split(',')
				self.data.append((temp[0], temp[1]))
			else:
				pass

		print "The file '{0}' is loaded".format(self.file)

	def cv_curve(self):
		"""
		Plot Cyclicvoltametry curve using matplotlib
		"""

		if 'chi_output' in os.listdir(os.getcwd()):
			pass
		else:
			os.mkdir('chi_output')

		potential = []
		current = []

		for x,y in self.data:
			potential.append(x)
			current.append(y)

		potential = np.array(potential)
		current = np.array(current)
		plt.figure(figsize=(8,6))

		plt.plot(potential, current, linewidth = 2.5)
		plt.xlabel('Potential (V) vs Ag/AgCl', fontsize = 20)
		plt.ylabel('Current (A)', fontsize = 20)
		plt.savefig('chi_output/{0}.png'.format(self.file[5:-4]))
		plt.show()

	def __str__(self):
		"""
		Summary
		"""
		result = '[Header area]\nEXP date = {0}\nInit E = {1} V\nRange E = {3} ~ {2} V\nScan rate = {4} V/s\n\n[Data area (first tenth)]\n'.format(*self.header)
		cvresult = 'Voltage(V), Current(A)\n'
		for x,y in self.data[:10]:
			cvresult += '  '+str(x)+',    '+str(y)+'\n'
		return result + cvresult + '       ...'

	def xlsx(self):
		"""
		Output potential and current data to excel file
		"""
		if 'chi_output' in os.listdir(os.getcwd()):
			pass
		else:
			os.mkdir('chi_output')

		workbook = xlsxwriter.Workbook('chi_output/{0}.xlsx'.format(self.file[5:-4]))
		worksheet = workbook.add_worksheet()
		worksheet.write(0, 0, 'Potential (V)')
		worksheet.write(0, 1, 'Current (A)')

		row = 1
		for x, y in self.data:
			worksheet.write(row, 0, x)
			worksheet.write(row, 1, y)
			row += 1
		workbook.close()

		print "Excel file created at 'chi_output/{0}.xlsx'".format(self.file[5:-4])

