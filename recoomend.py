import uvicorn
from fastapi import FastAPI
from datainp import  USER
from datainp import  PRODUCT
from content import *
import numpy as np
import pickle
import pandas as pd
app=FastAPI()

@app.get('/')
def index():
    return {'message':'hellosd'}

@app.post('/predict')
def predict_output(data:USER):
    print("yeloo")
    pickle_in = open("res", "rb")
    content_recommender = pickle.load(pickle_in)
    recommendation=content_recommender.get_recommendations(data.user_id)
    return {"recommendation":recommendation}





@app.post('/postdetail')
def post_data(data:PRODUCT):
    dat = [
        ['game', 'gta', 'user1', 'item1'],
        ['game', 'gta', 'user1', 'item2'],
        ['game', 'gta', 'user2', 'item3'],
        ['game', 'cod', 'user3', 'item4'],
        ['game', 'cod', 'user3', 'item5'],
        ['fashion', 'zara', 'user4', 'item6'],
        ['fashion', 'zara', 'user4', 'item7'],
        ['fashion', 'hm', 'user5', 'item8'],
        ['fashion', 'hm', 'user5', 'item9'],
        ['electronics', 'sony', 'user6', 'item10'],
        ['electronics', 'sony', 'user6', 'item11'],
        ['electronics', 'samsung', 'user7', 'item12'],
        ['electronics', 'samsung', 'user7', 'item13'],
        ['electronics', 'lg', 'user8', 'item14'],
        ['electronics', 'lg', 'user8', 'item15'],
        ['books', 'penguin', 'user9', 'item16'],
        ['books', 'penguin', 'user9', 'item17'],
        ['books', 'randomhouse', 'user10', 'item18'],
        ['books', 'randomhouse', 'user10', 'item19']
    ]
    df=pd.DataFrame(dat,columns=['sub_cat','brand','user_id','item_id'])
    pickle_in=open("res","rb")
    ContentBasedRecommender=pickle.load(pickle_in)
    content_recommender=ContentBasedRecommender(df)
    with open("res",'wb') as pickle_out:
        pickle.dump(content_recommender,pickle_out)

    return {"dataframe":df}













if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)





