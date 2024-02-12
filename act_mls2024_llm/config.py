import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="act_mls2024_llm",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="act_mls2024_llm_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from act_mls2024_llm.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export act_mls2024_llm_KEY=value
export act_mls2024_llm_KEY="@int 42"
export act_mls2024_llm_KEY="@jinja {{ this.db.uri }}"
export act_mls2024_llm_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
act_mls2024_llm_ENV=production act_mls2024_llm run
```

Read more on https://dynaconf.com
"""
