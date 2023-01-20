import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    re_dic=dict()
    key=['id','title','poster_path','vote_average','overview','genre_ids']
    for k in key:
        if k == 'genre_ids':
            names=[]
            for dic in genres:
                if dic['id'] in movie[k]:
                    names.append(dic['name'])
            re_dic['gener_names']=names
        else:
            re_dic[k]=movie[k]
    
    
    return re_dic
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
