import streamlit as st


st.set_page_config(
    page_title="Agent Builder",
    page_icon="🛂",
    layout="wide",
)


def render_sidebar() -> None:
    st.sidebar.title("Agent Builder")
    st.sidebar.caption("Phase 1 placeholder")

    st.sidebar.divider()
    st.sidebar.subheader("Agents")
    st.sidebar.info("Agent list will appear here.")

    st.sidebar.subheader("Tools")
    st.sidebar.info("Tool controls will appear here.")


def render_main_layout() -> None:
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
        st.info("Selected agent configuration will appear here.")

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


render_sidebar()
render_main_layout()
