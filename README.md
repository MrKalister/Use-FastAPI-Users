# Investigate [fastapi-users](https://fastapi-users.github.io/fastapi-users/latest/)
Don't forget:
* install requirements by poetry:
```shell
poetry install
```
* run docker compose:
```shell
docker compose up -d pg
```
* apply migrations due to alembic:
```shell
alembic upgrade head
```

## Additional short hints
* create secret:
```shell
python3 -c 'import secrets; print(secrets.token_hex())'
```
* to stop docker compose:
```shell
docker compose stop
```
* to stop and remove docker compose:
```shell
docker compose down
```
* downgrade migration:
```shell
alembic downgrade -1
```
or (to go to the absolute beginning)
```shell
alembic downgrade base
```

