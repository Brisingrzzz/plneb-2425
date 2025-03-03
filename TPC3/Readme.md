# TPC3: gerar um ficheiro html para agregação e visualização dos dados.

## Descrição geral

O presente trabalho foi realizado com base na atividade desenvolvida na TP3 e com o objetivo de melhorar a captura de informação do dicionário médico disponibilizado, pretendendo lidar de melhor forma com caracteres indesejados de forma a gerar um ficheiro `html` para **agregação** e **visualização** dos dados.

Tendo isto em conta, o programa segue a estrutura desenvolvida na aula, mantendo as etapas de leitura, marcação dos conceitos, extração dos mesmos, limpeza das descrições e geração do ficheiro html. Este TPC prentende incidir sobre a etapa de limpeza do ficheiro `.txt` lido.

## Implementação

De forma a remover os caracteres de quebra de página **\f**, foram aplicadas as duas expressões regulares apresentadas de seguida.


`texto = re.sub(r"\f(?=[a-zØ-öø-ÿ])", "", texto)`

Esta expressão procura identificar os caracteres **\f** localizados antes de letras minúsculas, incluindo caracteres acentuados, com o propósito de identificar os caracteres **\f** que precedem conceitos ou linhas intermédias da descrição. Para a marcação poder ocorrer normalment é realizada a remoção dos caracteres identificados.

`texto = re.sub(r"\n\f", "", texto)`

Esta segunda expressão tem como objetivo identificar os caracteres **\f** que precedem as frases iniciais das descrições. Neste caso, é necessário remover os caracteres **\f** e o **\n** que o precede de forma a manter a coesão entre conceito e descrição para a marcação.

Sendo assim, todos os caracteres indesejados foram removidos de forma apropriada e a marcação desenvolvida na aula pode decorrer normalmente. Os seguintes passos seguem a lógica discutida na aula, obtendo finalmente a organização e exibição dos dados de forma simples e facilmente interpretável no formato html pretendido.

Os ficheiros de dados pdf e txt estão incluídos, assim como o html gerado para verificação de resultados.