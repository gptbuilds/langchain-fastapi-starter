# Langchain FastAPI docker traefik starter

## Dev

`docker compose up --build`

To smoke test:

`curl -H Host:fastapi.localhost http://0.0.0.0:81/ping`

Note dev is running on port 81 because I had some other service running on
port 80 already. 

To test the Agent:
`curl -H Host:fastapi.localhost -X POST -H "Content-Type:
application/json" -d '{"message": "can you run the tool properly? Make
up params and test"}' http://0.0.0.0:81/test-agent`

The agent is a structured chat agent, the example tool in
`services/api/toolset/empty_tool.py` is an asynchronous tool that takes
multiple inputs.

## Prod

Change `docker-compose.prod.yml` and add your domain in:

```
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.fastapi.rule=Host(`sub.domain.com`)"
      - "traefik.http.routers.fastapi.tls=true"
      - "traefik.http.routers.fastapi.tls.certresolver=letsencrypt"
```

Change `services/traefik/traefik.prod.toml` and add your email in:

```
[certificatesResolvers.letsencrypt.acme]
  email = "your@email.com"
  storage= "acme.json"
  [certificatesResolvers.letsencrypt.acme.httpChallenge]
    entryPoint = "web"
```

`docker-compose -f docker-compose.prod.yml up --build`

To smoke test:

`curl https://sub.domain.com`
