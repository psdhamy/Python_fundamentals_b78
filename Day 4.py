#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Introduction to list datatype


# In[ ]:


list is a collection of items declared ina particular order
classification : it is classified as an mutable datatype


# In[ ]:


how to define /declare the list  []


# In[1]:


students= ['shruthi','siva','kumar','nivedhitha','vasanth','john','paul']


# In[2]:


print(students)


# In[3]:


type(students)


# In[ ]:


Intoduction to inexing
#req i want to get the name of nivedhitha on tne output


# In[4]:


print(students[3])


# In[5]:


print(students[3].title())


# In[ ]:


how to add a new elements to the list


# In[ ]:


how to modify a new elements to the list
how to delete a new elements to the list


# In[ ]:


# req i want to add pranay to the list


# In[6]:


students.append('pranay')
print(students)


# In[7]:


students.append('manoj')
print(students)


# In[ ]:


#req i want to add bala to the 2nd index position


# In[9]:


students.insert(2,'bala')
print(students)


# In[ ]:


#req i want to modify siva to vishal


# In[11]:


students[1]='vishal'
print(students)


# In[ ]:


Temporary deleting -- pop
by default pop will be deleting the item from the last. if needed we can specify the index as well. pop will be storing the 
deleted item in the variables that has been assigned to it.


# In[12]:


x=students.pop()
print(students)


# In[13]:


print(x)


# In[ ]:


#req delete john


# In[14]:


y=students.pop(6)
print(students)
print(y)


# In[ ]:


# req i want to delete vishal


# In[16]:


del students[1]
print(students)


# In[ ]:





# In[ ]:





# In[ ]:




