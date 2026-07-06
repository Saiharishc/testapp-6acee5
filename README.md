# TestApp

This is a simple application with a FastAPI backend and a React frontend.

## Backend

- Technology: FastAPI
- Endpoints:
    - GET /: Health check endpoint.
    - GET /test: A simple test endpoint returning a message.

## Frontend

- Technology: React

## Setup and Running

### Backend

1. Navigate to the backend directory (usually the root of the project).
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```
3. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend

1. Navigate to the frontend directory (e.g., `testapp-frontend`).
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the React development server:
   ```bash
   npm start
   ```
   This will typically open the app in your browser at `http://localhost:3000`.
