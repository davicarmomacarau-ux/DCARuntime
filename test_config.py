from core.config_manager import ConfigManager


config = ConfigManager()


print(
    config.load()
)


config.set(
    "version",
    "0.7.0"
)


print(
    config.load()
)