SELECT au_id, SUM(step2.advance + total_sales_per_title_and_author)
FROM (
	SELECT step1.title_id, step1.au_id, SUM(step1.sales_royalty) AS total_sales_per_title_and_author, step1.advance
	FROM (
		SELECT ta.title_id, au_id, t.advance, t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100 AS sales_royalty
		FROM titleauthor ta
		INNER JOIN titles t ON ta.title_id = t.title_id
		INNER JOIN sales s ON ta.title_id = s.title_id
        ) step1
	GROUP BY au_id, title_id
    ) step2
GROUP BY au_id;

CREATE TEMPORARY TABLE advance_royalty
SELECT ta.title_id, au_id, t.advance, t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100 AS sales_royalty
FROM titleauthor ta
INNER JOIN titles t ON ta.title_id = t.title_id
INNER JOIN sales s ON ta.title_id = s.title_id;

CREATE TEMPORARY TABLE advance_sum_royalty
SELECT advance_royalty.title_id, advance_royalty.au_id, SUM(advance_royalty.sales_royalty) AS total_sales_per_title_and_author, advance
FROM advance_royalty
GROUP BY au_id, title_id, advance;

SELECT au_id, SUM(advance_sum_royalty.advance + total_sales_per_title_and_author)
FROM advance_sum_royalty
GROUP BY au_id;

CREATE TABLE most_profiting_authors(
au_id VARCHAR(15),
profits FLOAT(10)
);

INSERT INTO most_profiting_authors (au_id, profits)
SELECT au_id, SUM(advance_sum_royalty.advance + total_sales_per_title_and_author) AS profits
FROM advance_sum_royalty
GROUP BY au_id
ORDER BY profits DESC;

SELECT * FROM most_profiting_authors