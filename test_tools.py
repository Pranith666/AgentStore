import os

from core.tool_loader import get_agent_tools


def get_llm():
    if os.getenv("USE_OPENAI_LLM") != "1":
        return None

    from core.llm_provider import OpenAILLM

    return OpenAILLM()


llm = get_llm()

for agent_name in ["research_agent", "writing_agent"]:
    print(f"\n=== {agent_name.upper()} TOOLS ===\n")

    tools = get_agent_tools(agent_name)

    for tool in tools:
        print(tool["name"])
        print(tool["module"].run("AI agents", llm, tool["config"]))
