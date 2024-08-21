#program to check if the alphabet is vowel or consonant.
alphabet=input("Enter an alphabet to check if the alphabet is vowel or consonant:")
if alphabet in ('a','e','i','o','u'):
    print(alphabet,"is a vowel")
else:
    print(alphabet,"is consonant")