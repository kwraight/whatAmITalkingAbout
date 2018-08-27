### glean information from twitter and make plot
import tweepy
from datetime import datetime, date, timedelta
import time
import matplotlib.pyplot as plt
import numpy as np
import argumentClass
import random
import sys
sys.path.insert(0, '../configs/')
import configSettings_ao


###############################
### USEFUL FUNCTIONS
###############################

def CleenTweets(argDict):
    
    api=configSettings_ao.get_api()
    print "\n%%% time check: "+str(datetime.now())
    # get posts
    pageNum=0 #loop over pages
    pageLim=argumentClass.Str2Int(argDict['pages'],"pageLimit")
    count=0
    delArr=[]
    
    while True:
        #retrieve tweets aka status list
        statList=api.user_timeline(id=argDict['who'],page=pageNum) #FriendPpe
        #print "\tpage",pageNum,"size of statList:",len(statList)
        if statList:
            for s in statList:
                if s.created_at < argDict['start'] or s.created_at > argDict['end']:
                    delArr.append(s.id)
        else:
            #print "no statList"
            break

        pageNum+=1
        if pageLim>0 and pageNum>=pageLim:
            break
        print "...next page:",pageNum
        
        
    print "GleanTwitter finds {0} data points in {1} pages ".format(count,pageNum)
    deletes=0
    for d in delArr:
        api.destroy_status(d)
        delete+=1
    print "deleted tweets:",deletes


###############################
### EXECUTE
###############################

def main():
    print ">>>someTools running..."

    plotDict=copy.deepcopy(argumentClass.templatePlotDict)
    ### get the inputs
    args = argumentClass.GetArgs()
    #print args
    
    ### set parameters
    for p in plotDict.keys():
        for k in vars(args).iteritems():
            if p in k[0] and not k[1]==None:
                print "got",k
                plotDict[p]=k[1]

    print argDict

    CleenTweets(argDict)
    print ">>>someTools finished."

if __name__ == "__main__":
    main()
    exit()



