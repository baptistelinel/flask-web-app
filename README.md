# Web app

## Start the server

```
make start_app
```

The application runs on http://localhost:8888.

## Docker containers information

| Name  |Image  |Port   |
|---|---|---|
|web_app    |blinel/web_app |5000->5000/tcp |
|postgres   |postgres       |5432->5432/tcp |
