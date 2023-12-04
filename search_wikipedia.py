import wikipediaapi

def search_wikipedia(query):
    """
    Search Wikipedia and display the summary of the first result.

    Parameters:
    - query (str): The user's search query.

    Returns:
    - str: The summary of the first result or an error message.
    """
    wiki_wiki = wikipediaapi.Wikipedia('en')

    # Search Wikipedia
    page_py = wiki_wiki.page(query)

    # Display the summary of the first result
    if page_py.exists():
        return page_py.summary[:500]  # Displaying the first 500 characters of the summary
    else:
        return f"Error: No results found for '{query}' on Wikipedia."

if __name__ == "__main__":
    # Example usage
    user_query = input("Enter your Wikipedia search query: ")
    result = search_wikipedia(user_query)
    print(result)
