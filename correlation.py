import csv

companies = ['PETR4','CPLE6','VALE3','CIEL3']
emp = []
temp = []
corrTable = []
corrDict = {}

def meanCalc(values):
	c = 0
	for value in values:
		c = c + value
	Mean = c/len(values)
	return Mean

def stdDev(values):
	c = 0
	x = meanCalc(values)
	for value in values:
		c = c + (value - x)**2
	SD = (c/(len(values) - 1))**(0.5) ## **(0.5) -> square root
	return SD

def covarianceCalc(values_1, values_2):
	c = 0
	m1 = meanCalc(values_1)
	m2 = meanCalc(values_2)
	ran = len(values_1)
	for i in range(ran):
		c = c +(values_1[i]-m1)*(values_2[i]-m2)
	cov = c/(ran-1)
	return cov



def getPricesOnly(database, date):
	storeValues = []
	i = False
	for item in database:
		if item[0] == date:
			i = True
		if i == True:
			storeValues.append(float(item[1]))
	return storeValues



print("Digite o ticker da empresa que deseje consultar:\n")
ticker = input()
print("Digite a data inicial no formato aaaa-mm-dd:\n")
data = input()

with open(ticker+'.SA.csv', 'r') as bvsp_file:
	bvsp_reader = csv.DictReader(bvsp_file)
	for line in bvsp_reader:
		emp.append([line.pop('Date'), line.pop('Adj Close')])
	pricesChosenCompany = getPricesOnly(emp, data) #precos da acao escolhida
	sdChosenCompany = stdDev(pricesChosenCompany)
	#meanChosenStock = meanCalc(pricesOnly)
	#print(sdChosenCompany)
	#print(meanChosenStock)

for company in companies:
	if(company != ticker):
		with open(company+'.SA.csv', 'r') as comp_file:
			comp_reader = csv.DictReader(comp_file)
			for line in comp_reader:
				temp.append([line.pop('Date'), line.pop('Adj Close')])
			pricesComparedCompany = getPricesOnly(temp, data) #precos da acao a ser comparada
			for e in pricesComparedCompany:
				print(e)
				break
			temp = []
			print(meanCalc(pricesComparedCompany))
			#sdComparedCompany = stdDev(pricesComparedCompany)
			#covPrices = covarianceCalc(pricesChosenCompany, pricesComparedCompany)
			#corr = covPrices/(sdChosenCompany*sdComparedCompany)
			#corrDict[ticker+'-'+company] = corr
#print(corrDict)