#age=int(input("Enter Your age:"))
#if age>=18:
    #print("You can play the game")
#else:
    #print("You cant play the game")

#ekhon jodi kono user inter ar jaigai string input dei tokon error create hobe.ar ei error handle korar jonno first a try use korte hobe.otthat amr bujte hobe kon jaigai user wrong input dite pare seikhane try use korte hohbe.

while True:
    try:
      age2=int(input("Enter your age:")) #jodi eikhane wrong input 
    #dei tahole expect a chole jabe and expect a ja ace seita show 
    #korbe.but try te jodi correct input dei tahole direct code 
    #jabe. expect a jabe na
      break


    except:
      print("Invalid input...")



if age2>=18:
    print("you can play the game")
else:
    print("You cant play the game") 
#but ei khetre prblm ace jodi wrong input dei tahole age2 a kono value save hobe na then expect function a ja ace seita print korar por jokon niche ase age2 te kono value pabe na tokon error dekhabe.tai amdr emn kisu korte hobe jate jotokon pojonto wrong input dei totokon pojonto jate niche na ase.sei khetre amra while loop use korte pare jeta ekhon upore use korbo.while loop totokon cholbe jotokhon input wrong hobe.input sothik holei while break kore code chole asbe          