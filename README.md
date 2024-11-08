# Custom Scraping Script using ScrapeGraphAI

A customizable shell script that integrates **Ollama** and **ScrapeGraphAI** for automated web scraping. It accepts a website URL and a prompt to quickly gather relevant information.

## Installation

### Prerequisites

- **Python 3.11** or later

### Step 1: Set Up the Virtual Environment

1. Open a terminal window in your project directory.
2. Create a virtual environment named `scrapeai` with Python's `venv`:

   ```bash
   python3 -m venv scrapeai
   ```

3. Activate the environment:

   ```bash
   source scrapeai/bin/activate  # On macOS/Linux
   scrapeai\Scripts\activate     # On Windows
   ```

### Step 2: Install ScrapeGraphAI

With the virtual environment active, install ScrapeGraphAI via `pip`:

```bash
pip install scrapegraphai --upgrade
```

### Step 3: Install Chromium Driver

Chromium is required for web automation tasks. Install it with:

```bash
sudo apt install chromium-chromedriver  # For Ubuntu/Linux
```

### Step 4: Install Required Python Packages

1. Install `nest_asyncio`, a utility that allows running nested asyncio tasks, which can be useful for complex web scraping workflows:

   ```bash
   pip install nest_asyncio
   ```

2. Install `playwright`, a cross-browser automation library, and its dependencies:

   ```bash
   pip install playwright
   playwright install-deps  # For Linux
   playwright install
   ```

### Step 5: Set Up and Configure Ollama (for LLM Integration)

Ollama provides support for running language models locally. Install and configure it by following these steps:

1. [Download Ollama](https://ollama.com/download) and install it for your OS.
2. After installation, run the following commands to set up models required by ScrapeGraphAI:

   ```bash
   ollama run mistral
   ollama run nomic-embed-text
   ```

3. Verify the models are installed:

   ```bash
   ollama list
   ```

### Step 6: Configure Environment Variables

1. Create a `.env` file in your project directory to specify the base URL for Ollama.

   ```plaintext
   OLLAMA_URL=http://localhost:11434
   ```

2. Ensure this `.env` file is in the same directory as your Python script.

### Step 7: Test the Installation

To confirm the setup is correct, run a test using the script.

## Usage

Run the script with the following command, replacing `<prompt>` and `<source>` with your desired input:

```bash
python script.py "<prompt>" "<source>"
```

### Example

To gather information about a company from a website, use:

```bash
python script.py "Find some information about what the company does, its name, and a contact email." "https://example.com"
```

### Command-Line Arguments

The script accepts two command-line arguments:

1. **`<prompt>`**: The prompt specifying the type of information to retrieve.
2. **`<source>`**: The URL of the website to scrape.
