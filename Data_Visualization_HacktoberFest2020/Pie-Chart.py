import numpy as np 
import matplotlib.pyplot as plt 
  
  
# Creating dataset 
Events = ['NASA_App_Challange', 'TCS_Challange', 'GoogleDevelopers_Event',  
        'GeeksAthon', 'AlexaEvent', 'HacktoberFest'] 
  
data = [23, 17, 35, 29, 12, 41] 
  
  
# Creating explode data 
explode = (0.1, 0.0, 0.2, 0.3, 0.0, 0.0) 
  
# Creating color parameters 
colors = ( "orange", "cyan", "brown", 
          "grey", "indigo", "beige") 
  
# Wedge properties 
wp = { 'linewidth' : 1, 'edgecolor' : "green" } 
  
# Creating autocpt arguments 
def func(pct, allvalues): 
    absolute = int(pct / 100.*np.sum(allvalues)) 
    return "{:.1f}%\n({:d} g)".format(pct, absolute) 
  
# Creating plot 
fig, ax = plt.subplots(figsize =(10, 7)) 
wedges, texts, autotexts = ax.pie(data,  
                                  autopct = lambda pct: func(pct, data), 
                                  explode = explode,  
                                  labels = Events, 
                                  shadow = True, 
                                  colors = colors, 
                                  startangle = 90, 
                                  wedgeprops = wp, 
                                  textprops = dict(color ="magenta")) 
  
# Adding legend 
ax.legend(wedges, Events, 
          title ="Events", 
          loc ="center left", 
          bbox_to_anchor =(1, 0, 0.5, 1)) 
  
plt.setp(autotexts, size = 8, weight ="bold") 
ax.set_title("Customizing pie chart") 
  
# show plot 
plt.show() 