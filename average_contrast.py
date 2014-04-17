
import os
import sys
from math import sqrt
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt

image_index = ["/nfs/t2/fmricenter/volume/S0001/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0004/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0005/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0006/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0007/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0009/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0010/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0012/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0014/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0016/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0020/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0025/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0027/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0034/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0035/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0036/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0037/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0038/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0040/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0041/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0051/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0053/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0057/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0059/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0068/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0069/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0070/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0074/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0076/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0077/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0081/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0085/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0087/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0091/obj.gfeat/cope1.feat/stats/tstat1.nii.gz",\
             "/nfs/t2/fmricenter/volume/S0092/obj.gfeat/cope1.feat/stats/tstat1.nii.gz"]

seeds=[(25,41,25),(25,36,29),(26,31,29),(23,38,23),(66,38,29),(25,39,24),(25,38,25),\
       (25,41,26),(24,35,22),(22,35,24),(27,29,28),(68,36,24),(27,30,26),(23,37,24),\
       (26,38,25),(24,38,27),(22,31,26),(23,34,26),(24,37,24),(24,37,25),(22,38,27),\
       (23,40,27),(25,40,24),(24,38,24),(21,38,24),(24,29,28),(26,40,26),(24,39,26),\
       (23,38,26),(21,40,22),(23,38,26),(23,39,23),(25,35,25),(23,38,30),(65,38,24)]

output=['S0001(25,41,25)','S0004(25,36,29)','S0005(26,31,29)','S0006(23,38,23)','S0007(66,38,29)',\
        'S0009(25,39,24)','S0010(25,38,25)','S0012(25,41,26)','S0014(24,35,22)','S0016(22,35,24)',\
        'S0020(27,29,28)','S0025(68,36,24)','S0027(27,30,26)','S0034(23,37,24)','S0035(26,38,25)',\
        'S0036(24,38,27)','S0037(22,31,26)','S0038(23,34,26)','S0040(24,37,24)','S0041(24,37,25)',\
        'S0051(22,38,27)','S0053(25,36,29)','S0057(25,40,24)','S0059(24,38,24)','S0068(21,38,24)',\
        'S0069(24,29,28)','S0070(26,40,26)','S0074(24,39,26)','S0076(23,38,26)','S0077(21,40,22)',\
        'S0081(23,38,26)','S0085(23,39,23)','S0087(25,35,25)','S0091(23,38,30)','S0092(65,38,24)']

number=[116,64,21,13,166,239,172,48,148,783,54,27,94,917,138,135,25,187,\
        127,113,280,38,129,245,68,122,19,102,84,96,340,543,55,231,62]

def region_growing(image,coordinate,out_put,Num):
    """
    Give a coordinate ,return a region.
    """
    x,y,z = coordinate
    image_shape = image.shape
    inside = (x>=0)and(x<image_shape[0])and(y>=0)and\
             (y<image_shape[1])and(z>=0)and(z<image_shape[2])
    if inside!=True:
        print "The coordinate is out of the image range."
        return False

    filename = out_put
    contents = []

    tmp_image = np.zeros_like(image)
    inner_image = np.zeros_like(image)
    inner_list = []
    contrast = []
    
    region_size = 1
    origin_t = image[x,y,z]
    inner_list = inner_list + [origin_t]

    neighbor_free = 10000
    neighbor_pos = -1
    neighbor_list = np.zeros((neighbor_free,4))

    offsets = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],\
           [0,0,-1],[0,0,1],[1,1,0],[1,1,1],\
           [1,1,-1],[0,1,1],[-1,1,1],[1,0,1],\
           [1,-1,1],[-1,-1,0],[-1,-1,-1],[-1,-1,1],\
           [0,-1,-1],[1,-1,-1],[-1,0,-1],[-1,1,-1],\
           [0,1,-1],[0,-1,1],[1,0,-1],[1,-1,0],\
           [-1,0,1],[-1,1,0]]


    while region_size <= Num:
        for i in range(26):
            xn = x + offsets[i][0]
            yn = y + offsets[i][1]
            zn = z + offsets[i][2]

            inside = (xn>=0)and(xn<image_shape[0])and(yn>=0)and(yn<image_shape[1]) \
                     and(zn>=0)and(zn<image_shape[2])  
            
            if inside and tmp_image[xn,yn,zn]==0:
                neighbor_pos = neighbor_pos+1
                neighbor_list[neighbor_pos] = [xn,yn,zn,image[xn,yn,zn]]   
                tmp_image[xn,yn,zn] = 1

        out_boundary = neighbor_list[np.nonzero(neighbor_list[:,3]),3]
        contrast = contrast + [np.mean(np.array(inner_list)) - np.mean(out_boundary)]


        entry = '%.6f' % (np.mean(np.array(inner_list)) - np.mean(out_boundary))
        contents.append(entry)
        fobj = open(filename,'w')
        fobj.writelines(['%s%s' % (eachline, os.linesep) for eachline in contents])


        tmp_image[x,y,z] = 2
        inner_image[x,y,z] = image[x,y,z]        
        region_size += 1

        if (neighbor_pos+100 > neighbor_free):   
            neighbor_free +=10000                
            new_list = np.zeros((10000,4)) 
            neighbor_list = np.vstack((neighbor_list,new_list)) 
            #if the longth of neighbor_list is not enough,add another 10000       
            
        distance = np.abs(neighbor_list[:neighbor_pos+1,3] - np.tile(origin_t,neighbor_pos+1))        
        index = distance.argmin()            
        inner_list = inner_list + [image[x,y,z]]
       
        neighbor_list[index] = neighbor_list[neighbor_pos]
        neighbor_pos -= 1
   
    return inner_image,region_size-1,contrast


for i in range(9,10):
    t_img=nib.load(image_index[i])
    t_data=t_img.get_data() 
    region,num,contrast = region_growing(t_data,seeds[i],output[i],number[i])
    t_img._data = region
    y1 = contrast
    nib.save(t_img,output[i]+".nii.gz")
    print num

    x1 = range(1,num+1)
    plt.plot(x1,y1,label='average contrast')

    plt.show()

