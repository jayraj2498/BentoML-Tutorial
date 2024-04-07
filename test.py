import bentoml 

iris_clf_runner=bentoml.sklearn.get("iris_clf:latest").to_runner()   # <- it is our model we convert it into runner 

iris_clf_runner.init_local()  

print(iris_clf_runner.predict.run([[5.9,3.5,5.1,1.8]]))        # now run the file 