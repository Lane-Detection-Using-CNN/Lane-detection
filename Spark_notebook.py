#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Read image data to dataframes 
df = spark.read.format("image").load("/FileStore/tables/*.jpg")


# In[2]:


size = df.select("image.height", "image.width",).first()
size


# In[3]:


#Extract attributes
df_pd = df.select("image.width", "image.height", "image.data", "image.nChannels").toPandas()


# In[4]:


#Create list of numpy arrays having attributes of each image
import numpy as np
img_arr = []
for index, row in df_pd.iterrows():
    height = row['height']
    width = row['width']
    nChannels = row['nChannels']
    data = row['data']
    
    img_arr.append(np.ndarray(shape=(height, width, nChannels),
            dtype=np.uint8,
            buffer=data,
            strides=(width * nChannels, nChannels, 1)))


# In[5]:


#Display img_arr
img_arr


# In[6]:


#Store img_arr in a txt file in Databricks storage system
dbutils.fs.put("/FileStore/tables/image_arrays.txt", str(img_arr))


# In[7]:


df_pd.head()


# In[8]:


#Extract attributes to be inserted in Hive Table
df_text = df.select("image.width", "image.height", "image.nChannels")


# In[9]:


#Create a csv file to store these attributes:
df_text.coalesce(1).write.format("csv").option("header", "true").mode("append").save("/FileStore/tables/attributes.csv")

