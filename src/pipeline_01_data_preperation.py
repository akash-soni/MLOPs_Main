import os
import argparse
import yaml # yet another markup language
import logging

def read_paramaters(config_path):
    """
    function which will read from configuration file and will return the what was read from configuration file
    """
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def main(config_path, datasource):
    config = read_paramaters(config_path)
    print(config)

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    default_config_path = os.path.join("config", "params.yaml")
    args.add_argument("--config", default = default_config_path)
    args.add_argument("--datasource", default = None)

    parsed_args = args.parse_args()
    print(parsed_args)

