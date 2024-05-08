from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=['settings.toml', '.secrets.toml'],
    environments=True,
    default_env="default",
    env="development",
)

# from dynaconf import inspect_settings
# print(inspect_settings(settings))   