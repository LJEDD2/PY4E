def count_word(text,word):
    # text를 txt파일로 저장하기
    filehand = open('m4_2.txt','w')
    filehand.write(text)
    filehand.close()

    text_cnt = text.count(word)
    return text_cnt

a = """ branchorama 나무는 특이한 규칙을 가지고 성장합니다. 
 어린 branchorama 초목은 하나의 잎을 꼭대기에 가진 가는 묘목이며, 그 잎에는 생장점이 있습니다. 
 성장하는 계절 동안 나무의 생장점들은 여러 개의 가지로 나뉘게 되며, 성장이 끝나면 각 가지는 생장점을 가진 하나의 잎을 꼭대기에 매달게 됩니다. 
 놀랍게도 같은 나무의 모든 생장점들은 같은 숫자(splitting factor)의 가지로 나뉘며, 그 숫자는 해가 지남에 따라 변합니다."""

word = input("찾고싶은 단어를 입력하세요 : ")
print(count_word(a, word))