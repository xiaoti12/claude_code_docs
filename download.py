import requests

base_url = "https://docs.anthropic.com/en/docs/claude-code"

cc_docs_names = [
    "overview",
    "quickstart",
    "common-workflows",
    "sdk",
    "sub-agents",
    "output-styles",
    "hooks-guide",
    "github-actions",
    "mcp",
    "troubleshooting",
    "overview",
    "amazon-bedrock",
    "google-vertex-ai",
    "corporate-proxy",
    "llm-gateway",
    "devcontainer",
    "setup",
    "iam",
    "security",
    "data-usage",
    "monitoring-usage",
    "costs",
    "analytics",
    "settings",
    "ide-integrations",
    "terminal-config",
    "memory",
    "statusline",
    "cli-reference",
    "interactive-mode",
    "slash-commands",
    "hooks",
    "legal-and-compliance",
]


def download_docs(doc_names: list[str]):
    for doc_name in doc_names:
        url = f"{base_url}/{doc_name}.md"
        response = requests.get(url)

        if response.status_code == 200:
            with open(f"{doc_name}.md", "w", encoding="utf-8") as file:
                file.write(response.text)
            print(f"Downloaded {doc_name}.md")
        else:
            print(f"Failed to download {doc_name}.md, status code: {response.status_code}")


if __name__ == "__main__":
    download_docs(cc_docs_names)
