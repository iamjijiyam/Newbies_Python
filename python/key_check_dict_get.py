dictionary = {
    "name" :"전문가용 연필",
     "type": "필기구",
      "ingredient" : ["흑연", "나무", "폴리에틸렌"],
} # 딕셔너리 선언하기

value = dictionary.get("존재하지 않는 키") #존재하지 않는 키에 접근
print("값:",value)

if value == None: #None확인 시 결과 값이 None과 같은 지 확인만 해주면 돼요!
    print("존재하지 않는 키에 접근했습니다. 데이터에선 None으로 표시됩니다.")