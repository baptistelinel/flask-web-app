# Web app

## Start application

```
make start_app
```

The application runs on http://localhost:5000.

## Destroy application

```
make destroy_app
```

## Docker containers information

| Name  |Image  |Port   |
|---|---|---|
|web    |web_app_web |5000->5000/tcp |
|database   |web_app_database       |5432->5432/tcp |
