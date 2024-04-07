import bentoml 
from sklearn import svm 
from sklearn import datasets  

import pandas as pd 

iris = datasets.load_iris()

x , y =iris.data  , iris.target  
# print(x,y) 

# print(len(x))

clf=svm.SVC(gamma='scale')

clf.fit(x,y)  



# save model to bentoml local model store 
save_model=bentoml.sklearn.save_model("iris_clf" , clf)  # we save our model in partucalr file 

print(f" model is saved {save_model}")   


## op -->  model is saved  Model(tag="iris_clf:as5dhe7u5gx3mqdu") 

## if train mul time mul time these tag=  will change , so you get mul moddel list 


##  (base) PS E:\New folder> bentoml models list    <-- type that command 
#  Tag                        Module           Size      Creation Time       
#  iris_clf:as5dhe7u5gx3mqdu  bentoml.sklearn  5.98 KiB  2024-04-07 19:43:33
# (base) PS E:\New folder>
## it is storeing models in our local model store  
## if you check c drive -->C:\Users\Jayraj\bentoml\models\iris_clf\as5dhe7u5gx3mqdu you see model stored in it 

- test.py 
