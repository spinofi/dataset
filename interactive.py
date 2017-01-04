# -*- encoding: utf-8 -*-
from sklearn.externals import joblib
from util import encode, decode
from model import Model

dicts = joblib.load("dicts.pkl")

model = Model(input_length=60,output_length=8,w_dim=100,e_dim=80,p_dim=20,enc_dim=100,dec_dim=100,w_size=200000,e_size=752,p_size=62)
model.load("model.ckpt")

while True:
    print "入力："
    sentence = raw_input()
    W = encode(sentence,dicts["word2id"])
    E,P = model.sample(W)
    decode(W,E,P,dicts["id2word"],dicts["id2emoji"])
    
