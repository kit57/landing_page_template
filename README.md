# landing_page_template
GenAI powered app that will create a landing page for the user with with a given prompt. 

It runs on streamlit framework and uses OpenAI gpt-4o LLM. 

## How it works

To run the app, first you must install the dependencies by running:

```pip install poetry```

and then run:

```poetry install```

This will install the dependencies specified in the pyproject.toml in your virtual environment.

You then need to set the OPENAI_API_KEY. It's mandatory for the app to work properly. If you don't know where to get this api key, please follow this [link](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key). Once you have it, <b>write the api key in the .env file.</b>

Now you're good to start streamlit and start generating landing pages with OpenAI. Write on the command prompt the following line:

```streamlit run main.py```


# LangFuse visualization

You can login in [Cloud Langfuse](https://cloud.langfuse.com/) to check the traces of the application. It can show you how many tokens you have used, the total cost and the latency.
