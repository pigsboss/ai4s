#!/usr/bin/env python3
import ollama
response = ollama.chat(
    model="deepseek-r1:70b",
    messages=[
        {"role": "user", "content": "Explain Newton's second law of motion"},
    ],
)
print(response["message"]["content"])
