# Databricks notebook source
# DBTITLE 1,Maximum number of teams that can be formed with given persons
def canFormTeams(n,m):
  #taking two person from n and one person form m
  if (n >=1 and m >=2):
    return True
  #taking one person from n and two person form m
  if (n>=2 and m >=1):
    return True
  #cannot form a teams
  return False

def maxTeams(n,m):
  count = 0
  
  while (canFormTeams(n,m)):
    if n > m:
      n -= 2
      m -= 1
    else:
      n -= 1
      m -= 2
    
    count+=1
    
  return count  
      

# COMMAND ----------

maxTeams(4,5)

# COMMAND ----------


