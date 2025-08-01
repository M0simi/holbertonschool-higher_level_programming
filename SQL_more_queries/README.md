# SQL - More Queries

This project focuses on more advanced SQL concepts and query techniques using MySQL. The goal is to reinforce understanding of relationships between tables, permissions, subqueries, joins, and grouping data.

## 📚 Topics Covered
- Creating users and granting privileges
- Managing databases and tables
- `NOT NULL`, `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY` constraints
- Inserting and selecting data with filters
- Using `JOIN` and `LEFT JOIN`
- Performing subqueries
- Aggregation with `GROUP BY` and `HAVING`

## 🗃️ Files Description

| File | Description |
|------|-------------|
| `0-privileges.sql` | Lists all privileges for specific MySQL users |
| `1-create_user.sql` | Creates a user with password and grants privileges |
| `2-create_read_user.sql` | Creates a DB and read-only user for it |
| `3-force_name.sql` | Creates a table with a NOT NULL column |
| `4-never_empty.sql` | Creates a table with NOT NULL constraints |
| `5-unique_id.sql` | Creates a table with a unique constraint on an ID |
| `6-states.sql` | Creates a table with `id` as `PRIMARY KEY` |
| `7-cities.sql` | Creates a table with a `FOREIGN KEY` to `states` |
| `8-cities_of_california_subquery.sql` | Lists cities in California (without JOIN) |
| `9-cities_by_state_join.sql` | Lists cities with their state using JOIN |
| `10-genre_id_by_show.sql` | Lists shows with at least one genre |
| `11-genre_id_all_shows.sql` | Lists all shows, includes those without genre |
| `12-no_genre.sql` | Lists shows that have no genre linked |
| `13-count_shows_by_genre.sql` | Counts number of shows per genre |
| `14-my_genres.sql` | Lists genres of the show "Dexter" |
| `15-comedy_only.sql` | Lists shows that are only in the "Comedy" genre |
| `16-shows_by_genre.sql` | Lists all shows and their genres (NULL if none) |

---

## ⚙️ Usage

To test a script:

```bash
cat <filename.sql> | mysql -uroot -p <database_name>
```
---

## ✍️ Author
[Meshari - M0simi](https://github.com/M0simi)
