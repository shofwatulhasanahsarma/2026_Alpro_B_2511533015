# Name: <Shofwatul Hasanah Sarma>
# NIM: <2511533015>
# Bonus

sentence = input("Kalimat: ")

cleaned = sentence.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
