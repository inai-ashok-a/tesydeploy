from fastapi import FastAPI
app = FastAPI()
print("Hii")



# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message": "Hello world!@!!! from new"}
