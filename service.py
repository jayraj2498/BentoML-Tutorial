## these is most imp file 
## it is resposible to create your entire api by using bentoml 

import numpy as np 
import bentoml 
from bentoml.io import NumpyNdarray 


iris_clf_runner = bentoml.sklearn.get("iris_clf:latest").to_runner()     # <-- our model 

svc = bentoml.Service("iris_classifier", runners=[iris_clf_runner]) # we crate service with nmae , and our model is runners 

@svc.api(input=NumpyNdarray(), output=NumpyNdarray())        # like thes we can create no of api  # our ip , op is ndarry 
def classify(input_series: np.ndarray) -> np.ndarray:
    result = iris_clf_runner.predict.run(input_series)        # here our para is np.array
    return result                                                 # model wrt ip  







# run --> bentoml serve service.py:svc --reload 
# after running these file you will get an api 
## aftre running you will get api 
## 2024-04-07T21:03:33+0530 [INFO] [cli] Starting production HTTP BentoServer from "service.py:svc" listening on http://0.0.0.0:3000 (Press CTRL+C to quit)

## next step
## we have to package it all to send to deployemnent section 
## we package it by using bentofile.yaml to deployemet you can dockerise it 