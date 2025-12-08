# Investigate [fastapi-users](https://fastapi-users.github.io/fastapi-users/latest/)
Don't forget:
* install requirements by poetry:
```
poetry install
```
* run docker compose:
```
docker compose up -d pg
```
* create secret:
```shell
python3 -c 'import secrets; print(secrets.token_hex())'
```
