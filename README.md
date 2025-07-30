# Books API

A simple REST API service in Python that allows you to manage book records.

---

## Endpoints

**`GET /books/`**: get all books.

**`GET /books/<id>/`**: retrieve a single book by id (will throw an error 404 if there is no book with such id).

**`POST /books/`**: create a book by specifying it's title, author's name and a year of publishing (will throw an error 400 if some fields are not present).

**Request body:**

```json
{
  "title": "Crime and Punishment",
  "author": "Fyodor Dostoevsky",
  "published_year": "1866"
}
```

---

## Setup and Usage

This project is preferred to run with `Docker compose`.

First you will need to get the code itself:

```bash
git clone https://github.com/ksmvrheee/books-api-test-task.git
cd books-api-test-task
```

Then you'll need to fill the `.env` file that contains environmental variables crucial for project to work.

### Environmental variables


| Variable                    | Role                                                                                                                         |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| DJANGO_SECRET_KEY           | Django secret key                                                                                                            |
| DEBUG                       | Django DEBUG variable (True/False)                                                                                           |
| DJANGO_ALLOWED_HOSTS        | List of allowed hosts for Django deployment (separated by commas)                                                            |
| DJANGO_PORT                 | Port for Django (8000 by default)                                                                                            |
| DJANGO_CSRF_TRUSTED_ORIGINS | List of trusted CSRF sources for Django (comma separated, with protocol (‘https://’), can be similar to the previous item) |
| DATABASE_ENGINE             | DB engine (`postgresql_psycopg2` for PostgreSQL by default).                                                                 |
| DATABASE_NAME               | DB name                                                                                                                      |
| DATABASE_USERNAME           | Username for the DB                                                                                                          |
| DATABASE_PASSWORD           | Password for the DB user                                                                                                     |
| DATABASE_HOST               | DB host (`db` by default, you should not modify that)                                                                        |
| DATABASE_PORT               | Port for the DB (`5432` for PostgreSQL by default, you should not modify that)                                               |

After you filled the `.env` file you can launch the project:

```bash
docker compose up --build
```

Now configure the ports and firewall and the application is ready to use.
