class ResearchAgent:

    def __init__(self, config):

        self.name = config["name"]
        self.description = config["description"]
        self.model = config["model"]

    def run(self, query):

        return f"Researching: {query}"