# 🚀 Dualify API

Welcome to **Dualify API** – a small API build to retrieve your grades from dualis, built with **FastAPI**!  

---
## ⚙️ **Setup Instructions**

### 🐳 Docker Prerequisites  

Before running this project with Docker, make sure you have **Docker installed** on your system.  

#### ✅ **Check if Docker is Installed**  
Run the following command in your terminal:  
```sh
docker --version
```

If you see a version like `Docker version 24.x.x`, Docker is installed! 🎉  
If not, follow the installation steps below.  

---

### 🔹 **Install Docker**  

#### **Mac & Windows**  
1. Download and install **Docker Desktop**:  
   👉 [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)  
2. Follow the setup instructions and start **Docker Desktop**.  
3. Verify installation:  
```sh
docker run hello-world
```

#### **Linux**  
Run the following commands in your terminal:  
```bash (ubuntu)
# Update package list
sudo apt update  

# Install Docker  
sudo apt install docker.io -y  

# Start & enable Docker service  
sudo systemctl start docker  
sudo systemctl enable docker  

# Verify installation  
docker --version  
```

### 🔹 **1. Clone the Repository**
```sh
git clone git@github.com:03kaan07/dualify_fastapi.git
cd dualify_fastapi
```
### 🔹 **2. Create Image and build Container**
Now ensure your docker-daemon is running and run this command in your terminal:
```sh
# Build the Docker image
docker build -t fastapi-backend .
```
```sh
# Run the container in detached mode (-d) and expose port 8000
docker run -d -p 8000:8000 --name fastapi-container fastapi-backend
```
### 🚀 Running the API

Once everything is set up, start or stop the FastAPI server by running:

```sh
# Start the container
docker start fastapi-container
```
```sh
# Stop the container
docker stop fastapi-container
```
Your API should now be running! 🎉  

By default, FastAPI provides an interactive API documentation at:  
🔗 **Swagger UI** → [http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs)  
🔗 **ReDoc** → [http://0.0.0.0:8000/redoc](http://0.0.0.0:8000/redoc)  

### 🛠 **Testing the API**  

Once your container is running, you can test the API directly from your terminal using `curl`.  

### 🔹 **Linux/macOS**  
Run the following command in your terminal:  

```sh
curl -X 'POST' \
  'http://0.0.0.0:8000/grades' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "mustermann@student.dhbw-mannheim.de",
  "password": "password"
}'
```

### 🔹 **Windows (PowerShell)**  
For Windows, use the equivalent `Invoke-RestMethod` command:  

```powershell
Invoke-RestMethod -Uri "http://0.0.0.0:8000/grades" -Method Post -Headers @{ "accept"="application/json"; "Content-Type"="application/json" } -Body '{ "username": "mustermann@student.dhbw-mannheim.de", "password": "password" }'
```

---

## ⚙️ **(MacOS for now)Setup Instructions (only needed for further development)**

- **Python** (3.x recommended)

### 🔹 **Check if Python is Installed**
Run the following command in your terminal:
```sh
python3 --version
```

### 🔹 **1. Clone the Repository**
```sh
git clone git@github.com:03kaan07/dualify_fastapi.git
cd dualify_fastapi
```
### 🔹 **2. Create a Virtual Environment**
It’s recommended to use a virtual environment in the projects root directory to manage dependencies.

#### **On macOS/Linux:**
```sh
python3 -m venv .venv
source .venv/bin/activate
```
#### **On Windows(PowerShell):**
```sh
python3 -m venv .venv
.venv\Scripts\activate
```
### 🔹 **3. Install Dependencies**
Once inside the virtual environment, install all required packages by running:

```sh
pip install -r requirements.txt
```
### 🚀 Running the API (locally for development)

Once everything is set up, start the FastAPI development server by running:

```sh
fastapi dev app/main.py
```
Your API should now be running! 🎉  

By default, FastAPI provides an interactive API documentation at:  
🔗 **Swagger UI** → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
🔗 **ReDoc** → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  

### 🛠 **Testing the API**  

Once your container is running, you can test the API directly from your terminal using `curl`.  

### 🔹 **Linux/macOS**  
Run the following command in your terminal:  

```sh
curl -X 'POST' \
  'http://127.0.0.1:8000/grades' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "mustermann@student.dhbw-mannheim.de",
  "password": "password"
}'
```

### 🔹 **Windows (PowerShell)**  
For Windows, use the equivalent `Invoke-RestMethod` command:  

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/grades" -Method Post -Headers @{ "accept"="application/json"; "Content-Type"="application/json" } -Body '{ "username": "mustermann@student.dhbw-mannheim.de", "password": "password" }'
```