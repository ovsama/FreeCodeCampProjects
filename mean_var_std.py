# This Python program aims at building a simple Mean-Variance-Standard Deviation Calculator for a  3 x 3 matrix.

def  calculate(list):
 
   if len(list) < 9:
       print("ValueError : List must contain nine numbers.")

   else:
       
      import numpy as np
  
      mtrx = np.array([list[0:3], list[3:6], list[6:9]])
      
      mt = mtrx.mean()
      m1 = mtrx[:,0].mean()
      m2 = mtrx[:,1].mean()
      m3 = mtrx[:,2].mean()
      m4 = mtrx[0,:].mean()
      m5 = mtrx[1,:].mean()
      m6 = mtrx[2,:].mean()


      vt = mtrx.var()
      v1 = mtrx[:,0].var()
      v2 = mtrx[:,1].var()
      v3 = mtrx[:,2].var()
      v4 = mtrx[0,:].var()
      v5 = mtrx[1,:].var()
      v6 = mtrx[2,:].var()


      st = mtrx.std()
      s1 = mtrx[:,0].std()
      s2 = mtrx[:,1].std()
      s3 = mtrx[:,2].std()
      s4 = mtrx[0,:].std()
      s5 = mtrx[1,:].std()
      s6 = mtrx[2,:].std()

      maxt = mtrx.max()
      max1 = mtrx[:,0].max()
      max2 = mtrx[:,1].max()
      max3 = mtrx[:,2].max()
      max4 = mtrx[0,:].max()
      max5 = mtrx[1,:].max()
      max6 = mtrx[2,:].max()

      mint = mtrx.min()
      min1 = mtrx[:,0].min()
      min2 = mtrx[:,1].min()
      min3 = mtrx[:,2].min()
      min4 = mtrx[0,:].min()
      min5 = mtrx[1,:].min()
      min6 = mtrx[2,:].min()


      sumt = mtrx.sum()
      sum1 = mtrx[:,0].sum()
      sum2 = mtrx[:,1].sum()
      sum3 = mtrx[:,2].sum()
      sum4 = mtrx[0,:].sum()
      sum5 = mtrx[1,:].sum()
      sum6 = mtrx[2,:].sum()


      dic = {'mean': [[m1, m2, m3], [m4, m5, m6], mt],'variance': [[v1, v2, v3], [v4, v5, v6], vt],'standard deviation': [[s1, s2, s3], [s4, s5, s6], st],'max':[[max1, max2, max3], [max4, max5, max6], maxt],'min': [[min1, min2, min3], [min4, min5, min6], mint],'sum': [[sum1, sum2, sum3], [sum4, sum5, sum6], sumt]} 
               
      print(dic)









