# LLM Comparison API

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/llm_comparison_api.git
    cd llm_comparison_api
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file and add your API key and Vercel Blob Storage URL:
    ```plaintext
    API_KEY=your_api_key
    VERCEL_BLOB_STORAGE_URL=your_blob_storage_url
    ANTHROPIC_API_KEY=test
    OPENAI_API_KEY=test
    ```

5. Run the application:
    ```bash
    uvicorn app.main:app --reload
    ```

## Deployment

1. Install the Vercel CLI:
    ```bash
     npm install -g vercel
    ```

2. Deploy the application:
    ```bash
    vercel
    ```

## Testing

1. Run the test suite:
    ```bash
    pytest
    ```
