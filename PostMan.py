str=''
h={}
o=[]
while(str!='x'):
    str=input()
    l=str.split()
    if(str!='x'):
        h[l[1]]=int(l[0])
index_i=-1
index_j=-1
rows=0
cols=0
if('SE' in h):
    cols = cols + h['SE']
if('NE' in h):
    cols+= h['NE']
if('E' in h):
    cols+=+ h['E']
if('SE' in h):
    rows=rows+h['SE']
if('S' in h):
    rows = rows + h['S']

l=[[' 'for j in range(cols)] for i in range(rows)]
i=0
j=0
for p in h:{
    if(p=='E'):
        i+=1
}
for i in range(rows):
    for j in range(cols):
        print(l[i][j],end=' ')

    print('\n');
