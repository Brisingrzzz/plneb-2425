# TPC2: Expressões regulares em Python

Este TPC contém diversas funções que utilizam **expressões regulares** realizando alguns **testes**.

---

## **Lista de Funções Implementadas**

Em seguida apresentam-se todas as funções implementadas no TPC, em conjunto com uma breve descrição e exemplo.
Foi usado o módulo `re` e as suas funções para a realização de todos os exercícios.

### 1.1. **`helloStart(pattern, s)`:**
 **Descrição:** Utiliza a função **match** para determinar se `hello` aparece no início da frase utilizando a **anchor** `^`.  
 **Exemplo:** `helloStart("^hello", "hello world")` retorna `True`

### 1.2. **`hasHello(pattern, s)`:**
 **Descrição:** Utiliza a função **search** para determinar se `hello` aparece na frase.  
 **Exemplo:** `hasHello("hello", "hello world")` retorna `True`

### 1.3. **`findHello(pattern, s)`:**
 **Descrição:** Utiliza a função **findall** para procurar todas as ocurrências de `hello` na frase (é também **case insensitive**).  
 **Exemplo:** `findHello("hello", "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!")` retorna `['Hello', 'hello', 'hello', 'HELLO']`

### 1.4. **`subHello(pattern, sub, s)`:**
 **Descrição:** Utiliza a função **sub** para procurar todas as ocurrências de `hello` na frase e substitui-as por `*YEP*` (é também **case insensitive**).  
 **Exemplo:** `subHello("hello", "*YEP*", "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!")` retorna `"*YEP* there! Uh, hi, *YEP*, it's me... Heyyy, *YEP*? *YEP*!"`

### 1.5. **`upperString(s)`:**
 **Descrição:** Utiliza a função **split** para separar a frase a cada ocurrência de `,`.  
 **Exemplo:** `slitByComma(",", "bananas, laranjas, maçãs, uvas, melancias, cerejas, kiwis, etc.")` retorna `['bananas', ' laranjas', ' maçãs', ' uvas', ' melancias', ' cerejas', ' kiwis', ' etc.']`

### 2. **`palavra_magica(frase)`:**
 **Descrição:** Utiliza a função **search** para determinar se o padrão `'\bpor favor(\?|\.{1,3}|!\?)$'` aparece na frase (Frase **terminada** em `por favor` seguido de um **sinal de pontuação**).  
 **Exemplo 1:** `palavra_magica("Posso ir à casa de banho, por favor?")` retorna `True`  
 **Exemplo 2:** `palavra_magica("Preciso de um favor.")` retorna `False`

### 3. **`narcissismo(linha)`:**
 **Descrição:** Utiliza a função **findall** procurar todas as ocurrências do padrão `\beu\b` e conta as mesmas (ocurrências da palavra `eu` na frase, é também **case insensitive**).  
 **Exemplo:** `narcissismo("Eu não sei se eu quero continuar a ser eu. Por outro lado, eu ser eu é uma parte importante de quem EU sou.")` retorna `6`

### 4. **`troca_de_curso(linha, novo_curso)`:**
 **Descrição:** Utiliza a função **sub** para substituir o padrão `'\bLEI\b'` por `LEBiom` na frase (procura por `LEI`, é também **case sensitive**).  
 **Exemplo:** `troca_de_curso("LEI é o melhor curso! Adoro LEI! Gostar de LEI devia ser uma lei.", 'LEBiom')` retorna `"LEBiom é o melhor curso! Adoro LEBiom! Gostar de LEBiom devia ser uma lei."`

### 5. **`soma_string(linha)`:**
 **Descrição:** Utiliza a função **split** para separar a frase a cada ocurrência de `,`, seguidamente soma todos os números resultantes usando a função `sum`.  
 **Exemplo:** `soma_string("4,-6,2,3,8,-3,0,2,-5,1")` retorna `6`

### 6. **`pronomes(frase)`:**
 **Descrição:** Utiliza a função **findall** para procurar ocurrências de pronomes, `eu`, `tu`, `ele`, `ela`, `nós`, `vós`, `eles`, `elas` (é também **case insensitive**).  
 **Exemplo:** `pronomes("EU e TU vamos ao parque, enquanto ELE e ela preferem ficar em casa; NÓS tentamos convencê-los, mas vós e ELES não quiseram mudar de ideia, e ELAS apenas observaram.")` retorna `['EU', 'TU', 'ELE', 'ela', 'NÓS', 'vós', 'ELES', 'ELAS']`

### 7. **`variavel_valida(frase)`:**
 **Descrição:** Utiliza a função **search** para procurar ocurrências do padrão `'^[a-z]\w*$'` (começa por uma **letra** e apenas contém **letras**, **números** ou **underscores**).  
 **Exemplo 1:** `variavel_valida('variavel_teste1')` retorna `True`  
 **Exemplo 2:** `variavel_valida('variavel_teste1%')` retorna `False`  
 **Exemplo 3:** `variavel_valida('_variavel_teste1')` retorna `False`

### 8. **`inteiros(frase)`:**
 **Descrição:** Utiliza a função **findall** para procurar ocurrências de `inteiros` podendo estes ser **negativos** ou **positivos** contendo **um** ou **mais** dígitos.  
 **Exemplo:** `inteiros("-1231 132131 2 -2 a2")` retorna `['-1231', '132131', '2', '-2', '2']`

### 9. **`underscores(frase)`:**
 **Descrição:** Utiliza a função **sub** para procurar ocurrências de qualquer `whitespace` e substitui o mesmo por `_` (caso apareçam mais que um **whitespace** seguido é substituído por apenas um **underscore**).  
 **Exemplo 1:** `underscores("Eu e tu vamos ao parque, enquanto ele e ela preferem ficar em casa; nós tentamos convencê-los, mas vós e eles não quiseram mudar de ideia, e elas apenas observaram.")` retorna `"Eu_e_tu_vamos_ao_parque,_enquanto_ele_e_ela_preferem_ficar_em_casa;_nós_tentamos_convencê-los,_mas_vós_e_eles_não_quiseram_mudar_de_ideia,_e_elas_apenas_observaram."`  
 **Exemplo 2:** `underscores("Eu e tu vamos            ao parque")` retorna `Eu_e_tu_vamos_ao_parque`

### 10. **`codigos_postais(lista)`:**
 **Descrição:** Utiliza a função **split** para separar a frase a cada ocurrência de `-` criando um tuplo diferente para cada código postal.  
 **Exemplo:** `codigos_postais(lista = ["4700-000", "1234-567", "8541-543", "4123-974", "9481-025"])` retorna: `[('4700', '000'), ('1234', '567'), ('8541', '543'), ('4123', '974'), ('9481', '025')]`

---

