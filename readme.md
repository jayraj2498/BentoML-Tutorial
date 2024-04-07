### BentoML 

- it is useful to build amzing AI application in such way that you able to deploye it in the production 
- inshort 
    - it is the platform for software engineering to build the Ai prodicts 

- till we made pipeline from training to preiction to dockerise to deployement for proj 
- so all these task you are doing if you are able to do these in just for simple line of code 
- by using "bentoMl" 

###  BentoML 

- we can you use in model_training 
- also we can use it in our app.py production file also 
- it is ML-ops adv methods 
- it is open source liabrary 
- it support multiple liabrary ML , DL and LLM 

#### Bento 

- by using BEnto we can put our application on cloud also 
    - define model 
    - save model 
    - create service 
    - build bento 
    - deploye bento 




#### run the file 

- ## op -->  model is saved  Model(tag="iris_clf:as5dhe7u5gx3mqdu")  
- 

- op -->  model is saved  Model(tag="iris_clf:as5dhe7u5gx3mqdu") 

<!-- ## if train mul time mul time these tag=  will change , so you get mul moddel list 


##  (base) PS E:\New folder> bentoml models list    <-- type that command 
#  Tag                        Module           Size      Creation Time       
#  iris_clf:as5dhe7u5gx3mqdu  bentoml.sklearn  5.98 KiB  2024-04-07 19:43:33
# (base) PS E:\New folder>
## it is storeing models in our local model store  
## if you check c drive -->C:\Users\Jayraj\bentoml\models\iris_clf\as5dhe7u5gx3mqdu you see model stored in it  -->

- Q how we able to read these model 
- crete test.py 

- iris_clf_runner=bentoml.sklearn.get("iris_clf:latest").to_runner()   # <- it is our model we convert it into runner 

- outout is -- > 
- (base) PS E:\New folder> python .\test.py
'Runner.init_local' is for debugging and testing only. Make sure to remove it before deploying to production.
output is --> [2]  


#### next : optimized model infrancing using BentoML 


-  run --> bentoml serve service.py:svc --reload 
- after running these file you will get an api 
- aftre running you will get api 
 2024-04-07T21:03:33+0530 [INFO] [cli] Starting production HTTP BentoServer from "service.py:svc" listening on http://0.0.0.0:3000 (Press CTRL+C to quit)

