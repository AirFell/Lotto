#made with Python 3.7.1
#by AirFell

          ##################
     ############################
##########     METHOD 2     ##########
     ############################
          ##################

# This method uses each number 000-999 as its own
#   number to be tallied when drawn. It will then
#   run stats in the same way as Method 1.


import csv
import urllib.request

############################################
#####   DOWNLOAD MOST RECENT NUMBERS   #####
############################################

urllib.request.urlretrieve("http://www.molottery.com/gameHistory.do?method=p3Printout&order=desc", "p3.csv")


######################################
#####   Conditional Statements   #####
######################################

drawRange = int(input("Enter recent draw history time range in days:") * 2)
drawMultiplier = int(input("Enter strenth of recent draw history against all history:"))
#30 days at 22x recommended.

#############################
#####   OPEN CSV FILE   #####
#############################

DrawSet = []
tmpList = []

with open('p3.csv', 'r') as NumberFile:
    reader = csv.reader(NumberFile)
    DrawnNumbers = list(reader)


###################################################
#####   This is here to make testing easier   #####
###################################################

#x = len(DrawnNumbers)
#del DrawnNumbers[14:x]
#print ("DrawnNumbers:", DrawnNumbers) 


###############################
#####   Create Draw Set   #####
###############################

for entry in DrawnNumbers:
#    print ("Entry:", entry[2:5])
    if entry[2].isnumeric():
        tmpList.clear()
        threeDigit = str()
        counter = 0
        for elem in entry[2:5]:
            threeDigit = threeDigit + str(elem)
#            print ("3 Digit:", threeDigit)
            counter = counter + 1
            if counter == 3:
                tmpList.append(int(threeDigit))
#                print ("tmpList:", tmpList)
                DrawSet.append(tmpList.copy())
    else:
        pass

#print ("\n")
#print ("DrawSet:", DrawSet)
#print ("\n")


##############################
#####   GENERATE LISTS   #####
##############################

CDS1 = []
cds1Count = int(1000)
while cds1Count > 0:
    CDS1.append(int(0))
    cds1Count = cds1Count - 1
print (len(CDS1))

RDS1 = []
rds1Count= int(1000)
while rds1Count > 0:
    RDS1.append(int(0))
    rds1Count = rds1Count - 1
print (len(RDS1))

#stopped here, we now have each entry as an individual 3 digit number.
#need to next figure out how to iterativly compare each number to the list and
#count one when they match.

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

print ("\n")

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

print ("\n")

################################
#####   SUBTRACT NUMBERS   #####
################################

outNumS1 = [a - b for a, b in zip(CDS1, RDS1)]
#print ("Set 1 Weighted:", outNumS1)

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


############################################
#####   PRINT and SAVE Final Numbers   #####
############################################

print ("\n",)
print ("Your Numbers are: ", finalNum)

WinningNumbers = open("WinningNumbers.txt","w")
WinningNumbers.write(str(finalNum))
WinningNumbers.close()
