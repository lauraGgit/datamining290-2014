#!/usr/bin/python
"""This script can be used to analyze data in the 2012 Presidential Campaign,
available from ftp://ftp.fec.gov/FEC/2012/pas212.zip - data dictionary is at
http://www.fec.gov/finance/disclosure/metadata/DataDictionaryContributionstoCandidates.shtml
"""

import fileinput
import csv

total = 0.0
rows = 0
candidates = []
contributions = []
minimum = 0
maximum = 0
for row in csv.reader(fileinput.input(), delimiter='|'):
    if not fileinput.isfirstline():
        total += float(row[14])
        rows += 1
        ###
        # TODO: calculate other statistics here
        # You may need to store numbers in an array to access them together
        ##/
        ## Push candidate id
        if (float(row[14]) < minimum):
            minimum = float(row[14])
        if (float(row[14]) > maximum):
            maximum = float(row[14])
        candidates.append(row[16])
        contributions.append(row[14])
print minimum
###
# TODO: aggregate any stored numbers here
#

mean = total/rows
contributions.sort()
conlen = len(contributions)
print conlen
medval = ((conlen+1)/2)
#print contributions[conlen]
if (conlen % 2) == 0:

    median = (contributions[medval - 1.5] + contributions[medval - 0.5])/2
else:
    median = contributions[medval-1]

## Calc Standard Deviation
sdSum = []
for s in contributions:
    num = (float(s) - mean)**2
    sdSum.append(num)
sdNumerator = sum(sdSum)
standDev = (sdNumerator/conlen)**0.5

## Sort and print candidates
uniqueCandidates = list(set(candidates))
uniqueCandidates.sort()
CandidatesStr = ""
for i in range(len(uniqueCandidates)):
    if (i != len(uniqueCandidates)):
        CandidatesStr += str(uniqueCandidates[i])+ ", "
    else:
        CandidatesStr += str(uniqueCandidates[i])

##### Print out the stats
print "Total: %s" % total
print "Minimum: " + str(minimum)
print "Maximum: " + str(maximum)
print "Mean: " + str(mean)
print "Median: " + str(median)
# square root can be calculated with N**0.5
print "Standard Deviation: " + str(standDev)

##### Comma separated list of unique candidate ID numbers
print "Candidates: " + CandidatesStr

def minmax_normalize(value):
    """Takes a donation amount and returns a normalized value between 0-1. The
    normilzation should use the min and max amounts from the full dataset"""
    ###
    # TODO: replace line below with the actual calculations
    norm = (value - float(minimum))/(float(maximum)-float(minimum))

    ###/

    return norm

##### Normalize some sample values
print "Min-max normalized values: %r" % map(minmax_normalize, [2500, 50, 250, 35, 8, 100, 19])

### Extra Credit ### z-scores
## I am only printing the first and last thousand contributions because it otherwise dominates the output.
def zScore(lst, xBar, sD):
    zScores = []
    for i in lst:
        score = round(((float(i) - mean) / standDev),4)
        zScores.append(score)
        zScores.sort()
    print zScores

print "Z-scores for first 1000 contributions: "
zScore(contributions[:999], mean, standDev)
print "Z-scores for last 1000 contributions: "
zScore(contributions[-999:], mean, standDev)



