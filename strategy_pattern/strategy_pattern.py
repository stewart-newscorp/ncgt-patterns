# strategy pattern

import json
import yaml
import toml
from abc import ABC, abstractmethod

class ConfigStrategy(ABC):
    @abstractmethod
    def read_config(self, file_path):
        pass

class JsonConfigStrategy(ConfigStrategy):
    def read_config(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

class YamlConfigStrategy(ConfigStrategy):
    def read_config(self, file_path):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)

class TomlConfigStrategy(ConfigStrategy):
    def read_config(self, file_path):
        with open(file_path, 'r') as file:
            return toml.load(file)

def create_config_reader(file: str) -> ConfigStrategy:
    if file.endswith(".json"):
        return JsonConfigStrategy()
    elif file.endswith(".toml"):
        return TomlConfigStrategy()
    elif file.endswith(".yaml"):
        return YamlConfigStrategy()
    else:
        raise Exception("Could not find config strategy")

# Usage example
if __name__ == "__main__":
    config_file = "config.yaml" # config.toml, config.yaml, config.json
    config_reader = create_config_reader(config_file)
    config = config_reader.read_config(config_file)
    print(config)
