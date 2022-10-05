#!/usr/bin/env python
# coding: utf-8

# In[5]:


import psycopg2
import pandas as pd
from sqlalchemy import create_engine


# In[6]:


indata = pd.read_csv("../dataset/kopo_decision_tree_all_new.csv")
indata.shape
indata.columns = indata.columns.str.lower()
indata.columns


# In[7]:


targetDbIp = "192.168.110.111"
targetDbPort = "5432"
targetDbId = "kopo"
targetDbPw = "kopo"
targetDbName = "kopodb"


# In[8]:


targetDbPrefix = "postgresql://"


# In[9]:


targetUrl = "{0}{1}:{2}@{3}:{4}/{5}".format(targetDbPrefix,
                                            targetDbId,
                                            targetDbPw,
                                            targetDbIp,
                                            targetDbPort,
                                            targetDbName)


# In[10]:


tableName = "pgout_kopo_hdk"
pg_kopo_engine = create_engine(targetUrl)


# In[11]:


indata.to_sql(name=tableName,
             con = pg_kopo_engine,
             if_exists="replace", index = False)


# In[12]:


callDB=pd.read_sql(sql = "select * from pgout_kopo_hdk ", con = pg_kopo_engine)
callDB


# In[ ]:





# In[ ]:




