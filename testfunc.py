# this is just a utility script where I write stuff to help me quickly generate repetetive tex

def rollprobability(num, adv):
	if adv==0:
		return 1-((11.0/12.0)**num)
	elif adv>0:
		return 1-( ((12.0-adv)/12.0)**num )
	else:
		if num+adv<0:
			return 0
		else:
			return ( 1-((11.0/12.0)**num) )

def percentstr(inputnum):
	retval = inputnum*100

	return "{0:.1f}".format(retval)

advrange = range(-5,5)
numrange = range(1,11)

titleline = "\\GRProll{X}{Y}"
for curradv in advrange:
	titleline+="& \\GRProll{X}{"+str(curradv)+"}"
titleline+="\\XX [0.5ex]"
print(titleline)
print("\\hline \\hline")

for numvar in numrange:
	currline="\\GRProll{"+str(numvar)+"}{Y} "
	for advvar in advrange:
		currline+="& "+percentstr(rollprobability(numvar,advvar))+"\\% "
	currline += "\\XX"
	print(currline)