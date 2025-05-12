# TPC10  
## Web Scraping — Extração de Conteúdos da Revista Portuguesa de Medicina Interna

### Objetivo
Extrair conteúdos do website da Revista Portuguesa de Medicina Interna, utilizando a biblioteca **Beautiful Soup**, e
estruturar os dados de forma lógica e organizada no formato **JSON**.

### Implementação
Para atingir este objetivos o processo de *web scraping* foi dividido em várias etapas, cada uma com uma função dedicada:

- `get_html(url)`: Obtém o conteúdo HTML da página indicada pelo URL, utilizando a biblioteca Requests, e devolve-o como texto.

- `get_pages()`: Obtém todas as páginas que contêm edições da revista. Devolve uma lista de links.

- `get_archive_data(soup)`: Processa os elementos de uma lista de edições da revista, extraindo os metadados para cada volume encontrado. Devolve um dicionário onde cada chave corresponde ao título do volume.

- `get_issues_data(url)`: Extrai todos os artigos de uma edição específica da revista, juntamente com a sua data de publicação e URL. Devolve um dicionário estruturado com estes elementos.

- `get_issue_data(url)`: Recolhe dados detalhados de um artigo, incluindo:
  - Título (e título alternativo, se existir)
  - Data de publicação
  - Autores (com nome, afiliação e ORCID, quando disponíveis)
  - DOI
  - Palavras-chave
  - Resumo (abstract)
  - Link para o PDF

- `scrape_data()`: Função principal que inicia o processo. Percorre as páginas de arquivo da revista, e para cada página, extrai as edições e os seus artigos, escrevendo os dados para um ficheiro JSON.

### Funcionamento
O script começa por aceder à página de arquivo principal da revista e identifica todas as edições disponíveis. Para cada edição, extrai a informação sobre todos os artigos publicados, garantindo que são processados na versão em português quando disponível.

Durante a execução, o script guarda os dados no ficheiro `revista_data.json`, adicionando as informações extraídas de cada página de arquivo.

### Output
O resultado do programa é um ficheiro JSON com a seguinte estrutura:

```json
{
    "Mês 1/Mês 2 - Volume X, Número Y (Ano)": {
        "URL": "https://revista.spmi.pt/index.php/rpmi/issue/view/XX",
        "data_publicacao": "YYYY-MM-DD",
        "artigos": [
            {
                "URL": "https://revista.spmi.pt/index.php/rpmi/article/view/XX",
                "titulo": "Título do artigo",
                "titulo_alt": "Título alternativo (se existir)",
                "data_publicacao": "YYYY-MM-DD",
                "autores": [
                    {
                        "nome": "Nome do autor",
                        "afiliacao": "Afiliação do autor",
                        "orcid": "Identificador ORCID (se disponível)"
                    }
                ],
                "DOI": "https://doi.org/XXXX",
                "keywords": ["Palavra-chave 1", "Palavra-chave 2"],
                "abstract": ["Parágrafo 1 do resumo", "Parágrafo 2 do resumo"],
                "pdf": "Link para o PDF do artigo"
            },
            ...
        ]
    },
    ...
}
```

**Nota**: Apenas os campos existentes para cada artigo são incluídos no JSON. Alguns artigos podem não ter todos os campos.

### Requisitos
O script requer as seguintes bibliotecas Python:
- requests
- BeautifulSoup4
- json (biblioteca padrão)