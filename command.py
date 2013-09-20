import sys,commands,json,os

ss=commands.getoutput("cat text.txt|grep 'CH'")

sa = ss.split('\n')

arr = []

for i in sa:


    cut_name = str(i).split(':')
    name = cut_name[0]
    value = cut_name[1]
    va = value.strip().split('  ')
    val = []
    for j in va: 
         agr = str(j).strip().split('=')
         s = '"%s":"%s"' % (agr[0],agr[1])
         val.append(s)
    xx = '"%s":{%s}' % (name,(''.join([ '%s,' % vv for vv in val ])[:-1] ))
    arr.append(xx)


  
netsense = ('{%s}' % (''.join([ '%s,' % ii for ii in arr ])[:-1]))
wf = open('data.json','wb')
wf.write(netsense)
wf.close()

with open("data.json") as file:
    data = json.load(file)
file.close()
"""
#put = raw_input()

x = put.split(' ')

if len(x)==1:
	 print "IRMS : %s , VRMS : %s ,POW : %s, VA : %s,AActE : %s,AppE : %s" % (data['%s' % str(x[0])]['IRMS'],data['%s' % str(x[0])]['VRMS'],data['%s' % str(x[0])]['POW'],data['%s' % str(x[0])]['VA'],data['%s' % str(x[0])]['AActE'],data['%s' % str(x[0])]['AppE'])
elif len(x)==2:
	print "%s : %s" % (str(x[1]),data['%s' % str(x[0])]['%s' % str(x[1])])
"""

if len(sys.argv) ==1:
	print ss
elif len(sys.argv) ==2:
	 print "IRMS : %s , VRMS : %s ,POW : %s, VA : %s,AActE : %s,AppE : %s" % (data[sys.argv[1]]['IRMS'],data[sys.argv[1]]['VRMS'],data[sys.argv[1]]['POW'],data[sys.argv[1]]['VA'],data[sys.argv[1]]['AActE'],data[sys.argv[1]]['AppE'])
		
elif len(sys.argv) ==3:
	print "%s" % (data[sys.argv[1]][sys.argv[2]])
else:
	print "Try agrian please!"