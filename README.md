# flask-mongo-app
A simple flask based python app, which takes names from a webpage and stores it in a mongodb database which is containarized.


# Flask & MongoDB Web Application with Docker

This is a simple web application built using Flask and MongoDB, fully containerized with Docker. It allows users to submit names through a web form and stores them in a MongoDB database. Another page displays the stored names.

## Features
- Web form to enter names
- Stores names in a MongoDB database
- Displays stored names on another page
- Fully containerized using Docker and Docker Compose

---

## Project Structure
```
flask-mongo-docker/
│── app.py                   # Flask web application
│── templates/               # HTML files for frontend
│   ├── index.html           # Form to enter names
│   ├── names.html           # Page to display names
│── requirements.txt         # Python dependencies
│── Dockerfile               # Instructions to containerize Flask app
│── docker-compose.yml       # Defines multiple containers
│── .gitignore               # Files to ignore in Git
│── README.md                # Project documentation
```

---

## Setup Instructions

### 1. **Prerequisites**
Ensure you have the following installed on your system:
- [Python 3](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### 2. **Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/flask-mongo-docker.git
cd flask-mongo-docker
```

### 3. **Build and Run with Docker Compose**
Run the following command to build and start the application:
```bash
docker-compose up --build
```
This will:
- Build the Flask app and MongoDB containers
- Start the services

### 4. **Access the Application**
- Open **`http://localhost:5000/`** → To enter names
- Open **`http://localhost:5000/names`** → To see stored names

### 5. **Stopping the Containers**
Press `CTRL+C` or run:
```bash
docker-compose down
```

---

## Detailed Explanation

### **Flask Application (`app.py`)**
- A simple web server using `Flask`.
- Connects to **MongoDB** (running in another container).
- Routes:
  - `"/"` → Displays a form for entering names.
  - `"/names"` → Fetches and displays stored names.

### **MongoDB Container (`docker-compose.yml`)**
- Runs a MongoDB service inside a container.
- Uses a persistent volume `mongo_data` to store data.

### **Dockerfile**
```Dockerfile
# Use an official Python image as base
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy everything from local project directory to the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
```
- Uses `python:3.9` as the base image.
- Copies project files into the container.
- Installs dependencies (`Flask`, `pymongo`).
- Exposes port 5000.
- Runs `app.py` when the container starts.

### **Docker Compose (`docker-compose.yml`)**
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - mongo
    environment:
      - MONGO_HOST=mongo
      - MONGO_PORT=27017

  mongo:
    image: mongo:latest
    container_name: mongo_db
    ports:
      - "27017:27017"
    volumes:
      - mongo_data:/data/db

volumes:
  mongo_data:
```
- Defines **two services**:
  1. **`web`** → The Flask application.
  2. **`mongo`** → A MongoDB database container.
- `ports: - "5000:5000"` → Maps container’s port 5000 to local machine’s port 5000.
- `depends_on: - mongo` → Ensures MongoDB starts before the Flask app.
- `volumes:` → Creates a persistent volume `mongo_data` to store MongoDB data.