from core.agent_loader import (
    get_agents,
    load_config
)


print("\n=== AVAILABLE AGENTS ===\n")

agents = get_agents()

for agent in agents:

    print(agent)

print("\n=== LOADED CONFIG ===\n")

if agents:

    first_agent = agents[0]["folder_name"]

    config = load_config(first_agent)

    print(config)