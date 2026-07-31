# Why We Use Virtual Environments

A virtual environment is like an isolated box for your Python project. 

We use it because different projects often need different versions of the same tool (like Django). If we install everything in one main place on our computer, the versions can conflict and break our projects. 

By using virtual environments, every project gets its own private space. This keeps things organized and prevents version conflicts.


# Setting up `uv` in Python

`uv` is a very fast tool to install and manage Python packages (it works like `pip`, but much faster).

### 1. Install uv
Open your terminal and run this command:
```bash
pip install uv
```

### 2. Create a virtual environment
Go into your project folder and run:
```bash
uv venv
```
This will create a new folder named `.venv` which holds your virtual environment.

### 3. Activate the virtual environment
You need to turn it on (activate it) before using it.
- **On Windows:**
```powershell
.venv\Scripts\activate
```
- **On Mac or Linux:**
```bash
source .venv/bin/activate
```

### 4. Install packages
Once the environment is active, you can install packages (like Django) very quickly:
```bash
uv pip install django
```
