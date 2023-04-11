#!/usr/bin/env python
# coding: utf-8

# # Importing Python Libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

import warnings
warnings.filterwarnings('ignore')


# In[2]:


for x in os.listdir():
    print(x)


# In[3]:


# create an empty dictionary to store the DataFrames
dfs = {}

# loop through all files in the directory
for file_name in os.listdir():
    # check if the file is a CSV file
    if file_name.endswith('.csv'):
        # read the CSV file into a DataFrame and store it in the dictionary
        df_name = file_name.replace('.csv', '') # get the DataFrame name from the file name
        dfs[df_name] = pd.read_csv(file_name)

# now you can access the DataFrames using their names as keys in the dictionary
print(dfs['states1'].shape)
print(dfs['states2'].shape)
print(dfs['states3'].shape)
print(dfs['states4'].shape)
print(dfs['states5'].shape)
print(dfs['states6'].shape)
print(dfs['states7'].shape)
print(dfs['states8'].shape)
print(dfs['states9'].shape)


# In[4]:


dfs = []

# loop through all files in the directory
for file_name in os.listdir():
    # check if the file is a CSV file
    if file_name.endswith('.csv'):
        # read the CSV file into a DataFrame and append it to the list
        df = pd.read_csv(file_name)
        dfs.append(df)
        
# concatenate all the DataFrames in the list into one DataFrame
combined_df = pd.concat(dfs)
print(combined_df.shape)

df = pd.DataFrame(combined_df)
df.head(5)


# In[5]:


duplicate_rows = df.duplicated()
print(duplicate_rows.value_counts())


# In[7]:


df.shape


# In[8]:


df.size


# In[9]:


df.describe()


# In[10]:


df.info()


# In[11]:


df.isnull().sum()


# In[12]:


df.drop('Unnamed: 0', axis=1, inplace = True)
print(df.head())


# In[13]:


df[['PropMen','PropWomen']] = df['GenderPop'].str.split('_', expand=True)


# In[14]:


df['PropMen'] = df['PropMen'].str.replace('M', '')
df['PropWomen'] = df['PropWomen'].str.replace('F', '')


# In[15]:


df['PropMen'] = df['PropMen'].replace('', 0)
df['PropMen'] = df['PropMen'].astype(int)


# In[16]:


# replace empty values with 0
df['PropWomen'] = df['PropWomen'].replace('', 0)
df['PropWomen'] = df['PropWomen'].astype(int)


# In[17]:


print(df['PropWomen'].dtype)
print(df['PropMen'].dtype)


# In[18]:


df['Income'] = df['Income'].str.replace('$', '')
df['Income'] = df['Income'].astype(float)


# In[19]:


print(df['Income'].dtype)


# In[20]:


df.info()


# In[21]:


women_per_state = df.groupby('State')['PropWomen'].value_counts()
women_per_state


# In[22]:


df.groupby('State')['Income'].value_counts()


# In[23]:


plt.figure(figsize=(5,3))
# create the scatter plot
plt.scatter(df['PropWomen'], df['Income'], alpha=1)

# add axis labels and a title
plt.xlabel('PropWomen')
plt.ylabel('Average Income')
plt.title('PropWomen Vs Average Income')
plt.grid(False)

# display the plot
plt.show()


# In[24]:


# Create histogram
plt.figure(figsize=(15,3))
ax = sns.barplot(x = df['State'], y = df['PropWomen'], data=df, palette = 'dark')

ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
ax.set_facecolor('white')

plt.xlabel('States')
plt.ylabel('Frequencies')
plt.title('Histogram of Women Per State')
plt.grid(False)

plt.show()


# In[25]:


Pop_by_states = df.groupby("State")[['PropMen','PropWomen']].value_counts()
Pop_by_states


# In[26]:


remaining_pop = df["TotalPop"] - df["PropMen"]
remaining_pop


# In[27]:


df.head()


# In[28]:


#Hispanic Column
df['Hispanic'] = df['Hispanic'].str.replace('%', '')
df['Hispanic'] = df['Hispanic'].astype(float)

#White Column
df['White'] = df['White'].str.replace('%', '')
df['White'] = df['White'].astype(float)

#BlackBlack Column
df['Black'] = df['Black'].str.replace('%', '')
df['Black'] = df['Black'].astype(float)

#Native Column
df['Native'] = df['Native'].str.replace('%', '')
df['Native'] = df['Native'].astype(float)

#Asian Column
df['Asian'] = df['Asian'].str.replace('%', '')
df['Asian'] = df['Asian'].astype(float)

#Pacific Column
df['Pacific'] = df['Pacific'].str.replace('%', '')
df['Pacific'] = df['Pacific'].astype(float)


# In[29]:


df.info()


# In[30]:


df.head()


# In[31]:


df.columns


# In[32]:


# Define the columns to be plotted
cols_to_plot = ['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']

for i in cols_to_plot:
    # Create a histogram for each column
    ax = df[i].hist(alpha=1, grid=False, figsize=(6, 3), color = 'black')
    
    ax.set_facecolor('White')
    plt.grid(False)
    # Add titles and labels
    plt.title('Racist in the Dataset', fontsize=10)
    plt.tight_layout(rect=(0, 0, 1.2, 1.2))
    plt.show()


# In[33]:


sns.set(font_scale=2)
df.hist(grid=False,figsize=(30,30), color='red')

ax = plt.gca()
ax.set_facecolor('White')

plt.show()


# In[34]:


df.info()


# In[35]:


plt.figure(figsize=(5,3))
sns.set(font_scale=1)

sns.heatmap(df.isnull(), cbar=False, cmap='viridis', annot=True)

plt.show()


# In[36]:


updated = df.drop(df[['State','GenderPop']], axis = 1)
print(updated.head())


# In[37]:


mean_pacific = df['Pacific'].mean()
updated['Pacific'] = updated['Pacific'].fillna(mean_pacific)


# In[38]:


plt.figure(figsize=(5,3))
sns.set(font_scale=1)

cmap_list = ['viridis', 'plasma', 'inferno', 'magma', 'cividis', 'coolwarm', 'YlGnBu', 'BuPu', 'PuBuGn', 'PuBu', 'OrRd',
             'YlOrRd', 'RdPu', 'PuRd', 'gist_heat', 'terrain', 'ocean', 'gist_ncar']

for cmap in cmap_list:
    sns.heatmap(updated.isnull(), cbar=False, cmap=cmap)
    plt.title(cmap)
    plt.show()


# In[41]:


updated.head()


# In[42]:


# remove duplicates across all columns
updated = updated.drop_duplicates()

# print the dataframe after removing duplicates
print('Dataframe after removing duplicates:\n', updated)


# In[43]:


duplicates = updated.duplicated()
print(duplicates.value_counts())


# In[44]:


# check if any duplicates exist
if duplicates.any():
    # print the column(s) with duplicate data
    print("Duplicate data in column(s):")
    for col, is_duplicate in zip(df.index, duplicates):
        if is_duplicate:
            print(col)
else:
    print("No duplicate data found.")


# In[45]:


updated.shape


# In[47]:


# create a correlation matrix
corr_matrix = updated.corr()

# create a heatmap of the correlation matrix
sns.heatmap(corr_matrix, cmap='ocean', annot=True)

# display the heatmap
plt.show()


# In[ ]:





# In[ ]:




