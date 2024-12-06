import numpy as np
import pandas as pd
# arr=[[2,3],[1,2]]
# print(np.array(arr))

# print(np.arange(2,15,2))

# eye ex np.eye(3,5 creates identity matrix )
#if diagonal matrix np.diag([1,4],[2,3]) prints 1 3 element
#for zero matrix np.zeros((2,3,4))

# indexing and slicing 
# data=np.array([11,22,33,44,55])
# print(data[0])

# negative indices count from backwards
# print(data[-1])

# slicing
# print(data[-1:-3])
# print(data[:3])


# 2d array
# twoD=np.array([[1,2],[3,4],[5,6]])
# print(twoD)
# print(twoD[0,0])
# print(twoD[1:-1,0:1])


# dot product
# Define two vectors
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# Dot product
# dot_product = np.dot(a, b)
# print(dot_product)

# cross_product = np.cross(a, b)
# print(cross_product)

# magnitude_a = np.linalg.norm(a)
# magnitude_b = np.linalg.norm(b)
# print(magnitude_a)
# print(magnitude_b)


# print((np.random.rand(2,2)*10).astype(int))

# np.random.seed(101)  # Set seed for reproducibility
# df = pd.DataFrame(np.random.rand(2, 2), index=['a', 'b'], columns=['e', 'f'])
# print(df)
# print(df.loc[['a']]) #chahine row 
# print(df.iloc[1:2]) #print by index

# print(df[df['e'] > 0.5]) #with condition

# print(df.iloc[:,1]) # select from where to where in index

#select colum and rows as such


#dictionary
# data={
#     'company':['apple','google','facebook'],
#     'person':['subesh','saroj','sangam'],
#     'salary':[1000,2000,3000]
# }
# df=pd.DataFrame(data)
# # print(df)

# sal=df.groupby('company')['salary'].mean() #can be sum() count()
# print(sal)




#np.nan creates a null value i.e. NaN
# d={'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
# df=pd.DataFrame(d)
# print(df)

#dropping row with NaN
# print(df.dropna()) #it just gives the row having data

# print(df.dropna(axis=1)) #it drops the col
# print(df.dropna(thresh=2))

#filling with something
# print(df.fillna(value='1')) # fill with 1 


#filling with mean value in nan value 
# print(df['B'].fillna(value=df['B'].mean())) #fills mean in col A, B, C as want
# print(df)

#read csv file
# readCSV=pd.read_csv('F:\PYthon\Lab\subesh\data.csv')
# print(readCSV)