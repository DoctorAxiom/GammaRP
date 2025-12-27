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
			vdis = -adv-1
			return ( (11/12)**vdis - ((11/12)**num)*((10/11)**vdis) )

def percentstr(inputnum):
	retval = inputnum*100
	if retval<0.1:
		return "{\\color{grpneg}"+"{0:.1f}".format(retval)+"\\%}"
	return "{0:.1f}".format(retval)+"\\%"

advrange = range(-6,9)
numrange = range(1,9)

titleline = "\\GRProll{X}{Y} "
for curradv in advrange:
	titleline+="& \\GRProll{X}{"+str(curradv)+"} "
titleline+="\\XX [0.5ex]"
print(titleline)
print("\\hline \\hline")

for numvar in numrange:
	currline="\\GRProll{"+str(numvar)+"}{Y} "
	for advvar in advrange:
		currline+="& "+percentstr(rollprobability(numvar,advvar))+" "
	currline += "\\XX"
	print(currline)