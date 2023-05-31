def	readfile(filepath):
	file_object = open(filepath)
	try:
		all_the_text = file_object.read( )
	finally:
		file_object.close( )
	if  all_the_text:

		return all_the_text
	else:
		return False




def  procToMatix(s):
	retMatrix=[]
	ilist=s.split("\n")
	for each in ilist[:-1]:
		jlist=each.split("\t")
		zlist=[]
		for  x in jlist[:-1]:
			zlist.append(float(x))
		retMatrix.append(zlist)

	return retMatrix



def  readData(filepath):
	text=readfile(filepath)

	fmatrix=procToMatix(text)

	return fmatrix