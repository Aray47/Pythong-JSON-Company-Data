import sys
import json
import time
import os

rootDir = ('/Users/Slam/desktop/python/companies')

companyNames = {}

sectorTech = []
sectorEstate = []
sectorEnergy = []
sectorIndust = []
sectorUtil = []

def main():
    print('Loading files.....\n')
    time.sleep(1)
    print('Please Wait....\n')
    getSectors()
    getCompanies()
    mainMenu()
    return(0)

#updating empty dictionary with company information
def getCompanies():
    for dirName, subDirList, fileList in os.walk(rootDir):
        for fname in fileList:
            fname='companies/'+fname
            with open(fname, 'r+', encoding='utf-8') as f:
                data = json.load(f)
            companyNames.update({data['companyName'] : data['symbol']})
            

#loading the program with pre-loaded sectory categories
def getSectors():
    for dirName, subDirList, fileList in os.walk(rootDir):
        for fname in fileList:
            fname='companies/'+fname
            with open(fname, 'r+', encoding='utf-8') as f:
                data = json.load(f)
                if data['sector'] == 'Technology':
                    sectorTech.append(data['symbol'])
                if data['sector'] == 'Real Estate':
                    sectorEstate.append(data['symbol'])
                if data['sector'] == 'Energy':
                    sectorEnergy.append(data['symbol'])
                if data['sector'] == 'Industrials':
                    sectorIndust.append(data['symbol'])
                if data['sector'] == 'Utilities':
                    sectorUtil.append(data['symbol'])


def lookUpStock():
    userSearch = input("Enter a stock symbol to search: ")
    print('\nSearching for %s ....\n' % userSearch)
    time.sleep(1)
    data = json.load(open("companies/%s.json" % userSearch ))
    print('Company Name: %s' % data['companyName'])
    print('Stock Symbol: %s' % data['symbol'])
    print('Description: %s'% data['description'])
    print('CEO: %s'% data['CEO'])
    print('Website: %s'% data['website'])
    mainMenu()

#attempting to look up by name
#pattern searching I found to be the hardest
#part of this assignment
def lookUpName():
    resultNames = []
    userSearch = input('Type a keyword: ')
    for k in companyNames.keys():
        if k is not None:
            if userSearch.find(k):
                print(k)
            else:
                print('no')

#each sector categorized upon selection
def printTech():
    index = 1
    for s in sectorTech:
        print('%d:  %s'%(index,s))
        index +=1
    selection = int(input("Enter selection from menu above:  "))
    if selection > index and not 0:
        print('\nYou selected "%s"' % sectorTech[selection - 1])
        data = json.load(open("companies/%s.json" % sectorTech[selection - 1]))
        print('Company Name: %s' % data['companyName'])
        print('Stock Symbol: %s' % data['symbol'])
        print('Description: %s'% data['description'])
        print('CEO: %s'% data['CEO'])
        print('Website: %s'% data['website'])
    else:
        mainMenu()
    

def printEstate():
    index = 1
    for s in sectorEstate:
        print('%d:  %s'%(index,s))
        index +=1
    selection = int(input("Enter selection from menu above:  "))
    if selection > index and not 0:
        print('\nYou selected "%s"' % sectorEstate[selection - 1])
        data = json.load(open("companies/%s.json" % sectorEstate[selection - 1]))
        print('Company Name: %s' % data['companyName'])
        print('Stock Symbol: %s' % data['symbol'])
        print('Description: %s'% data['description'])
        print('CEO: %s'% data['CEO'])
        print('Website: %s'% data['website'])
    else:
        mainMenu()

def printEnergy():
    index = 1
    for s in sectorEnergy:
        print('%d:  %s'%(index,s))
        index +=1
    selection = int(input("Enter selection from menu above:  "))
    if selection > index and not 0:
        print('\nYou selected "%s"' % sectorEnergy[selection - 1])
        data = json.load(open("companies/%s.json" % sectorEnergy[selection - 1]))
        print('Company Name: %s' % data['companyName'])
        print('Stock Symbol: %s' % data['symbol'])
        print('Description: %s'% data['description'])
        print('CEO: %s'% data['CEO'])
        print('Website: %s'% data['website'])
    else:
        mainMenu()

def printIndust():
    index = 1
    for s in sectorIndust:
        print('%d:  %s'%(index,s))
        index +=1
    selection = int(input("Enter selection from menu above:  "))
    if selection > index and not 0:
        print('\nYou selected "%s"' % sectorIndust[selection - 1])
        data = json.load(open("companies/%s.json" % sectorIndust[selection - 1]))
        print('Company Name: %s' % data['companyName'])
        print('Stock Symbol: %s' % data['symbol'])
        print('Description: %s'% data['description'])
        print('CEO: %s'% data['CEO'])
        print('Website: %s'% data['website'])
    else:
        mainMenu()

def printUtil():
    index = 1
    for s in sectorUtil:
        print('%d:  %s'%(index,s))
        index +=1
    selection = int(input("Enter selection from menu above:  "))
    if selection > index and not 0:
        print('\nYou selected "%s"' % sectorUtil[selection - 1])
        data = json.load(open("companies/%s.json" % sectorUtil[selection - 1]))
        print('Company Name: %s' % data['companyName'])
        print('Stock Symbol: %s' % data['symbol'])
        print('Description: %s'% data['description'])
        print('CEO: %s'% data['CEO'])
        print('Website: %s'% data['website'])
    else:
        mainMenu()

def exitProgram():
    print('See ya later!')
    sys.exit(-1)

def functionBad():
    print("Bad Selection. Menu does not exist.")
    mainMenu()

def lookUpSector():
    print('\n')
    print('Available Sectors ')
    print('     1:  Technology')
    print('     2:  Real Estate')
    print('     3:  Energy')
    print('     4:  Industrials')
    print('     5:  Utilities')
    print('     M: Go back to main menu')

    funcDictionary = {
        '1' : printTech,
        '2' : printEstate,
        '3' : printEnergy,
        '4' : printIndust,
        '5' : printUtil,
        'M' : mainMenu
    }

    uI = input('Enter your choice: ')
    uI = uI.upper()
    funcDictionary.get(uI, functionBad)()

def mainMenu():
    print('\nMain Menu')
    print("     1:  Lookup company by stock symbol")
    print("     2:  Find company by name")
    print("     3:  Find company by sector")
    print("     Q:  Exit/Quit")

    funcDictionary = {
        '1' : lookUpStock,
        '2' : lookUpName,
        '3' : lookUpSector,
        'Q' : exitProgram,
    }

    uI = input('Enter choice from menu above: ')
    uI = uI.upper()
    funcDictionary.get(uI, functionBad)()

if __name__ == '__main__':
    sys.exit(main())