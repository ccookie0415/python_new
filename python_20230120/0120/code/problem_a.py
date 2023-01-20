# -*- coding: utf-8 -*-

import json
from pprint import pprint


def movie_info(movie_dict):
    pass 
    # 여기에 코드를 작성합니다.
    re_dic=dict()
    key=['id','title','poster_path','vote_average','overview','genre_ids']
    for k in key:
        re_dic[k]=movie_dict[k]
    
    return re_dic
    
    
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))