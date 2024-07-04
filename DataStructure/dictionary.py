# Define a dictionary to store book information
favorite_book = {
    'title': 'To Kill a Mockingbird',
    'author': 'Harper Lee',
    'genre': 'Fiction'
}

# Retrieve the genre using the get() method
book_genre = favorite_book.get('genre')
print(book_genre)