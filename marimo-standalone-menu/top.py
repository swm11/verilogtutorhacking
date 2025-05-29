from fastapi import FastAPI
import marimo
import sys
sys.path.append("./")

server = (
    marimo.create_asgi_app()
    .with_app(path="", root="./counter.py")
    .with_app(path="/counter", root="./counter.py")
    .with_app(path="/tlights", root="./tlights.py")
)

# Create a FastAPI app
app = FastAPI()

#app.add_middleware(auth_middleware)
#app.add_route("/login", my_login_route, methods=["POST"])

app.mount("/", server.build())

# Run the server
if __name__ == "__main__":
    import uvicorn

#    uvicorn.run(app, host="svr-www-ecad.cl.cam.ac.uk", port=8000)
    uvicorn.run(app, host="localhost", port=80)

