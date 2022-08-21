s = ["김갑,3242524215",
     "이을,3242524223",
     "박병,2242554131",
     "최정,4245242315",
     "정무,3242524315"]

# 정답지
a = [3, 2, 4, 2, 5, 2, 4, 3, 1, 2]


def grader(s, a):
    arr = []
    for i in s:
        q, w = i.split(',')
        cnt = 0
        for i in range(len(w)):
            if a[i] == int(w[i]):
                cnt += 1
        arr.append([cnt, q])
    arr.sort(reverse=True)
    return arr


arr = grader(s, a)
idx = 1
for i in arr:
    print(f"학생 : {i[1]}, 점수 : {i[0] * 10}, {idx}등")
    idx += 1