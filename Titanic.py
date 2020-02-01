#!/usr/bin/env python
# coding: utf-8

# ## Importing the library  for Titanic data analysis

# In[102]:


# import matplotlib.pyplot as plt
# %matplotlib inline
# x=[5,7,8,9,10]
# y=[5,7,8,9,10]
# plt.plot(x,y)
# plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# get_ipython().run_line_magic('matplotlib', 'inline')

import seaborn as sns

titanic_data=pd.read_csv('/home/hindu/Desktop/python/ml learn/titanic1.csv')
print(titanic_data.shape)


# # information of data

# In[103]:


print(titanic_data.info())


# In[104]:


print(titanic_data.head())


# # checking the Null Values

# In[105]:


print(titanic_data.isnull())


# In[106]:


print(titanic_data.isnull().sum())


# ### Plotting the heatmap for checking NaN values

# In[107]:


sns.heatmap(titanic_data.isnull(),yticklabels=False,cmap='viridis')
plt.show()

# # Analyzing the data

# In[108]:


sns.countplot('Survived',data=titanic_data)
plt.show()

# ## checking sex wise survival

# In[109]:


sns.countplot('Survived',hue='Sex',data = titanic_data)
plt.show()

# ## checking the class of survived passanger

# In[110]:


sns.countplot(x='Survived', hue='Pclass',data=titanic_data)
plt.show()

# ## Graph of age distribution

# In[111]:


titanic_data['Age'].plot.hist()
plt.show()

# ## Plotiing siblings and Spouse

# In[112]:


sns.countplot(x='Siblings/Spouses Aboard' , data=titanic_data)
plt.show()

# ## plotting number of Parents/Children Aboard

# In[113]:


sns.countplot(x='Parents/Children Aboard',data=titanic_data)
plt.show()

# ## Analysing the age of passanger class

# In[114]:


sns.boxplot(x='Pclass',y='Age',data=titanic_data)
plt.show()

# ##   Getting dummy value for Sex to feed in model

# In[115]:


sex=pd.get_dummies(titanic_data['Sex'],drop_first=True)
print(sex.head())


# ## Getting dummy value for Passanger class to feed the model

# In[116]:


Pcl=pd.get_dummies(titanic_data['Pclass'],drop_first=True)
print(Pcl.head())


# ## add the sex and pcl to titanic_data

# In[117]:


titanic_data=pd.concat([titanic_data,sex,Pcl],axis=1)
print(titanic_data.head())


# ## droping un-necessary column

# In[118]:


titanic_data.drop(['Pclass','Sex','Name'],axis=1,inplace=True)


# In[119]:


print(titanic_data.head())


# ## Train and test data split

# In[121]:





# In[120]:


X=titanic_data.drop('Survived',axis=1)
y=titanic_data['Survived']
print(X.head())


# In[122]:
print(y.head())

from sklearn.model_selection import train_test_split


# ## Data split into 70% and 30% ratio

# In[165]:


X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=40)


# ## importing the Logistic regression model from sklearn

# In[166]:


from sklearn.linear_model import LogisticRegression


# ## making the instance of Logistic Regression model

# In[167]:


logistic=LogisticRegression()


# ## Fitting the data into Model

# In[168]:


logistic.fit(X_train,y_train)


# ## Predicting from the tested model

# In[169]:


predictions=logistic.predict(X_test)


# In[170]:


print(predictions)


# ## verifying the results

# In[171]:


from sklearn.metrics import classification_report


# In[172]:


print(classification_report(y_test,predictions))


# ## checking confusion metrix

# In[173]:


from sklearn.metrics import confusion_matrix


# In[174]:


print(confusion_matrix(y_test,predictions))


# ## checking the accuracy of model

# In[175]:


from sklearn.metrics import accuracy_score


# In[176]:


print("Accuracy of model : ",accuracy_score(y_test,predictions)*100,"%")


# In[ ]:




