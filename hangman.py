import random


print("Its Hangman World :]")
print("enter the number of words stages you wanted to play must be greater than 3")
print("note:-made it below 10")


Stage=int(input())



if(3< Stage <=15):
  words=[]
  i=0
  
  '''input'''
  
  global point
  point=0

  num=[]
  global health
  health=3


  l=1 
  for x in range(Stage):
      print("enter the word:-"+str(l))
      words.append(input())
      l=l+1


  """Combining"""

  
  def combine(valu):
    str=" "
    return str.join(valu)

  def realcombine(valu):
    str=""
    return str.join(valu) 


  """Spliting"""


  def split(inpput):
    return list(inpput)



  """Stats printing"""


  
  def point_table(point_value,health_value):
    print("")
    print("")
    print("")

    print("")
    print("                                       your point:="+str(point_value))
    print("                                       your health:="+str(health_value))
    print("")



  """Main function"""


  def main(value):
    spliting=split(value)
    word=realcombine(value)
    z=len(value)
    delet=int(z/2)
    for x in range(delet):
      ran=random.randint(1,(z-1))
      remov=spliting.pop(ran)
      prin=spliting.insert(ran,"_")
      
    finalll=combine(spliting)
    print(finalll)
    print("Enter the full word to fill the blank to gain point")
    three=input()
    
    if (three==word):
      global point
      global health
      point=point+1
      point_table(point,health)
      
      
    else:
      if health==0:
        print("")
        print("")
        print(".....................................................")
        print(".....................................................")
        print(".....................................................")
        print(".....................................................")
        print(".....................................................")
        print("OOPSSS Your Health is Zero :[")
        print("Exiting from game :[ ........")
        print(".....................................................")
        print(".....................................................")
        print(".....................................................")
        print(".....................................................")
        quit()
      
      health=health-1
      point_table(point,health)  


       

          
  print(".....................................................")
  print(".....................................................")
  print(".....................................................")
  print(".....................................................")
  print(".....................................................")
  print("           Lets begin the Hangman game               ") 
  print(".....................................................")
  print(".....................................................")
  print(".....................................................")
  print(".....................................................")
  print(".....................................................")  
  print("       here are the words to fill and gain point     ")   
  print(".....................................................")
  print(".....................................................")
  print(".....................................................")  
  print("")
  print("                                       your point:= 0")
  print("                                       your health:="+str(health))

 
  wordno=0
  for x in range(Stage):
      wordno=wordno+1
      f=words[x]
      k=len(f)
      if (k<3):
        print("")
        print("")
        print(".....................................................")
        print(".....................................................")
        print("Word Number"+str(wordno))
        print("invalid- this word is less than 3")
        break
      elif (k>15):
        print("")
        print("")
        print("Word Number"+str(wordno))
        print(".....................................................")
        print("invalid- any word is greater than 20")
        break
      elif (k>2) :
        print("")
        print("")
        print("Word Number"+str(wordno))
        print("")
        main(f)
  

  print(".....................................................")
  print(".....................................................")
  print(".....................................................")
  print(".....................................................")
  print(".....................................................")
  print("             THANKS FOR PLAYING THE GAME             ")
  print(".....................................................")
  print(".....................................................")
  print(".....................................................")
  print(".....................................................")
  print(".....................................................")        
  
     
  
  
else:
  print("Hangman's criteria not fully filled :[")
  print("Exiting from game :[ ........")
