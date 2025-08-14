def recommend_books_by_genre():
    # Take input for book names and genres
    book_names = input("Enter book names (comma separated): ").split(',')
    genres = input("Enter genres for each book (comma separated, in order): ").split(',')

    # Clean up whitespace
    book_names = [name.strip() for name in book_names]
    genres = [genre.strip() for genre in genres]

    # Map books to genres
    book_genre_map = {}
    for book, genre in zip(book_names, genres):
        book_genre_map[book] = genre

    # Ask user for preferred genre
    preferred_genre = input("Enter genre: ").strip()

    # Find and print books matching the preferred genre
    recommended_books = [book for book, genre in book_genre_map.items() if genre.lower() == preferred_genre.lower()]
    if recommended_books:
        print("Recommended books:")
        for book in recommended_books:
            print(book)
    else:
        print("No books found for the given genre.")

# Example usage
if __name__ == "__main__":
    recommend_books_by_genre()
