''' PYTHON SMALL PROGRAMS '''


#OTP Generation,Lucky Draw
'''import random
count=0
while True:
  try:
    x=int(input("enter range:"))
    for y in range(x):
      count+=1
      z=random.randint(1,200)
      if z==143:
        print('Congratulations U Got It - ***I LOVE U*** - number= ',z)
        print('Your Lucky Count Is--',count)
        break
      else:
        print("Better Luck Next Time = ",z)
    if z==143:
      break
  except:
    print("enter digits only!")'''

#Generating The Required Length Of Number
'''while True:
  try:
    x=int(input("enter the required length of the number u want:"))
    for y in range(x):
      print(random.randint(0,9),end="")
    print()
  except:
    print("enter digits only!")'''

#Finding The Temperature Of Cities
'''while True:
  import requests

  ad='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
  try:
    city=input('city')
    url=ad+city
    json_data=requests.get(url).json()
    #print(json_data)
    print(json_data['name'],'Have The Country Code',json_data['cod'],'And The Temperature Is',json_data['main']['temp'],sep=" ")
  except:
    print("There Is No Such City.Please Check Once!")'''

#Finding The Index Of A Same Character
'''x=list(input("enter list :"))
while True:
  try:
    a=input("enter common num :")
    b=int(input("enter which common number index :"))
    count=0
    for y,z in enumerate(x):
      if z==a:
        count+=1
        if count==b:
          print(y)
  except:
        print("enter correct number") '''

#Print Statement
'''while True:
  c=input("enter what u wanna add :")
  x=[]
  x.append(c)
  for y in x:
    a,b=len(y),len(y)-2
    print(y[0],y[a-1],sep="-"*b)'''

#Smart Python Questions
'''import re
print(chr(ord('e')+1))
print('a@ 1, '.islower( ))
sen='a b c'
matched=re.match(r'(.*) (.*?) (.*)',sen)
print(matched.group(2))'''

# Hello World program in Python
    
'''inp = input()
def main():
    output = ''
    for letter in inp:
        letter = letter.upper()
        if letter == 'A':
            output += 'T'
        elif letter == 'T':
            output += 'A'
        elif letter == 'G':
            output += 'C'
        else:
            output += 'G'

    print(output[::-1])
main()'''

 
'''x=[]
def main():

 # Write code here 
    i=int(input())
    x.append(i)
for i in range(3):
    main()
print(max(x)) '''

'''def makeInc(x):
  def inc(y):
    return x,y
  return inc
incOne = makeInc(1)
incFive = makeInc(5)
print(incOne(2)) # returns 6
print(incFive(3))'''

'''def raj(a="raj"):
  print(a)
raj(a="hi")'''

'''def cursing(depth):
  try:
    cursing(depth + 1) # actually, re-cursing
  except RuntimeError as RE:
    print('I recursed {} times!'.format(depth))
cursing(5)'''


#Fibonacci Series (Task1)
'''def Fibonacci(par):
    C= [string.count(x) for x in set(par)] #To Make The Elements To Be Unique And Thier Counts
    C.sort()
    flag = 1 #To change The Value
    if len(C) < 3:
        return 'Dynamic'
    for y in range(len(C)-1, 1, -1): #Looping Based On Top Value From Last Element Of List
      if C[y] != C[y-1] + C[y-2]: #Checking Conditions Regarding Equals Or Not
        flag = 0
        break
    #print(flag)
    if flag == 1:
        return 'Dynamic'
    else:
        return 'Not'
Result = "" 
try: #To Try The Error and To Catch The Error
  T = int(input("Enter The Testcases You Want:"))#Number Of Testcases
  if T>1 and T<10:
    for i in range(T):
      string = input("Enter The String:")#String With Lowercase As Input
      if string.islower() and len(string)<10**5:
        Result += Fibonacci(string)+'\n'         #Function Calling
      else:
        print("Enter Lowercase only!")
  else:
    print("Enter Range between 1 and 10 only!")
except:
  print("Please Enter Valid Input Only!") # To Solve The Error Problem
print(Result)'''

#Bear and Milky Cookies(Task4)
'''
a=[]
try: #To Try The Error and To Catch The Error
  T = int(input("Enter The Testcases You Want:")) #Number Of Testcases
  if T>=1 and T<50:
    for i in range(T):
      N=int(input("Enter The No Of Minutes :")) #Number Of Minutes
      if N>=1 and N<50:
        for j in range(N):
          k=input("Enter Your Choice Cookie or Milk:") #Choosing Cookie or Milk
          a.append(k) #Adding The Choices To List
        print(' '.join(a)) # List Of Elements With Spaces
        d=len(a)
        if (d==1 and a[0]=="cookie"): #1st Possible Way Of Conditions
          print("No")
        elif (d==1 and a[0]=="milk"): #2nd Possible Way of Condition
          print("Yes")
        elif (a[0]=="cookie" and a[1]=="cookie") or (a[0]=="milk" and a[1]=="cookie") or (all(a[0]=='milk' for x in range(len(a)-1))==True) and (a[-1]=='cookie'): #3rd lly
          print("No")
        elif (all(x==a[0] for x in a)==True): #4th Simlilarly
          print("Yes")
        else:
          print("Yes")
        a=[] #To Make The List Again Empty For New Items Means It Overrides Previous Values
      else:
        print("Enter Range between 1 and 50 only!")
  else:
    print("Enter Range between 1 and 50 only!")
except:
  print("Enter Valid Data Only!")  # To Solve The Error Problem'''


