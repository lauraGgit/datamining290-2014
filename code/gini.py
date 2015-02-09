#!/usr/bin/python
"""Script can be used to calculate the Gini Index of a column in a CSV file.

Classes are strings."""

import fileinput
import csv
import collections

(
    CMTE_ID, AMNDT_IND, RPT_TP, TRANSACTION_PGI, IMAGE_NUM, TRANSACTION_TP,
    ENTITY_TP, NAME, CITY, STATE, ZIP_CODE, EMPLOYER, OCCUPATION,
    TRANSACTION_DT, TRANSACTION_AMT, OTHER_ID, CAND_ID, TRAN_ID, FILE_NUM,
    MEMO_CD, MEMO_TEXT, SUB_ID
) = range(22)

CANDIDATES = {
    'P80003338': 'Obama',
    'P80003353': 'Romney',
}

############### Set up variables
# TODO: declare datastructures
votes = []
aZip = collections.defaultdict(list)
############### Read through files
for row in csv.reader(fileinput.input(), delimiter='|'):
    candidate_id = row[CAND_ID]
    if candidate_id not in CANDIDATES:
        continue

    candidate_name = CANDIDATES[candidate_id]
    zip_code = row[ZIP_CODE]
    ###
    # TODO: save information to calculate Gini Index
    ##/
    votes.append(candidate_name)
    aZip[zip_code].append(candidate_name)


###
# TODO: calculate the values below:
gini = 0  # current Gini Index using candidate name as the class


def calcGini(vList):
    vCount = collections.Counter()
    vCount.update(vList)
    vDict = dict(vCount)
    gSum = sum(vDict.values())
    gFrac = 0
    for cand in vDict:
        gFrac += (float(vDict[cand])/float(gSum))**2
    return 1 - gFrac

gini = calcGini(votes)

split_gini = 0  # weighted average of the Gini Indexes using candidate names, split up by zip code
##/
gzip = []
totalContr = float(len(votes))
for z in aZip:
    weight = float(len(aZip[z]))/totalContr
    gIndex = calcGini(aZip[z])
    gzip.append((gIndex*weight))
split_gini = sum(gzip)

print "Gini Index: %s" % gini
print "Gini Index after split: %s" % split_gini


### how many romeney/obama contributions per zipcode
### 2 classes one 
### 1.) just evaluate average contibutions overall gine
## 2. ) calculate gini for each zip sum up gini across zips 
###     then goes there
### extra credit:
#### zip code where to break point < less than for partition by zipcode


