from GetPageLinksTitles import get_page_link_titles
from GetPageSections import get_page_sections

def wiki_get_linked_sections(TITLE):
    pagelinks_titles = get_page_link_titles(TITLE)

    print(f"The number of links on page '{TITLE}' is:", len(pagelinks_titles))
    print(f"List of link titles on page {TITLE}:", pagelinks_titles)

    all_related_sections = []

    for pagetitle in pagelinks_titles:
        sections = get_page_sections(pagetitle)
        for section in sections:
            all_related_sections.append(section)


    print(f"A long list of all sections on pages linked from '{TITLE}':", all_related_sections)

    return all_related_sections




