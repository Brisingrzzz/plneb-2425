def splitAndLower(s):
    new_s = ""
    for word in s.lower().split():
        new_s += word
    return new_s

#ex1
#given a string "s", returns the reverse string

def reverseString(s):
    return s[::-1]

#ex2
#given a string "s", returns how many of a given character (case insensitive) are present in it.

def countCharacters(char, s):
    return s.lower().count(char)

#ex3
#given a string "s", returns the number of vowels there are present in it

def countVowels(s):
    res = 0
    vowels = "aeiou"
    for char in s.lower():
        if char in vowels:
            res += 1

    return res

#ex4
#given a string "s", convert it into lowercase

def lowerString(s):
    return s.lower()

#ex5
#given a string "s", convert it into uppercase

def upperString(s):
    return s.upper()

#ex6
#check if a given string "s" is a palindrome

def isPalindrome(s):
    new_s = splitAndLower(s)
    if new_s == reverseString(new_s):
        return True
    else:
        return False

#ex7
#check if two given strings, "s1" and "s2", are balanced (if all characters in s1 are present in s2 or vice versa)

def areBalanced(s1, s2):
    return set(s1).issubset(set(s2)) or set(s2).issubset(set(s1))

#ex8
#counts the number of times "s1" appears in "s2"

def countOccurences(s1, s2):
    return s2.count(s1) if len(s1) else 0

#ex9
#for two given strings, "s1" and "s2", check if "s1" is an anagram of "s2"

#easy way
#def isAnagram(s1, s2):
#    return sorted(splitAndLower(s1)) == sorted(splitAndLower(s2))

#using a hash map/dictionary

def isAnagram(s1, s2):
    new_s1 = splitAndLower(s1)
    new_s2 = splitAndLower(s2)
    if len(new_s1) != len(new_s2):
        return False

    charCount = {}

    for char in new_s1:
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1
    for char in new_s2:
        if char not in charCount or charCount[char] <= 0:
            return False
        charCount[char] -= 1

    for char in charCount:
        if charCount[char] != 0:
            return False

    return True

#ex10
#for a given list of strings returns the anagram table for said list

def anagramTable(s_list):
    anagram_table = {}
    for string in s_list:
        key = ''.join(sorted(splitAndLower(string)))
        if key not in anagram_table:
            anagram_table[key] = [string]
        else:
            anagram_table[key].append(string)

    return anagram_table

if __name__ == '__main__':
    #ex1
    # use case
    print("\n----- EXERCÍCIO 1 -----")
    print(f'Exemplo da reversão de uma string\nOriginal: hello world\nReverso: {reverseString("hello world")}')

    # ex2
    # use case
    print("\n----- EXERCÍCIO 2 -----")
    print(f'Conta o número de "a" e "A" numa string\nOriginal: BANana\nNum: {countCharacters("a", "BANana")}')

    # ex3
    # use case
    print("\n----- EXERCÍCIO 3 -----")
    print(f'Conta o número de vogais presentes numa string\nOriginal: hello world\nNum: {countVowels("hello world")}')

    # ex4
    # use case
    print("\n----- EXERCÍCIO 4 -----")
    print(f'Converte uma string para minúscula\nOriginal: HELLO WORLD\nMinúscula: {lowerString("HELLO WORLD")}')

    # ex5
    # use case
    print("\n----- EXERCÍCIO 5 -----")
    print(f'Converte uma string para maiúscula\nOriginal: hello world\nMaiúscula: {upperString("hello world")}')

    # ex6
    # use case
    print("\n----- EXERCÍCIO 6 -----")
    print(f'Verifica se uma string é capicua\nOriginal: Sit on a potato pan Otis\nÉ capicua: {isPalindrome("Sit on a potato pan Otis")}')

    # ex7
    # use case
    print("\n----- EXERCÍCIO 7 -----")
    print(f'Verifica se duas strings estão balanceadas\ns1 = hello, s2 = world\nEstão balanceadas: {areBalanced("hello", "world")}')
    print(f'\ns1 = wor, s2 = world\nEstão balanceadas: {areBalanced("wor", "world")}')
    print(f'\ns1 = world, s2 = wor\nEstão balanceadas: {areBalanced("world", "wor")}')

    # ex8
    # use case
    print("\n----- EXERCÍCIO 8 -----")
    print(f'Conta o número de ocorrências de s1 em s2\ns1: hello, s2 = hello world hello\nNum: {countOccurences("hello", "hello world hello")}')

    # ex9
    # use case
    print("\n----- EXERCÍCIO 9 -----")
    print(f'Verifica se s1 é anagrama de s2\ns1 = dlwor, s2 = world\nÉ anagrama: {isAnagram("dlwor", "world")}')
    print(f'\ns1 = Sit on a potato pan Otis, s2 = SitonapotatopanOtis\nÉ anagrama: {isAnagram("Sit on a potato pan Otis", "SitonapotatopanOtis")}')

    # ex10
    # use case
    print("\n----- EXERCÍCIO 10 -----")
    print(f'''Dada uma lista de strings cria a tabela de anagramas dessa lista\n
Original: ["roma", "amor", "sacas", "casas", "tigre", "tiger", "iceman", "cinema", "listen", "silent", "Sit on a potato pan Otis", "SitonapotatopanOtis"] \n
Tabela de anagramas: {anagramTable(["roma", "amor", "sacas", "casas", "tigre", "tiger", "iceman", "cinema", "listen", "silent","Sit on a potato pan Otis", "SitonapotatopanOtis"])}''')