import jieba
import jieba.analyse
import wordcloud
import ast
from imageio import imread
import pandas as pd
from PIL import ImageColor
import numpy as np
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

mask = imread("Omicron.jpg")

stop_words = ['你', '和', '的', '了', '们']

with open('col_may18_2_21.jl', 'r') as file:
    list = ast.literal_eval(f'[{file.read()}]')

materials = ""
# for obj in list[0:53]:
for obj in list:
    obj_cut = jieba.lcut(obj['text'])
    materials += " ".join(obj_cut)

tag = jieba.analyse.extract_tags(sentence=materials,  topK=280, withWeight=True,  allowPOS=(),withFlag=True)
df = pd.DataFrame(data=tag, columns=['','tf-idf'])
print(df)
w = wordcloud.WordCloud( width = 2000, height = 1600,  background_color = "white", colormap='Set1', font_path = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc", stopwords = stop_words, mask = mask   )
# w.generate(materials)
w.fit_words(dict(zip(df[''], df['tf-idf'])))
w.to_file("materials0_30.png")
