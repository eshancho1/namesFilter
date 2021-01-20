import csv, sqlite3

def csvtolst(x):
  lst=[]
  with open(x,'r') as f:
    read=csv.reader(f)
    for line in read:
      lst.append(line)
  return lst

data=csvtolst('pbn.csv')

def filterFem(x):
  lst=[]
  for line in x:
    if line[1]=='FEMALE' and line[2]=='BLACK NON HISPANIC':
      if float(line[5])<8 and line[0] == '2015':
        lst.append(line)
  return lst
data2 = filterFem(data)

def pielst():
  l = []
  l2 = []
  l3 = []
  for line in data2:
    l.append(line[3])
  for line in data2:
    l2.append(line[4])
  l3.append(l)
  l3.append(l2)
  return l3

def makeDictionary(key, value):
  d = {}
  i = -1
  for keys in key:
    i += 1
    d[keys] = value[i]
  return d

def piegraph():
  l = []
  l2 = []
  l3 = []
  for line in data2:
    l.append(line[3])
  for line in data2:
    l2.append(line[4])
  l3.append(l)
  l3.append(l2)
  return makeDictionary(l,l2)

def filterMale(x):
  lst=[]
  for line in x:
    if line[1]=='MALE' and line[3] == 'JASON':
      if line[0]=='2012':
        lst.append(line)
  return lst
data3 = filterMale(data)


def linegraph():
  l = []
  l2 = []
  for line in data3:
    l.append(line[2])
  for line in data3:
    l2.append(line[4])
  return makeDictionary(l,l2)



connection = sqlite3.connect('graphs.db')
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS tabloost" + "('year','gender','race', 'name', 'count', 'rank')")

def csvdb(file):
    with open(file) as f:
        boost = csv.reader(f)
        for line in boost:
          print(line[5])
          data.execute("INSERT INTO tabloost VALUES (?,?,?,?,?,?)", (line[0],line[1], line[2], line[3], line[4], line[5]))
        connection.commit()
        cursor.execute("SELECT * FROM tabloost")
        print(cursor.fetchall())


