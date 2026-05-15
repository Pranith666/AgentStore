from core.agent_loader import get_agents, load_config


agents = get_agents()

print("Available Agents:")
print(agents)

print("\nAgent Configs:\n")

for agent in agents:

    config = load_config(agent)

    print(f"{agent}:")
    print(config)
    print()