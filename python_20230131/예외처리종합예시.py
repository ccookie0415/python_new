# 파일 읽기
try :
    f = open('noofile.txt')
except FileNotFoundError:
    print('해당 파일이 없습니다.')
    
else:
    print('파일을 읽기 시작합니다.')
    print(f.read())
    print('파일을 모두 읽었습니다.')
    f.close()
    
finally:
    print('파일 읽기를 종료합니다')