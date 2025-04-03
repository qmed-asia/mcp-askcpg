# Qmed-AskCPG

**Qmed-AskCPG** is a Python package that allows clinicians and developers to query Malaysian Clinical Practice Guidelines (CPGs) using natural language. It leverages the MCP (Medical Content Pipeline) server to return structured responses based on official CPG references.

📦 PyPI: [https://pypi.org/project/mcp-askcpg/](https://pypi.org/project/mcp-askcpg/)

---

## 🔧 Installation

Install the package via pip:

```bash
pip install mcp-askcpg
```

---

## ⚙️ Manual Configuration (Example)

If you are using a `uvx`-based setup or a JSON-based task runner, you can manually configure the environment as follows:

```json
"clinical_practice_guide": {
  "command": "uvx",
  "args": ["mcp-askcpg"],
  "env": {
    "ASKCPG_API_KEY": "<PLEASE_ASK_ME>",
    "ASKCPG_BACKEND": "<PLEASE_ASK_ME>"
  }
}
```

> **Note:** Please contact the maintainer to obtain your `ASKCPG_API_KEY` and `ASKCPG_BACKEND` values.

---

## 💬 Example Query

Once the server is running, you can ask a question like:

```text
Please tell me the procedure of stroke management in CPG?
```

The system will return a structured response based on Malaysia’s official clinical guidelines.

---

## 📚 References

This project is built on the MCP structured reference system:

🔗 [https://github.com/adhikasp/mcp-twikit](https://github.com/adhikasp/mcp-twikit)

---

## 🚀 How We Published to PyPI

We followed this excellent guide for publishing directly from GitHub:

📝 [Publishing a Python Package to PyPI in 2024](https://medium.com/@blackary/publishing-a-python-package-from-github-to-pypi-in-2024-a6fb8635d45d)

---

## 📩 Contact

For access credentials or collaboration inquiries, please contact the Qmed Asia team.

---

## 🏥 About Qmed Asia

Qmed Asia is a health technology company focused on building digital tools for clinicians and pharmacists. Our goal is to make evidence-based medicine more accessible and actionable through intelligent clinical infrastructure.

---

## 🏷️ Tags

`clinical-guidelines` • `malaysia` • `medical-ai` • `nlp` • `mcp` • `python` • `healthtech`
