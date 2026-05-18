import importlib.util
from pathlib import Path

from core.agent_loader import AGENTS_FOLDER, load_config


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def get_agent_tools(agent_name):
    config = load_config(agent_name)
    tools = []

    for tool_name in config.get("tools", []):
        module = load_tool(agent_name, tool_name)
        tool_config = config.get("tool_configs", {}).get(tool_name, {})

        tools.append({
            "name": tool_name,
            "module": module,
            "config": tool_config,
        })

    return tools


def load_tool(agent_name, tool_name):
    tool_path = (
        PROJECT_ROOT
        / AGENTS_FOLDER
        / agent_name
        / "tools"
        / f"{tool_name}.py"
    )

    if not tool_path.exists():
        raise FileNotFoundError(f"No tool found at {tool_path}")

    module_name = f"{agent_name}_{tool_name}"
    spec = importlib.util.spec_from_file_location(module_name, tool_path)

    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load tool module: {tool_name}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if not hasattr(module, "run") or not callable(module.run):
        raise AttributeError(f"Tool {tool_name} must define run(input, llm, config)")

    return module
