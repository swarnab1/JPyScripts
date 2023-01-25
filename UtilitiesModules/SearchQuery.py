import webbrowser


def SearchQuery():
    print("\nThis program will open a search query in your default browser.")

    while True:
        userSearchService = input("SearchEngine >>> Enter Google, Bing, DuckDuckGo or exit: ")
        if userSearchService != "" and userSearchService == "google" or userSearchService == "bing" \
                or userSearchService == "duckduckgo":
            while True:
                userSearchQuery = input(userSearchService.capitalize() + "Search >>> Enter your search query: ")
                if userSearchQuery == "":
                    print("Enter a query")
                    continue
                else:
                    webbrowser.open("https://www." + userSearchService.casefold() + ".com/search?q=" + userSearchQuery,
                                    new=0, autoraise=True)
                    print("To search again, press Enter. To exit, type anything and press Enter.")
                    if input("SearchEngine >>> ") == "":
                        break
                    else:
                        return
        elif userSearchService == "exit":
            return
        else:
            print("Enter a valid service")
            continue
