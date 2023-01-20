import json


def max_revenue(movies):
    max_dict=movies[0]
    max_value=0
    for dic in movies:
        a = open(f'data/movies/{dic["id"]}.json', encoding='utf-8')
        b = json.load(a)
        if b['revenue'] > max_value:
            max_dict=dic
            max_value=b['revenue']
    return max_dict['title']
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))