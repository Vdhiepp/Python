#Cho ds=[1,2,3,4,5,6]. Lọc ra các pt chẵn

ds = [1,2,3,4,5,6]
ds_chan = list(filter(lambda x : x%2 == 0 ,ds))
print(ds_chan)