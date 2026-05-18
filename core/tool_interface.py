from typing import Any, Protocol


class Tool(Protocol):

    def run(self, input: str, llm: Any, config: dict) -> str:
        ...


def run_llm_prompt(input: str, llm: Any, config: dict) -> str:
    prompt_template = config.get("prompt", "{input}")
    prompt = prompt_template.format(input=input)

    if llm is None:
        return prompt

    if hasattr(llm, "invoke"):
        response = llm.invoke(prompt)
    elif callable(llm):
        response = llm(prompt)
    else:
        raise TypeError("llm must be callable or expose invoke(prompt)")

    return str(response)
