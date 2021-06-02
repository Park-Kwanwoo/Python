def coffee(quantity, price):
    change = price - (quantity * 100)
    if change >= 0:
        prn(quantity, change)
    else:
        prn()


def prn(quantity=0, change=0):
    if quantity == 0 & change == 0:
        print('금액이 부족합니다')
    else:
        print('주문하신 커피 {}잔 나왔습니다. 거스름돈은 {}입니다'.format(quantity, change))

def start():
    q = int(input('주문하실 커피의 갯수를 입력하세요 : '))
    p = int(input('금액을 투입해주세요 : '))
    coffee(q, p)

if __name__=='__main__':
    start()