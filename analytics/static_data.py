import json

dataObject = [
	['貸款來源', 'Taiwan', 'US'],
	['貸款年利率', '1.688', '4.8'],
	['當地貨幣', 'TWD', 'USD'],
	['匯率', '31', '1'],
	['貸款總額 (Local)', '12000000', '0'],
	['貸款總額 (USD)', '389231', '0'],
	['貸款月利率', '0.14', '0.4'],
	['貸款年數', '20', '30'],
	['期數', '240', '360'],
	['每月還款 (Local)', '58904', '0'],
	['每月還款 (USD)', '1911', '0']
]

editState = [
	[0,1,1],
	[0,1,1],
	[0,1,1],
	[0,1,1],
	[0,1,1],
	[0,1,1],
	[0,1,1],
	[0,1,1],
	[0,1,1],
	[0,1,1],
	[0,1,1]
]

def load_static_data():
	return {'dataObject': dataObject, 'editState': editState}

def update_data(evt):
	print(evt)
	row = evt['row']
	col = evt['col']
	pre = evt['pre']
	val = evt['val']
	dataObject[row][col] = val
	print(dataObject)