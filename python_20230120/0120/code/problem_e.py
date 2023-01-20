import json


def dec_movies(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    title_list=[]
    for dic in movies:
        a = open(f'data/movies/{dic["id"]}.json', encoding='utf-8')
        b = json.load(a)
        if b['release_date'].split('-')[1]=='12':
            title_list.append(dic['title'])
    return title_list 
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))