<p align="center">
  <img src="https://app.autoblocks.ai/images/logo.png" width="300px">
</p>

<p align="center">
  <a href="https://docs.autoblocks.ai/">Documentation</a>
  |
  <a href="https://app.autoblocks.ai/">Application</a>
  |
  <a href="https://www.autoblocks.ai/">Home</a>
</p>

<p align="center">
  This repository contains examples of how to use Autoblocks with various frameworks, libraries, and languages.
</p>

## Getting started

- Sign up for an Autoblocks account at https://app.autoblocks.ai
- Grab your Autoblocks ingestion key from https://app.autoblocks.ai/settings/api-keys
- Grab your OpenAI API key from https://platform.openai.com/account/api-keys
- Create a `.env` file at the root of this repository with the following environment variables (**Tip**: Run `cp .env.example .env` for extra quick setup)

```
OPENAI_API_KEY=<your-api-key>
AUTOBLOCKS_INGESTION_KEY=<your-ingestion-key>
```

All examples will pull environment variables from this file!

## JavaScript

> **_NOTE:_** All JavaScript examples require `npm` and `node` >= 16 to be installed.

<!-- JavaScript start -->
| Name                                                     | Description                                                                                                            |
| -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| [chatbot-nextjs](/JavaScript/chatbot-nextjs)             | A Next.js app that uses openai and Autoblocks to power and monitor a chatbot                                           |
| [langchain](/JavaScript/langchain)                       | Automatic tracing of a LangChain pipeline                                                                              |
| [novel-ai-text-editor](/JavaScript/novel-ai-text-editor) | A Next.js app that uses [Novel](https://github.com/steven-tey/novel) and Autoblocks to power an AI-enabled text editor |
| [openai-automated](/JavaScript/openai-automated)         | Automatic tracing of openai calls                                                                                      |
| [openai-manual](/JavaScript/openai-manual)               | Manual tracing of openai calls                                                                                         |
<!-- JavaScript end -->

## Python

> **_NOTE:_** All Python examples require [`poetry`](https://python-poetry.org/docs/#installation) to be installed.

<!-- Python start -->
| Name                                   | Description                               |
| -------------------------------------- | ----------------------------------------- |
| [langchain](/Python/langchain)         | Automatic tracing of a LangChain pipeline |
| [openai-manual](/Python/openai-manual) | Manual tracing of openai calls            |
<!-- Python end -->
