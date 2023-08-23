dictionary = {
    "name" :"전문가용 연필",
     "type": "필기구",
      "ingredient" : ["흑연", "나무", "폴리에틸렌"],
} # 딕셔너리 선언하기

key = input("> 접근하고자하는 키를 입력하세요.") #input 넣어서 키 입력받기

if key in dictionary:
    print(dictionary[key]) # 입력된 키를 출력
else:
    print("존재하지 않는 키입니다. 다시 시도하세요.") # 조건에 부합하지 않을 시 출력할 메시지
