import uvicorn
from os import getenv

if __name__ == "__main__":
	port = int(getenv("PORT", 8000))
	uvicorn.run("app.api:app", host="10.168.1.95", port=port, reload=False)
