import numpy
#Expected Output is 0
t6 = 0
#Actual Output
o6 = 0.8387
#Output Error:
err6 = o6*(1-o6)*(t6-o6)
#print err6
#Setup hidden node 5
o5 = 0.9933
w56 = 1.5
#Error for node 5
err5 = o5*(1-o5)*(err6*w56)
#print err5
#Adjust weight w56
l = 10 # learn rate
w56 = w56 + l*err6*o5 
#print w56

weight = numpy.matrix([[0,0,-3,2,4,0],[0,0,2,-3,0.5,0],[0,0,0,0,0,0.2],[0,0,0,0,0,0.7],[0,0,0,0,0,1.5]])
o = [1,2,0.7311,0.0179,0.9933,0.8387]

def backwardProp(wMat, learnRate, t, out):
	last = out[len(out)-1]
	err6 = last*(1-last)*(t-last)
	print "err_6 = " + str(err6)
	last_err = err6
	for i in range(len(wMat), 0, -1):
		err = 0
	 	for j in range (6):
	 		if wMat[i-1, j] != 0:
	 			currWeight = wMat[i-1, j]
	 			aOut = out[i-1]
	 			err += aOut*(1-aOut)*(last_err*currWeight)
	 			actWeight = currWeight + learnRate*last_err*aOut
	 			print "w_"+str(i)+str(j+1)+" = "+str(actWeight)
	 	print "err_"+str(i) +"= "+str(err)
	 	last_err = err
	 			



backwardProp(weight, l, t6, o)