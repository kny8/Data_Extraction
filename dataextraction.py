import wikipedia

#Topic of their interest: ex- politics, art, literature, music etc
print("Choose the  topic of your interest: ")
list_of_topic=['Politics', 'Art', 'Science', 'Music', 'Literature','Tourism','Food']
for i in range(len(list_of_topic)):
    print(i+1,". ",list_of_topic[i])

choice=int(input())
choice-=1
list_of_food=["pizza", "hotdogs","sausages","burger","sandwich"]
list_of_tourism=["red fort", "taj mahal","eiffel tower","the leaning tower of pisa"]
list_of_Politics=["narendra modi", "rahul gandhi","sonia gandhi","ramnath kovind"]
list_of_Art=["madhubani painting", "kathak","kathakali","kuchipudi"]
list_of_Science=["mangalyan", "Joint Polar Satellite System","chromosome","mitochondria"]
list_of_Music=["lata mangeshkar", "arijit singh","shakira","sonu nigam","taylor swift","lady gaga"]
list_of_Literature=["william shakespeare", "pablo neruda","william wordsworth","rabindranath tagore"]
chosen=[]
#A/c to their choice, ask either directly make a list of the concerned topic or user can also add in the list
if(choice==0):
    chosen=list_of_Politics
elif(choice==1):
    chosen=list_of_Art
elif(choice==2):
    chosen=list_of_Science
elif(choice==3):
    chosen=list_of_Music
elif(choice==4):
    chosen=list_of_Literature
elif(choice==5):
    chosen=list_of_tourism
elif(choice==6):
    chosen=list_of_food
else:
    print("Invalid Choice")
    
k=len(chosen)
for i in range(k):
    print(i+1, ". ",chosen[i].upper(), " :")
    print(wikipedia.summary(chosen[i], sentences=1))
    print("")

print("Enter the SNO. of the data in which you are most interested :")
SNo=int(input())
SNo=SNo-1
print(wikipedia.summary(chosen[SNo]))