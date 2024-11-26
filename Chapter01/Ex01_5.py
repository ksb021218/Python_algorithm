# 기존의 가격 정보 딕셔너리
price = {
    "콩나물해장국": 4500,
    "갈비탕": 9000,
    "돈가스": 8000
}

# 새로운 메뉴 "팟타이"를 7000원에 추가
price["팟타이"] = 7000

# 모든 메뉴와 가격을 출력
for menu, cost in price.items():
    print(f"{menu}: {cost}원")