#Gross Salary(Task10)
'''try: #To Try The Error and To Catch The Error
  T = int(input("Enter The Testcases You Want:")) #Number Of Testcases
  if T>=1 and T<1000:
    for i in range(T):
      Sal=int(input("Enter Your Salary :")) #Salary details
      if Sal>=1 and Sal<=100000:
        if Sal<1500: #Checking The Conditions Based On Salary
          M=int(input("Enter Your HRA Percentage :")) #HRA Percentage
          K=int(input("Enter Your DA Percentage :")) #DA Percentage
          HRA=(Sal*M)/100
          DA=(Sal*K)/100
          GS=Sal+HRA+DA  #Total Gross Salary
          print(GS)
        elif Sal>=1500: #Checking The Conditions Based On Salary
          K=int(input("Enter Your DA Percentage :")) #DA Percentage
          HRA=500
          DA=(Sal*K)/100
          GS=Sal+HRA+DA  #Total Gross Salary
          print(GS)
      else:
        print("Enter The Salary Between 1 and 100000!")
  else:
    print("Enter The Range Between 1 and 1000 only!")
except:
  print("Enter Valid Data Only!") # To Solve The Error Problem'''

#Task4 Method2
'''import random
b=['cookies','milk']
a=[]
T = int(input("Enter The Testcases You Want:"))
if T>=1 and T<50:
  for i in range(T):
    N=int(input("Enter The No Of Minutes :"))
    if N>=1 and N<50:
      for j in range(N):
        a.append(random.choice(b))
      print(' '.join(a))
      d=len(a)
      if (d==1 and a[0]=="cookies"):
        print("No")
      elif (d==1 and a[0]=="milk"):
        print("Yes")
      elif (a[0]=="cookies" and a[1]=="cookies") or (a[0]=="milk" and a[1]=="cookies") or (all(a[0]=='milk' for x in range(len(a)-1))==True) and (a[-1]=='cookies'):
        print("No")
      elif (all(x==a[0] for x in a)==True):
        print("Yes")
      else:
        print("Yes")
      a=[]
    else:
      print("Enter Range between 1 and 50 only!")
else:
  print("Enter Range between 1 and 50 only!")'''

'''import sys
f=[]
try:
  T = int(sys.stdin.readline()) #Number Of Testcases
  if T>=1 and T<100:
    for i in range(T):
      b=sys.stdin.readline()
      a=b.split()
      for y in range(int(a[-1])):
        if(y%2==0):
          if f==[]:
            c=2*int(a[0])
            f.append(c)
          else:
            f[0]=2*f[0]
        else:
          c=2*int(a[1])
          if len(f)==1:
            f.append(c)
          else:
            f[1]=2*f[1]
      print(max(f)//min(f))
      f=[]
      a=[]
  else:
    print("Enter The Range Between 1 and 100 only!")
except:
  print("Enter The Valid Data only!")'''


''' import sys
try: #To Try The Error and To Catch The Error
  T = int(sys.stdin.readline()) #Number Of Testcases
  if T>=1 and T<50:
    for i in range(T):
      b=sys.stdin.readline()
      a=b.split()
      d=len(a)
      if (d==1 and a[0]=="cookie"): #1st Possible Way Of Conditions
        print("No")
      elif (d==1 and a[0]=="milk"): #2nd Possible Way of Condition
        print("Yes")
      elif (a[0]=="cookie" and a[1]=="cookie") or (a[0]=="milk" and a[1]=="cookie") or (all(a[0]=='milk' for x in range(len(a)-1))==True) and (a[-1]=='cookie'): #3rd lly
        print("No")
      elif (all(x==a[0] for x in a)==True): #4th Simlilarly
        print("Yes")
      else:
        print("Yes")
      a=[]
  else:
    print("Enter Range between 1 and 50 only!")
except:
  print("Enter Valid Data Only!")  # To Solve The Error Problem '''


#Iteration Through Nested Lists
''' x=[1,2,[3,4,5],6,7,[8,9],10]
for i in x:
    if isinstance(i,list):
        for j in i:
            print(j)
    else:
        print(i) 

 # 1st Method
for y in x:
    if type(y)==list:
        for z in y:
            print(z)
    else:
        print(y)

 # 2nd Method
for y in x:
    try:
        for z in y:
            print(z)
    except:
        print(y) '''

