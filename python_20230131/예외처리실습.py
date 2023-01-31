try:
    num = input('100으로 나눌 값을 입력하시오 :')
    print(100/int(num))
    
except ValueError:
    print('숫자를 넣어주세요.')
    
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
    
except:
    print('에러는 모르지만 에러가 발생하였습니다.')
