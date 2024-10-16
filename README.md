# langchain-learning

## Description of each folders
This repository contains some simple codes to implement RAG using different LLMS
1. **Example 1** - here both the python files demonstrates the use of local and public APIs
    * **Ollama-app.py** : using locally hosted models
    * **Openai-app.py** : using openai api keys
2. **Example 2** - Demonstrates to use APIs of an LLM [uses both Openai and Ollama]
    * **app.py** : uses fastapi to host the LLM application
    * **client.py** : consumes the APIs of app.py and provides the results based on that
3. **Example 3** - Creating a vectorstore
    * **simplerag.ipynb** - shows the creation of vector store documents and loading files in langchain
4. **Example 4** - A very simple example of a complete RAG
    * **retriever.ipynb** : this file contains the implementation
5. **Example 5** - This example shows how we can create an agent using Groq inference and tools like wiki, arxiv and a custom documentation RAG
    * **agents.ipynb** : this file contains the example and implementation
6. **Example 6** - This example demonstrates the Groq api usage
    * **groq_test.py** : This has a streamlit interface to perform your test
7. **Example 7** - [In Progress] This example will demonstrate the use of RAG using huggingface library
    * **huggingface.ipynb** : The implementation of rag with huggingface is still in progress as there are certain changes in the langchain and I need to read those before completing the implementation. 

# How to run the codes. 
1. For python use 
`python <file_name>.py`
2. For Streamlit with python use
`streamlit run <file_name>.py`

# Installiation of Libraries 
* Use the below given command[this has all the versions which are required to work without any library related issues]
`pip install -r requirements.txt`
* Use the below given command[use the latest libraries]
`pip install -r requirements_latest.txt`

# Useful links 
1. https://ollama.com/
2. https://python.langchain.com/docs/concepts/#agents
3. https://python.langchain.com/docs/how_to/#agents
4. https://python.langchain.com/docs/how_to/tools_builtin/
5. https://python.langchain.com/v0.1/docs/integrations/text_embedding/
6. https://python.langchain.com/v0.1/docs/integrations/llms/
7. https://python.langchain.com/v0.1/docs/integrations/chat/
8. https://smith.langchain.com/
9. https://platform.openai.com/account/api-keys
10. https://groq.com/


# Concept Learning Urls:
1. https://medium.com/@EjiroOnose/vector-database-what-is-it-and-why-you-should-know-it-ae7e7dca82a4
2. https://python.langchain.com/docs/tutorials/retrievers/
3. https://medium.com/decodingml/rag-fundamentals-first-c6f7acd4ed3b
4. https://www.ibm.com/topics/large-language-models

# reach out to me on 
* linkedIn -  https://www.linkedin.com/in/nikhilsharmabph/
* Linktr.ee - https://linktr.ee/Nikhil_JavaDev
* My Portfolio - https://www.datascienceportfol.io/nikhilsharma
* Github - https://github.com/Nikhil8bph