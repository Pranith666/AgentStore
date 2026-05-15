from core.agent_loader import load_config


def build_agent(agent_name):

    config = load_config(agent_name)

    return config