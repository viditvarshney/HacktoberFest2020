import numpy as np 
import matplotlib.pyplot as plt 


# creating the dataset 
Programming_Languages = {'C':60, 'C++':65, 'Java':70, 
		'Python':95} 
Comparison = list(Programming_Languages.keys()) 
Percentage_Out_OF_100 = list(Programming_Languages.values()) 

fig = plt.figure(figsize = (10, 5)) 

# creating the bar plot 
plt.bar(Comparison, Percentage_Out_OF_100, color ='Blue', 
		width = 0.4) 

plt.xlabel("Programming Languages") 
plt.ylabel("Comparison According to Current Scenario") 
plt.title("Technologies Comparison") 
plt.show() 
