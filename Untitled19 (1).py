#!/usr/bin/env python
# coding: utf-8

# In[2]:


ASSIGNMENT 3      


# In[ ]:


#PROBLEM 1


# In[ ]:


#In a cricket tournament , based on the the outcomes of particular match a team gets following points:
#  * wins gets 3 points
#  * draws gets 1 point
#  *looses gets 0 point
# Team Aravali plays 8 matches in the tournament.It wins 4matches , looses 3 matches and draws 1 . What is th total point gained by team Arawali


# In[2]:



game_win=float(input("Enter win game:"))
game_draws=float(input('Enter draw game:'))
game_loses=float(input("Enter loose game:"))
Aravali_points = ((game_win*3) +(game_draws*1)+(game_loses*0))


# In[4]:


print(Aravali_points)


# In[ ]:


#Problem 2


# In[ ]:


#A bag contains 45 apples , 65 Oranges and 30 bananas.Find the percentage of each type of food items in the bag.


# In[6]:


n1=float(input("Enter the no of apples"))
Apple_percent=n1/140*100
print(Apple_percent)
n2=float(input("Enter the no of oranges"))
Orange_percent=n2/140*100
print(Orange_percent)
n3=float(input("Enter the no of Bananas"))
Banana_percent=n3/140*100
print(Banana_percent)


# In[ ]:


# Problem 3


# In[ ]:


#You are given a sentence which reads"Wikipedia is a free online encyclopedia, createdand edited by volunteers around the world and hosted by the wikimediaFoundation."


# In[9]:


Sentence = "Wikipedia is a free online encyclopedia, createdand edited by volunteers around the world and hosted by the wikimedia Foundation."
print ("The Sentence is : " + Sentence)
res = Sentence.count(" ")+1
print("The number of words in sentence are: "  +str(res))


# In[ ]:




