import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr

df = pd.read_excel("Website Performance Analysis dataset.xlsx" , sheet_name = "data-export")
print(df.columns)
print(df.head)

df.columns = ['Channel Group',
       'DateHour', 'Users', 'Sessions', 'Engaged sessions',
       'Avg Engagement Time', 'Engaged sessions per user',
       'Events per session', 'Engagement rate', 'Event count']
print(df['Events per session'].max())
df["Hour"] = df["DateHour"].astype(str).str[-2:].astype(int)

numeric_df = df.select_dtypes(include=[float, int])




# (1) line plot --- Sessions by Hour

plt.figure(figsize = (8,10))
hours = df.groupby('Hour')['Engaged sessions'].mean()
sns.lineplot(x=hours.index,y=hours.values,color = "darkblue",marker="s",linewidth=4)
plt.title("Average Engaged sessions by Hour")
plt.xlabel("Hours")
plt.ylabel("Average Engaged sessions")
plt.xticks(range(0, 24))
plt.savefig("Sessions by Hour.png")
plt.show()



# (2) pie chart --- top 10 Events per session and top 10 Event count

y = df["Events per session"].head(10)
y1 = df["Event count"].head(10)
color = ["lightgreen","g","pink","r","b","Teal" , "plum" , "skyblue","violet" , "orange"]
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.pie(y1,labels = y , autopct = "%1.2f%%" , colors = color)
plt.savefig("Top 10 Event Count Distribution.png")
plt.show()






# (3)bar plot  ----  the average number of Users per Channel


avg_users = df.groupby('Channel Group')['Users'].mean().sort_values(ascending = False)
colors = sns.color_palette("colorblind", 10)
plt.figure(figsize = (8,10))
plt.bar(avg_users.index, avg_users.values,color = colors)
plt.xlabel("Channel" , fontsize = 100)
plt.ylabel("average number of Users")
plt.title("average number of Users per Channel")
plt.xticks(rotation=45)
plt.savefig("average number of Users per Channel.png")
plt.show()




# (4) Scatterplot ---- Users vs Events per session

plt.figure(figsize=(8, 6))
sns.scatterplot(data = df , x = "Users", y = "Events per session" , color = 'red')
plt.title("Users vs Events per session")
plt.xlabel("Users")
plt.ylabel("Events per session")
plt.tight_layout()
plt.savefig("Users vs Events per session.png")
plt.show()




# (5) Heatmap --- Correlation Heatmap of Website Performance Data

correlation = numeric_df.corr()
plt.figure(figsize = (10,6))
sns.heatmap(correlation , annot = True ,fmt = '.2f' , cmap ="Reds",linewidth = 0.5 )
plt.title("Correlation Heatmap of Website Performance Data")
plt.savefig("heatmap.png")
plt.show()





# (6)Histogram ----Average  Event count per session

plt.figure(figsize=(10,12))
sns.histplot(data=df , x = "Event count",color = "teal",bins=30,kde=True)
plt.title("Average  Event count per session")
plt.xlabel("Events count per session")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("Average Events count per session.png")
plt.show()




# (7) Box Plot ----- Event count per Channel

plt.figure(figsize = (10,12))
sns.boxplot(x = "Channel Group" , y = "Event count" ,data = df , color = "blue")
plt.title("Average Event count per Channel")
plt.xlabel("Channel Group")
plt.ylabel("Avg Event count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Event count per Channel")
plt.show()




# (8) ViolinPlot --- Engagement rate across Channel Groups

plt.figure(figsize=(10,8))
sns.violinplot(x="Channel Group" ,y="Engagement rate" ,hue="Channel Group", data=df,
               palette="pastel")
plt.title("Engagement rate across Channel Groups across Channel Groups")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Engaged Sessions per User.png")
plt.show()





