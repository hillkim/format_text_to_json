#!/usr/bin/python
#hillkim
#modify and use however you wish


#the data has 3 fields country initial,full name, box coordinates
#the script reads the data line by line and formats it to a json object



#output file
d = open("data.json",'w') 

#inital line of the json file
print >>d , "{ \"countries\" :["

#reading the input file(Data.txt)
with open("Data.txt") as f:
    for dataLine in f:
    #print country initial and name
          data= dataLine.split(':')
          print >>d , "{\n\"country\" : "+data[0].strip().replace('\'','\"')+","
          dataAfter=data[1].split(',')
          print >>d ,"\"name\" : "+dataAfter[0].replace('\'','\"').replace('(','')+","

          #print dataAfter
          print >>d , "\"co-ord\":["
          for i in range (1,len(dataAfter)-1):
                  if i!=len(dataAfter)-2:
                       print >>d , dataAfter[i].strip().replace(')','').replace('(','')+","
                  else:
                       print >>d , dataAfter[i].strip().replace(')','').replace('(','')
          print >>d , "]\n},"
#final lines in json file
print >>d , "] }"

