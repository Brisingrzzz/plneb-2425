# TPC1: Manipulação de Strings em Python

Este projeto contém diversas funções para a **manipulação de strings** realizando alguns  **testes automáticos**.

---

## **Lista de Funções Implementadas**

Em seguida apresentam-se todas as funções implementadas no projeto, em conjunto com uma breve descrição e exemplo.

### 1. **`reverseString(s)`:**
 **Descrição:** Inverte uma string usando **slicing** (`[::-1]`).  
 **Exemplo:** `reverseString("hello world")` retorna `"dlrow olleh"`

### 2. **`countCharacters(char, s)`:**
 **Descrição:** A string é colocado em **minúsculas**, é percorrida e sempre que for encontrado um caracter pretendido (`char`) é incrementado um **contador**.  
 **Exemplo:** `countCharacters("a", "BANana")` retorna `3`

### 3. **`countVowels(s)`:**
 **Descrição:** A string é colocada em **minúsculas**, é percorrida e sempre que for encontrado um caracter que pertence a uma string previamente definida (`"aeiou"`) é incrementado um **contador**.  
 **Exemplo:** `countVowels("hello world")` retorna `3`

### 4. **`lowerString(s)`:**
 **Descrição:** Converte a string para minúsculas recorrendo ao método **.lower()**.  
 **Exemplo:** `lowerString("HELLO WORLD")` retorna `"hello world"`

### 5. **`upperString(s)`:**
 **Descrição:** Converte a string para maiúsculas recorrendo ao método **.upper()**.  
 **Exemplo:** `upperString("hello world")` retorna `"HELLO WORLD"`

### 6. **`isPalindrome(s)`:**
 **Descrição:** Começa por remover *whitespaces* e colocar a string em *lowercase* e utiliza a função `reverseString` anteriormente descrita para comparar a string **original** e o seu **inverso**.  
 Reconhece tanto uma **única palavra** como uma **frase**.  
 **Exemplo:** `isPalindrome("Sit on a potato pan Otis")` retorna `True`

### 7. **`areBalanced(s1, s2)`:**
 **Descrição:** Verifica se o **set** dos caracteres de **s1** é um **subset** do **set** dos caracteres de **s2**, ou **vice versa**.  
 **Exemplo 1:** `areBalanced("hello", "world")` retorna `False`
 **Exemplo 2:** `areBalanced("wor", "world")` retorna `True`
 **Exemplo 3:** `areBalanced("world", "wor")` retorna `True`

### 8. **`countOccurences(s1, s2)`:**
 **Descrição:** Utiliza o método .count() de uma string para contar as ocorrências de **s1** em **s2**. Se **s1** for uma **string vazia** é devolvido `0`.  
 **Exemplo:** `countOccurences("hello", "hello world hello")` retorna `2`

### 9. **`isAnagram(s1, s2)`:**
 **Descrição:** Primeiro é verificado se as strings têm **tamanhos** diferentes, retornando `False` se isso ocorrer. Procede removendo *whitespaces* e colocando a string em *lowercase*, de seguida são **mapeados** as **contagens** de todos os diferentes caracteres de s1, itera-se sobre s2 de forma semelhante verificando a cada iteração se o caracter está presente no **mapa** anterior e se o respetivo **contador** é **maior que 0**, caso nenhuma destas condições seja verificada a função retorna `False`, caso contrário o **contador** é **decrementado por 1**.  
 Após a iteração sobre s2 é verificado se no **mapa** existe algum valor **superior a 0**, caso exista a funçâo retorna `False`.  
 Finalmente se nenhuma destas condições se verificar é retornado `True`.  
 **Nota**: é possível obter os mesmos resultados utilizando as funções de sort para ordenar ambas as strings e comparando os resultados, este método pareceu mais ineficiente uma vez que envolve o uso de algoritmos de ordenação.  
 **Exemplo 1:** `isAnagram("dlwor", "world"),` retorna `True`  
 **Exemplo 2:** `isAnagram("Sit on a potato pan Otis", "SitonapotatopanOtis"),` retorna `True`

### 10. **`classes_anagramas(list)` e `tabela_anagramas(dici)`:**
 **Descrição:** Cada string da lista recebida é ordenada alfabeticamente e usada como chave num dicionário. Se a chave ainda não existir, cria-se uma entrada no dicionário com uma lista que contém essa string. Caso exista, a string é adicionada à lista que lhe corresponde. Finalmente obtemos um agrupamento das strings de acordo com a sua relação enquanto anagramas.  
 **Exemplo:** `tabela_anagramas(classes_anagramas(["amor", "mora", "ramo", "roma", "galo", "algo", "gola", "ator", "rato", "rota"])` retorna:

---

