# Full-Stack Application with FastAPI and Vite-React

## Project Overview

This project is a full-stack application that combines FastAPI for the backend and a Vite-powered React 18 app using Tailwind CSS for the frontend. The project architecture allows seamless integration between the client and server sides, leveraging modern web technologies for efficient development and scalable deployment.

### Technologies Used

- **Frontend**: Vite, React 18, Tailwind CSS
- **Backend**: FastAPI
- **Database**: MongoDB (configured with Motor)
- **Authentication**: JWT

## Setup Instructions

### Prerequisites

- [Node.js](https://nodejs.org/) and [npm](https://www.npmjs.com/get-npm)
- [Python 3.8+](https://www.python.org/downloads/)
- [MongoDB](https://www.mongodb.com/try/download/community) (running instance or connection)

### Backend Setup (FastAPI)

1. **Navigate to the Backend Folder**

   ```bash
   cd backend
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI Server**

   ```bash
   python -m app.main
   ```

   Your FastAPI backend should be running at `http://localhost:8000`.

### Frontend Setup (Vite + React 18 + Tailwind CSS)

1. **Navigate to the Frontend Folder**

   ```bash
   cd frontend
   ```

2. **Install Dependencies**

   ```bash
   npm install
   ```

3. **Run the Frontend Development Server**

   ```bash
   npm run dev
   ```

   Your React application should be accessible at `http://localhost:3000` (or another port if 3000 is in use).

### Environment Variables

Make sure to set any required environment variables for both the frontend and backend. Common configurations include database connection strings and API URLs.

#### Example `.env` Files

- **Backend**: Create a `.env` file in the `backend` directory for environment-specific variables, such as:

  ```plaintext
  DATABASE_URL=mongodb://localhost:27017
  DATABASE_NAME=<your_db>
  JWT_SECRET_KEY=<your_secret_key_here>
  JWT_ALGORITHM=HS256
  ACCESS_TOKEN_EXPIRE_MINUTES=30
  ```

- **Frontend**: Create a `.env` file in the `frontend` directory for environment-specific variables, such as:

  ```plaintext
  VITE_API_URL=http://localhost:8000/api
  ```

## Usage

- Access the frontend client via a web browser at the served address.
- The client interacts with the backend for features like user authentication and data management.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the project.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.
