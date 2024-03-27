clusters = ["music", "politics", "science", "art", "sport", "funny", "games"]
nums = 0
for i in clusters:
    f = open(f"data/comments_{i}.txt", encoding="utf8")
    list_com = f.readlines()
    f.close()
    nums += len(list_com)
    print(i, len(list_com))
print("all", nums)
