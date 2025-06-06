# Copyright 2023 The Qwen team, Alibaba Group. All rights reserved.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re

from setuptools import find_packages, setup


def get_version() -> str:
    with open('qwen_agent/__init__.py', encoding='utf-8') as f:
        version = re.search(
            r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
            f.read(),
            re.MULTILINE,
        ).group(1)
    return version


def read_description() -> str:
    with open('README.md', 'r', encoding='UTF-8') as f:
        long_description = f.read()
    return long_description


# To update the package at PyPI:
# ```bash
# python setup.py sdist bdist_wheel
# twine upload dist/*
# ```
setup(
    name='qwen-agent',
    version=get_version(),
    author='Qwen Team',
    author_email='tujianhong.tjh@alibaba-inc.com',
    description='Qwen-Agent: Enhancing LLMs with Agent Workflows, RAG, Function Calling, and Code Interpreter.',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    keywords=['LLM', 'Agent', 'Function Calling', 'RAG', 'Code Interpreter'],
    packages=find_packages(exclude=['examples', 'examples.*', 'qwen_server', 'qwen_server.*']),
    package_data={
        'qwen_agent': [
            'utils/qwen.tiktoken', 'tools/resource/*.ttf', 'tools/resource/*.py', 'gui/assets/*.css',
            'gui/assets/*.jpeg'
        ],
    },

    # Minimal dependencies for Function Calling:
    install_requires=[
        'dashscope>=1.11.0',
        'eval_type_backport',
        'json5',
        'jsonlines',
        'jsonschema',
        'openai',
        'pydantic>=2.3.0',
        'requests',
        'tiktoken',
    ],
    extras_require={
        # Extra dependencies for RAG:
        'rag': [
            'charset-normalizer',
            'rank_bm25',
            'jieba',
            'snowballstemmer',
            'beautifulsoup4',
            'pdfminer.six',
            'pdfplumber',
            'python-docx',
            'python-pptx',
            'pandas',
            'tabulate',
        ],

        # Extra dependencies for MCP:
        'mcp': ['mcp'],

        # Extra dependencies for Python Executor, which is primarily for solving math problems:
        'python_executor': [
            'pebble',
            'multiprocess',
            'timeout_decorator',
            'python-dateutil',
            'sympy',
            'numpy',
            'scipy',
        ],

        # Extra dependencies for Code Interpreter:
        'code_interpreter': [
            'anyio>=3.7.1',
            'fastapi>=0.103.1',
            'jupyter>=1.0.0',
            'matplotlib',
            'numpy',
            'pandas',
            'pillow',
            'seaborn',
            'sympy',
            'uvicorn>=0.23.2',
        ],

        # Extra dependencies for Gradio-based GUI:
        'gui': [
            # Gradio has bad version compatibility. Therefore, we use `==` instead of `>=`.
            'pydantic==2.9.2',
            'pydantic-core==2.23.4',
            'gradio==5.23.1',
            'gradio-client==1.8.0',
            'modelscope_studio==1.1.7',
        ],
    },
    url='https://github.com/QwenLM/Qwen-Agent',
)
