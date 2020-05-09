import os
import matplotlib.pyplot as plt
import pandas as pd

crops_data = pd.read_csv("CropsDataFile.csv")
state = crops_data["State_Name"].values.tolist()
district = crops_data["District_Name"].values.tolist()
crop_year = crops_data["Crop_Year"].values.tolist()
season = crops_data["Season"].values.tolist()
crop = crops_data["Crop"].values.tolist()
area = crops_data["Area"].values.tolist()
production = crops_data["Production"].values.tolist()
os.chdir("C:\\Users\\saran\\New folder")

# It stores all data on your folder in C drive
A = open("Year Wise Data.txt",'w')
B = open("Crop wise Data.txt",'w')

print("pree 1 for yearwise crop data\npress 2 for the graphs\npress 3 to get cropwise data\npress 4 for exit")
while(1):
    c = int(input("type your choice "))
    if(c==1):
        n=int(input("type the desired year : "))
        print("data of your desired crop is stored in new folder")
        for i in range(0,len(crop_year)):
            if(crop_year[i]==n):
            
                A.write("\n State:"+str(state[i])+ "\n District:"+ str(district[i])+"\n Season:" +str(season[i])+"\n Crop:"+str(crop[i])+"\n Area :"+str(area[i])+ "\n Production : "+str(production[i])+"\n")
                
    elif(c==2):
        C=str(input("type the desired crop name : "))
        Year=[]
        Production=[]
        for i in range(0,len(crop_year)):
            if(crop[i]==C):
                Year.append(crop_year[i])
                Production.append(production[i])
        plt.bar(Year,Production) 
        plt.xlabel("Year") 
        plt.ylabel("Production") 
        plt.title(f"Year vs Crop Productivity graph of {C}",color = "red" )
        plt.show()     
    elif(c==3):
        D=str(input("type the crop name : "))
        for i in range(len(crop_year)):
            if(crop[i]==D):
                B.write("\n State:"+str(state[i])+ "\n District:"+ str(district[i]) + " \n Crop Year: " +str(crop_year[i])+"\n Season:" +str(season[i])+"\n Area :"+str(area[i])+ "\n Production : "+str(production[i])+"\n")
        print("data of your desired crop is stored in new folder") 
    else:
        break            
     