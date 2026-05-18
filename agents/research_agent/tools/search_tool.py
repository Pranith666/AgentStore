from core.tool_interface import run_llm_prompt


def run(input, llm, config):

    result = run_llm_prompt(input, llm, config)

    if llm is None:
        return f"Search prompt: {result}"

    return result
