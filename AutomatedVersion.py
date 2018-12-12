#made with Python 3.7.1
#by AirFell

          ##################
     ############################
##########     METHOD 1     ##########
     ############################
          ##################

# This method uses each draw as its own slot,
#   slot 1, slot 2 and slot 3. Each draw is
#   added up from all draw history, then a
#   user-selected timeframe is chosen and
#   multiplied for each draw in that time
#   and subtracted to the entire history
#   tally for each draw per slot, per number.


import csv
import urllib.request

############################################
#####   DOWNLOAD MOST RECENT NUMBERS   #####
############################################

#urllib.request.urlretrieve("http://www.molottery.com/gameHistory.do?method=p3Printout&order=desc", "p3.csv")


#############################
#####   OPEN CSV FILE   #####
#############################

DrawSet = []
tmpList = []

with open('p3.csv', 'r') as NumberFile:
    reader = csv.reader(NumberFile)
    DrawnNumbers = list(reader)

#################################################
#####   Conditional Statements/User Input   #####
#################################################

u = len(DrawnNumbers) - 1
#print (len(DrawnNumbers))

drawRange = int(30 * 2)
drawMultiplier = u - drawRange

#testing junk
#del DrawnNumbers[14:x]
#print ("DrawnNumbers:", DrawnNumbers) 


###############################
#####   Create Draw Set   #####
###############################

for entry in DrawnNumbers:
    if entry[2].isnumeric():
        tmpList.clear()
        counter = 0
        for elem in entry[2:5]:
            tmpList.append(int(elem))
            counter = counter + 1
            if counter == 3:
                DrawSet.append(tmpList.copy())
    else:
        pass

#print ("\n")
#print ("DrawSet:", DrawSet)
#print ("\n")


##############################
#####   GENERATE LISTS   #####
##############################

CDS1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
CDS2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
CDS3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

RDS1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
RDS2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
RDS3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


################################
#####  LONG TERM COUNTER   #####
################################

#####~~~SERIES 1~~~#####
for list in DrawSet:
    dn = list[0]
    if dn == 0:
        CDS1[0] = CDS1[0] + 1
    elif dn == 1:
        CDS1[1] = CDS1[1] + 1
    elif dn == 2:
        CDS1[2] = CDS1[2] + 1
    elif dn == 3:
        CDS1[3] = CDS1[3] + 1
    elif dn == 4:
        CDS1[4] = CDS1[4] + 1
    elif dn == 5:
        CDS1[5] = CDS1[5] + 1
    elif dn == 6:
        CDS1[6] = CDS1[6] + 1
    elif dn == 7:
        CDS1[7] = CDS1[7] + 1
    elif dn == 8:
        CDS1[8] = CDS1[8] + 1
    elif dn == 9:
        CDS1[9] = CDS1[9] + 1
#print ("Output CDS1", CDS1)

#####~~~SERIES 2~~~#####
for list in DrawSet:
    dn = list[1]
    if dn == 0:
        CDS2[0] = CDS2[0] + 1
    elif dn == 1:
        CDS2[1] = CDS2[1] + 1
    elif dn == 2:
        CDS2[2] = CDS2[2] + 1
    elif dn == 3:
        CDS2[3] = CDS2[3] + 1
    elif dn == 4:
        CDS2[4] = CDS2[4] + 1
    elif dn == 5:
        CDS2[5] = CDS2[5] + 1
    elif dn == 6:
        CDS2[6] = CDS2[6] + 1
    elif dn == 7:
        CDS2[7] = CDS2[7] + 1
    elif dn == 8:
        CDS2[8] = CDS2[8] + 1
    elif dn == 9:
        CDS2[9] = CDS2[9] + 1
#print ("Output CDS2", CDS2)

#####~~~SERIES 3~~~#####
for list in DrawSet:
    dn = list[2]
    if dn == 0:
        CDS3[0] = CDS3[0] + 1
    elif dn == 1:
        CDS3[1] = CDS3[1] + 1
    elif dn == 2:
        CDS3[2] = CDS3[2] + 1
    elif dn == 3:
        CDS3[3] = CDS3[3] + 1
    elif dn == 4:
        CDS3[4] = CDS3[4] + 1
    elif dn == 5:
        CDS3[5] = CDS3[5] + 1
    elif dn == 6:
        CDS3[6] = CDS3[6] + 1
    elif dn == 7:
        CDS3[7] = CDS3[7] + 1
    elif dn == 8:
        CDS3[8] = CDS3[8] + 1
    elif dn == 9:
        CDS3[9] = CDS3[9] + 1
#print ("Output CDS3", CDS3)


#print ("\n")

##################################
#####   SHORT TERM COUNTER   #####
##################################


