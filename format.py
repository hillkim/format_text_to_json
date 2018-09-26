#!/usr/bin/python


#print "give me a bottle of rum!"

#mock = "'AF': ('Afghanistan', (60.5284298033, 29.318572496, 75.1580277851, 38.4862816432)),"
#print mock
d = open("output.json",'w')
#print >>d, 'whatever'     # Python 2.x
#print('whatever', file=f) # Python 3.x

print >>d , "{ \"countries\" :["
with open("Data.txt") as f:
    for dataLine in f:
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
print >>d , "] }"

#for element in l:
 #   parts = element.split(',')
    #print parts
