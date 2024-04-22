import wikipedia


def main():
    while True:
        search_phrase = input("Search (or press Enter to quit): ").strip()
        if not search_phrase:
            break

        try:
            page = wikipedia.page(search_phrase, auto_suggest=False)
            print(f"Title: {page.title}")
            print(f"Summary: {page.summary}")
            print(f"URL: {page.url}")
        except wikipedia.DisambiguationError as e:
            print(f"Disambiguation error: {e.options}")
        except wikipedia.PageError:
            print("Page not found")


if __name__ == "__main__":
    main()
