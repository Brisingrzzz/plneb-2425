import json
import requests
from bs4 import BeautifulSoup


BASE_URL = "https://revista.spmi.pt/index.php/rpmi/issue/archive"
NUM_PAGES = 6


def get_html(url):
    html_content = requests.get(url).text

    if html_content:
        print(f"Fetched HTML content from {url}")
    else:
        print(f"Failed to fetch HTML content from {url}")

    return html_content

def get_pages():
    url = BASE_URL
    html_content = get_html(url)
    soup = BeautifulSoup(html_content, "html.parser")
    
    pages = []
    pages.append(url)
    next_page = soup.find("a", class_="next")
    
    while next_page:  
        pages.append(next_page["href"])
        html_content = get_html(next_page["href"])
        soup = BeautifulSoup(html_content, "html.parser")
        next_page = soup.find("a", class_="next")

    return pages

def get_archive_data(soup):
    archive_data = {}

    for list_item in soup.find_all("li"):
        months_div = list_item.find("a", class_="title")
        months = months_div.text.strip()
        extra_div = list_item.h2.div
        
        if months_div:
            url = months_div["href"]

        if extra_div:
            months += (" - " + extra_div.text.strip())

        archive_data[months] = get_issues_data(url)

    return archive_data

def get_issues_data(url):
    issues = []

    html_content = get_html(url)
    soup = BeautifulSoup(html_content, "html.parser")

    sections = soup.find("div", class_="sections")
    for h3 in sections.find_all("h3"):
        issue_url = h3.a["href"]
        issues.append(get_issue_data(issue_url))

    pub_date_div = soup.find("div", class_="published")
    pub_date = pub_date_div.find("span", class_="value").text.strip()

    return {
        "URL": url,
        "data_publicacao": pub_date,
        "artigos": issues,
    }


def get_issue_data(url):
    # Garantir que estamos na versão em português
    pre_html_content = get_html(url)
    pre_soup = BeautifulSoup(pre_html_content, "html.parser")
    
    pt_url = pre_soup.find("li", class_="locale_pt_PT").a["href"]
    
    html = get_html(pt_url)
    soup = BeautifulSoup(html, "html.parser")
    
    issue_data = {"URL": url}

    # Título
    issue_data["titulo"] = soup.find("h1", class_="page_title").text.strip().replace("  ", " ")

    # Título alternativo
    subtitle = soup.find("h2", class_="subtitle")
    if subtitle:
        issue_data["titulo_alt"] = subtitle.text.strip().replace("  ", " ")

    # Data de publicação
    issue_data["data_publicacao"] = soup.find("div", class_="item published").find("div", class_="value").text.strip().replace("  ", " ")

    # Autores
    author_list = soup.find("ul", class_="authors")
    author_values = []
    for li in author_list.find_all("li"):
        author_info = {}
        author_info["nome"] = li.find("span", class_="name").text.strip().replace("  ", " ")

        affiliation = li.find("span", class_="affiliation")
        if affiliation:
            author_info["afiliacao"] = affiliation.text.strip().replace("  ", " ")

        orcid = li.find("span", class_="orcid")
        if orcid:
            author_info["orcid"] = orcid.text.strip().replace("  ", " ")

        author_values.append(author_info)

    issue_data["autores"] = author_values

    # DOI
    doi_section = soup.find("section", class_="item doi")
    if doi_section:
        issue_data["DOI"] = doi_section.find("span", class_="value").a["href"]

    # Keywords
    key_section = soup.find("section", class_="item keywords")
    if key_section:
        issue_data["keywords"] = [key.strip().replace("  ", " ") for key in key_section.find("span", class_="value").text.split(",")]

    # Abstract
    abstract_section = soup.find("section", class_="item abstract")
    if abstract_section:
        abstract_data = []
        for p in abstract_section.find_all("p"):
            abstract_data.append(p.text.strip().replace("  ", " "))
        issue_data["abstract"] = abstract_data

    # Link to PDF
    pdf_url = soup.find("a", class_="obj_galley_link pdf")
    if pdf_url:
        issue_data["pdf"] = pdf_url["href"]
    
    return issue_data


def scrape_data():
    res = {}
    
    for page_url in get_pages():
        html_content = get_html(page_url)
        soup = BeautifulSoup(html_content, "html.parser")

        content_div = soup.find("ul", class_="issues_archive")
        data = get_archive_data(content_div)
        res.update(data)
    return res


if __name__ == "__main__":
    data = scrape_data()
    with open("revista_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)