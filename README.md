# diary-backend
Backend for [diary web app](https://csgang.xyz/r/diary).

## Dev instructions
The project uses Poetry for package management.
```
poetry install
```
to install all dependencies.

Then, install pre-commit hooks with
```
poetry run pre-commit install
```

To initialize the database and generate the DB client, run
```
poetry run prisma db push
```

### Migrations
Migrations are managed by Prisma, read the [Prisma docs](https://www.prisma.io/docs/concepts/components/prisma-migrate) for more info.
