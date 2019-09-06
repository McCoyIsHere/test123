x = 1 and x = 3


def testJackpot(arr):
    ans = False
    first = arr[0]
    count = 0
    for i in range(len(arr)):
        if first == arr[i]:
            count += 1
    if count == len(arr):
        ans = True

    return ans

print(testJackpot(["$", "$$", "$$$", "$$$$"]))
print(testJackpot(["&&", "&", "&&&", "&&&&"]))
print(testJackpot(["&", "&", "$a", "&"]))
print(testJackpot(["@@", "@@", "@@", "@@"]))
print(testJackpot(["Nadeem","Nadeem"])) # ➞ false
