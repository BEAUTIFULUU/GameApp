result = (x * x for x in range(3))
for x in result:
    print(x)

t = [1, 2, 4, 6]

print(iter(t))

st = 1


def is_palindrome(word):
    if word == word[::-1]:
        return True

    else:
        return False


word_to_check = "kajak"
result = is_palindrome(word_to_check)

print(result)

s = "kurwa"

print(s[::-1])

d = {"gowno": 1, "dupa": 2}
new_data = {"kot": 3, "pies": 4}

d.update(new_data)

print(d)

ls = [1, 2, 3]

additional_l = ()

ls.extend(additional_l)

print(ls)

d.setdefault("cipa", None)

print(d)

gen_expression = list(x for x in range(6))
print(gen_expression)


def palindrome_check(wrd: str) -> bool:
    if wrd == wrd[::-1]:
        return True
    return False


print(palindrome_check(wrd="afd"))

lt = [3, 6, 2, 1, 7]

ss = {lt, 1, "s"}
print(ss)