#- Reduce DrawSet down to only the most recent x draws.
#- 2, same process as long term counter, but add a loop to subtract 1 from all
#print ("DrawSet TEST 1:", DrawSet)
DrawSet.reverse()
#print ("DrawSet TEST 2:", DrawSet)
x = len(DrawSet)
del DrawSet[drawRange:x]
#print ("DrawSet TEST 3:", DrawSet)


#####~~~SERIES 1~~~#####
for list in DrawSet:
    dn = list[0]
    if dn == 0:
        RDS1[0] = RDS1[0] + drawMultiplier
    elif dn == 1:
        RDS1[1] = RDS1[1] + drawMultiplier
    elif dn == 2:
        RDS1[2] = RDS1[2] + drawMultiplier
    elif dn == 3:
        RDS1[3] = RDS1[3] + drawMultiplier
    elif dn == 4:
        RDS1[4] = RDS1[4] + drawMultiplier
    elif dn == 5:
        RDS1[5] = RDS1[5] + drawMultiplier
    elif dn == 6:
        RDS1[6] = RDS1[6] + drawMultiplier
    elif dn == 7:
        RDS1[7] = RDS1[7] + drawMultiplier
    elif dn == 8:
        RDS1[8] = RDS1[8] + drawMultiplier
    elif dn == 9:
        RDS1[9] = RDS1[9] + drawMultiplier
#print ("Output RDS1", RDS1)

#####~~~SERIES 2~~~#####
for list in DrawSet:
    dn = list[1]
    if dn == 0:
        RDS2[0] = RDS2[0] + drawMultiplier
    elif dn == 1:
        RDS2[1] = RDS2[1] + drawMultiplier
    elif dn == 2:
        RDS2[2] = RDS2[2] + drawMultiplier
    elif dn == 3:
        RDS2[3] = RDS2[3] + drawMultiplier
    elif dn == 4:
        RDS2[4] = RDS2[4] + drawMultiplier
    elif dn == 5:
        RDS2[5] = RDS2[5] + drawMultiplier
    elif dn == 6:
        RDS2[6] = RDS2[6] + drawMultiplier
    elif dn == 7:
        RDS2[7] = RDS2[7] + drawMultiplier
    elif dn == 8:
        RDS2[8] = RDS2[8] + drawMultiplier
    elif dn == 9:
        RDS2[9] = RDS2[9] + drawMultiplier
#print ("Output RDS2", RDS2)

#####~~~SERIES 3~~~#####
for list in DrawSet:
    dn = list[2]
    if dn == 0:
        RDS3[0] = RDS3[0] + drawMultiplier
    elif dn == 1:
        RDS3[1] = RDS3[1] + drawMultiplier
    elif dn == 2:
        RDS3[2] = RDS3[2] + drawMultiplier
    elif dn == 3:
        RDS3[3] = RDS3[3] + drawMultiplier
    elif dn == 4:
        RDS3[4] = RDS3[4] + drawMultiplier
    elif dn == 5:
        RDS3[5] = RDS3[5] + drawMultiplier
    elif dn == 6:
        RDS3[6] = RDS3[6] + drawMultiplier
    elif dn == 7:
        RDS3[7] = RDS3[7] + drawMultiplier
    elif dn == 8:
        RDS3[8] = RDS3[8] + drawMultiplier
    elif dn == 9:
        RDS3[9] = RDS3[9] + drawMultiplier
#print ("Output RDS3", RDS3)


#print ("\n")

################################
#####   SUBTRACT NUMBERS   #####
################################

outNumS1 = [a - b for a, b in zip(CDS1, RDS1)]
#print ("Set 1 Weighted:", outNumS1)

outNumS2 = [a - b for a, b in zip(CDS2, RDS2)]
#print ("Set 2 Weighted:", outNumS2)

outNumS3 = [a - b for a, b in zip(CDS3, RDS3)]
#print ("Set 3 Weighted:", outNumS3)

#############################
#####   SELECT WEIGHT   #####
#############################
finalNum = []

tempList = outNumS1.copy()
tempList.sort(key=None, reverse=True)
value = tempList[0]
finalNum1 = (outNumS1.index(value))
finalNum.append(finalNum1)
#print (finalNum)

tempList = outNumS2.copy()
tempList.sort(key=None, reverse=True)
value = tempList[0]
finalNum2 = (outNumS2.index(value))
finalNum.append(finalNum2)
#print (finalNum)

tempList = outNumS3.copy()
tempList.sort(key=None, reverse=True)
value = tempList[0]
finalNum3 = (outNumS3.index(value))
finalNum.append(finalNum3)


############################################
#####   PRINT and SAVE Final Numbers   #####
############################################

#print ("\n",)
print ("Your Numbers are: ", finalNum)

WinningNumbers = open("WinningNumbers.txt","w")
WinningNumbers.write(str(finalNum))
WinningNumbers.close()