#To Print List Of Items In Matrix Format
''' x=[0,1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1,0]
count=0
for i in x:
    count+=1
    if(count%4==0):
        print(i)
    else:
        print(i,end=' ')


#### OUTPUT  #####

    0 1 2 3
    4 5 6 7
    8 9 9 8
    7 6 5 4
    3 2 1 0  '''

# Taking The keypad Numbers as Input and Inser Into Files
''' fl=open('words.txt')
m=fl.read()
dic={1:'abc',2:'def',3:'ghi',4:'jkl',5:'mno',6:'pqr',7:'stu',8:'vwx',9:'yz'}
user=input('enter a number')
emplist=['']
emplist1=[]
for x in user:
    let=dic[(int(x))]
    emplist=[pet+lets for pet in emplist for lets in let]
print(emplist)
print(len(emplist))
for p in emplist:
    if p in m:
        emplist1.append(p)
for index,word in enumerate(emplist1):
    print(index,'-',word)  '''

# Employee Spendings depends on User Input
'''name=input("enter employee name:")
salary=int(input("enter employee salary:"))
d={}
d["name"]=name
d["salary"]=salary
while(True):
    exp1=input("enter what expense:")
    if exp1=="q":
        break
    amount=int(input("enter amount:"))
    if amount<salary:
        d[exp1]=amount
        tot=salary-amount
        d["rembal"]=tot
        print(tot)
    else:
        print("insufficient balance")
               
print(d)      '''


#Random Password Generator
''' import random
import string
pwd = ""
count = 0
length = int(input("How many characters would you like in your password? "))

while count != length:

  upper = [random.choice(string.ascii_uppercase)]
  lower = [random.choice(string.ascii_lowercase)]
  num = [random.choice(string.digits)]
  symbol = [random.choice(string.punctuation)]
  everything = upper + lower + num + symbol

  pwd += random.choice(everything)
  count += 1
  

if count == length:
  print (pwd)    '''


# Highest length of word in sentence
''' s='Hie Welcome To Python World'
x=s.split()
c=[]
d=[]
for y in x:
    for b in x:
        if len(y)>len(b):
            if b not in c:
                c.append(b)
print(c)    
for y in x:
    if y not in c:
        d.append(y)
print(d) '''

# Lowest length of word in sentence
''' s='Hie Welcome To Python World Rajasekhar'
x=s.split()
c=[]
d=[]
for y in x:
    for b in x:
        if len(y)>len(b):
            if y not in c:
                c.append(y)
    
for y in x:
    if y not in c:
        d.append(y)
print(d) '''

#To Plot a graph Depending on Csv File Data of Perticular People of Everyone
''' import csv
from collections import Counter
import matplotlib.pyplot as plt
with open('C:/Users/USER/assignment.csv',newline='') as csvfile:
    reader=csv.reader(csvfile)
    next(reader)
    if(reader!=''):
        for row in reader:
            d={}
            c=[]
            for row1 in row[1:]:
                d[row1]=d.get(row1,0)+1
                if row1 is not int and row1!='':
                    c.append(int(row1))
                elif row1 is str:
                    pass
                    
            #print(c)
            rep=Counter(c)
            print(rep)
            repnum=[]
            for i in rep:
                repnum.append([i,rep[i]])
            plt.bar([row[0] for row in repnum],[row[1] for row in repnum])
            plt.axis([0,5,0,20])
            plt.show()
            plt.title(label=row[0])
    else:
        pass    '''


#To Print The List Of Numbers From High to Low From Right and Left
''' Input -> l1=[9,2,3,8,5,1,4,6,0,11,13,52]     and Output -> [52, 11, 8, 5, 3, 1, 0, 2, 4, 6, 9, 13]
a=len(l1)
b=1
for x in range(0,a-1):
    if(x%2==0):
        if(x==0):
            l1.sort(reverse=True)
            print(l1)
        elif(x>=2):
            a=a-1
            l3=l1[b:a]
            l3.sort(reverse=True)
            l1[b:a]=l3
            print(l1)
    else:
        if(x==1):
            l2=l1[x:a]
            l2.sort()
            l1[x:a]=l2
            print(l1)
        elif(x>=3):
            b=b+1
            l4=l1[b:a]
            l4.sort()
            l1[b:a]=l4
            print(l1)   '''



#### Seperating Every Two words Of String with Spaces and print Two words per line ########
            
#x='hyderabad,namrathaestates,ameerpet,pin-500018,gyhgyhyy,sai,girish,ram,chandu,vamsi,odd,even,sekhar,raj,fasak'
'''output --- hyderabad namrathaestates
            ameerpet pin-500018
            gyhgyhyy sai
            girish ram
            chandu vamsi
            odd even
            sekhar raj
            fasak '''
            
#sol-
# x=x.split(',')
# ln=len(x)
# # print(ln)
# for a,y in enumerate(x):
#     try:
#         # print(a)
#         if a%2==0:
#             print(x[a],x[a+1])
#         else:
#             pass
#     except:
#         pass

# else:
#     if ln % 2 != 0:
#         print(x[ln-1])
#     else:
#         pass




