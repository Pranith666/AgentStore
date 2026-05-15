import os
import json


AGENTS_FOLDER = "agents"


def get_agents():

    agents = []

    if not os.path.exists(AGENTS_FOLDER):
        return agents

    for item in os.listdir(AGENTS_FOLDER):

        agent_path = os.path.join(
            AGENTS_FOLDER,
            item
        )

        config_path = os.path.join(
            agent_path,
            "config.json"
        )

        if os.path.isdir(agent_path) and os.path.exists(config_path):

            with open(config_path, "r") as file:
                config = json.load(file)

            agents.append({
                "folder_name": item,
                "name": config.get("name"),
                "description": config.get("description")
            })

    return agents

def load_config(agent_name):

    config_path = os.path.join(
        AGENTS_FOLDER,
        agent_name,
        "config.json"
    )

    if not os.path.exists(config_path):
        raise FileNotFoundError(
            f"No config found for {agent_name}"
        )

    try:

        with open(config_path, "r") as file:
            config = json.load(file)

        return config

    except json.JSONDecodeError:

        raise ValueError(
            f"Invalid JSON in {agent_name}"
        )