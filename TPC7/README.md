# TPC 7

## Descrição geral

O objetivo deste TPC é acrescentar uma rota para uma tabela à aplicação desenvolvida ao longo das últimas aulas. Esta rota tem as seguintes funcionalidades adicionais pedidas e detalhadas de seguida.

### Navbar:

Foi adicionada uma nova entrada na Navbar. Para isso foi criada uma nova rota `/conceitos/tabela` que passa os items da base de dados para o template `table.html`.


### Estilo da tabela:

Para embelezar a tabela de designações - descrições foi acrescentada a funcionalidade de mudar de cor de fundo da linha da tabela aquando do hover.

### Regex Search:

Para permitir a pesquisa com expressões regulares (regex) na tabela de designações - descrições, foi definida a opção de regex no ficheiro de configuração, `conceito.js`

### Extra
Foi adicionada a feature de carregar na designação e ser redirecionado para a página da designação e respetiva descrição, semelhante ao implementado na página de conceitos.