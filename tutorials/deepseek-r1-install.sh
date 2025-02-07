#!/bin/bash
brew update
brew upgrade
brew install ollama
brew services restart ollama
sleep 3
ollama pull deepseek-r1:70b
pip install ollama langchain chromadb gradio langchain-community langchain-ollama pymupdf

