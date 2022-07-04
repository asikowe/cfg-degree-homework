USE BookStore;

-- Given two SQL tables below: authors and books.
-- ● The authors dataset has 1M+ rows
-- ● The books dataset also has 1M+ rows
-- Create an SQL query that shows the TOP 3 authors who sold the
-- most books in total!

CREATE INDEX indx_books on authors(book_name);
CREATE INDEX indx_books on books(book_name);

SELECT a.author_name FROM authors a
INNER JOIN books b ON b.book_name = a.book_name
GROUP BY a.author_name
HAVING sum(b.sold_copies) > 1
ORDER BY sum(b.sold_copies) DESC
LIMIT 3;

