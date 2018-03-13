import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def getBrowserInfo(connectStat, stream, describe):
	print '\n\n'
	print 'Browser Info Analysis: stream ', stream
	print '\n\n'


	rankStream = df['#stream'] == stream
	browserList = df['browser'].unique()

	if connectStat:
		cnt = df['connected'] == True
	elif not connectStat:
		cnt = df['connected'] == False
	else:
		cnt = df['connected']

	
	for browser in browserList:
		browserStream = df['browser'] == browser
		print 'browser: [', browser, ']'
		print df[rankStream][browserStream & cnt].mean()
		if describe:
			print df[rankStream][browserStream & cnt].describe()
		print df[rankStream & browserStream]['connected'].value_counts()
		print '-----------'		

	print '\n\n\n'


def getISPInfo(connectStat, stream, describe):
	print '\n\n'
	print 'ISP Info Analysis: stream ', stream
	print '\n\n'

	rankStream = df['#stream'] == stream

	ispList = df['isp'].unique()

	if connectStat:
		cnt = df['connected'] == True
	elif not connectStat:
		cnt = df['connected'] == False
	else:
		cnt = df['connected']

	print 'ISP Frequencies:'
	print df[rankStream]['isp'].value_counts()
	print '---------------------'
	
	for isp in ispList:
		ispStream = df['isp'] == isp 
		print 'isp: [', isp, ']'
		print df[rankStream][ispStream & cnt].mean()
		if describe:
			print df[rankStream][ispStream & cnt].describe()
		print df[rankStream & ispStream]['connected'].value_counts()
		print '-----------'		

	print '\n\n\n'


def browserISPRelation(stream):
	print '\n\n'
	print 'Browser + ISP Relation Analysis: stream ', stream
	print '\n\n'
	
	rankStream = df['#stream'] == stream


	#browseList = df['browser'].unique()
	ispList = df['isp'].unique()


	for isp in ispList:
		ispStream = df['isp'] == isp 
		print 'isp: [', isp, ']'
		print df[rankStream & ispStream]['browser'].value_counts()
		print '-----------'		

	print '\n\n\n'


def plotResults(objects, valueList, title, inc, path):
	y_pos = np.arange(len(objects))
	performance = valueList
	 
	plt.bar(y_pos, performance, align='center', alpha=0.5)
	plt.xticks(y_pos, objects)
	#plt.ylabel('Usage')

	title = title + ' ' + str(inc)
	plt.title(title)
	plt.savefig(path)	 
	plt.close()

def connectionTrueZeroRelation(stream):
	print '\n\n'
	print 'Connection True, but zero p2p: stream ', stream
	print '\n\n'
	
	rankStream = df['#stream'] == stream

	zeroStream = df['p2p'] < 0.001
	cnt = df['connected'] == True

	#browseList = df['browser'].unique()
	ispList = df['isp'].unique()

	sumList = []

	for isp in ispList:
		ispStream = df['isp'] == isp 
		print 'isp: [', isp, ']'
		valCon = df[rankStream & ispStream & zeroStream & cnt]['browser'].value_counts()
		print valCon
		sumList.append(valCon)


		print '-----------'		

	result = None
	for i in range(0,len(sumList)):
		if i == 0:
			result = sumList[0]
		else:
			result = result.add(sumList[i], fill_value=0)

	inds = np.array(result.index.tolist()).argsort()
	resultAr = np.array(result.tolist())[inds]

	path = './connect_p2p_zero/' + str(stream) + '.png'
	plotResults(result.index.tolist(), resultAr, '# of browsers that is connected with p2p equal zero: stream ', stream, path)


	print '\n\n\n'

def connectionStats(stream):
	rankStream = df['#stream'] == stream
	print 'Connection Ratio (stream ',stream,'):'
	print df[rankStream]['connected'].value_counts()
	print '\n\n\n'

df = pd.read_csv('../../data.csv')

connectStat = True
#connectStat = False
stream = 1
describe = False



for stream in range(1,max(df['#stream'].unique())):
	print '++++++++++++++++++++ ', stream, ' +++++++++++++++++++++++'
	getBrowserInfo(connectStat, stream, describe)
	getISPInfo(connectStat, stream, describe)
	browserISPRelation(stream)
	connectionTrueZeroRelation(stream)
	connectionStats(stream)

