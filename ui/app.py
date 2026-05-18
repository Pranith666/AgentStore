from pathlib import Path
import sys

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from core.agent_loader import get_agents, load_config

st.set_page_config(
    page_title="Agent Builder",
    page_icon="🛂",
    layout="wide",
)


def render_sidebar() -> tuple[dict | None, dict | None]:
    st.sidebar.title("Agent Builder")
    st.sidebar.caption("Select an agent workspace")

    st.sidebar.divider()
    st.sidebar.subheader("Agents")

    if st.sidebar.button("Refresh Agents", use_container_width=True):
        st.rerun()

    agents = get_agents()

    if not agents:
        st.sidebar.info("No agents found.")
        return None, None

    selected_folder = st.sidebar.selectbox(
        "Select agent",
        options=[agent["folder_name"] for agent in agents],
        format_func=lambda folder_name: next(
            (
                agent.get("name") or agent["folder_name"]
                for agent in agents
                if agent["folder_name"] == folder_name
            ),
            folder_name,
        ),
    )

    selected_agent = next(
        agent for agent in agents if agent["folder_name"] == selected_folder
    )
    config = load_config(selected_agent["folder_name"])

    if selected_agent.get("description"):
        st.sidebar.caption(selected_agent["description"])
    
    #st.sidebar.subheader("Tools")
    #tools = config.get("tools", [])

    #if tools:
     #   for tool_name in tools:
      #      st.sidebar.write(tool_name)
    #else:
     #   st.sidebar.info("No tools configured.")
        st.sidebar.subheader("Tools")

    tools = config.get("tools", [])
    tool_configs = config.get("tool_configs", {})

    tool_icons = {
        "search_tool": "🔍",
        "summarize_tool": "📝",
        "draft_tool": "✍️",
        "edit_tool": "🛠️",
    }

    if tools:
        for tool_name in tools:
            tool_config = tool_configs.get(tool_name, {})

            icon = tool_icons.get(tool_name, "🔧")

            pretty_name = (
                f"{icon} "
                f"{tool_name.replace('_', ' ').title()}"
            )

            with st.sidebar.expander(pretty_name):
                st.write("Tool Interface:")
                st.code("run(input, llm, config)")

                st.write("Configuration:")
                st.json(tool_config)

    else:
        st.sidebar.info("No tools configured.")

    return selected_agent, config

def render_main_layout(selected_agent: dict | None, config: dict | None) -> None:
    st.title("Generic Agent Builder")
    st.caption("Create, edit, and run agents from one workspace.")

    chat_column, config_column = st.columns([2, 1], gap="large")

    with chat_column:
        st.subheader("Agent Chat")
        st.info("Chat interface will be added in a later phase.")
        st.text_input("Message", placeholder="Ask an agent something...", disabled=True)
        st.button("Send", disabled=True)

    with config_column:
        st.subheader("Agent Details")

        if selected_agent and config:
            st.write(f"Selected: {selected_agent.get('name') or selected_agent['folder_name']}")
            st.json(config)
        else:
            st.info("Select an agent to view its configuration.")

        with st.expander("Tool Editor", expanded=True):
            st.text_area(
                "Prompt",
                placeholder="Tool prompt editor placeholder",
                disabled=True,
            )
            st.text_area(
                "Remarks",
                placeholder="Describe requested tool changes...",
                disabled=True,
            )
            st.button("Apply Remarks", disabled=True)


selected_agent, selected_config = render_sidebar()
render_main_layout(selected_agent, selected_config)
