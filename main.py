from typing import Union, Optional
import datetime

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


from webspace import paths

app = FastAPI()

app.mount(
    "/" + paths.STATIC_ASSETS_DIR.__str__(), 
    StaticFiles(directory=paths.STATIC_ASSETS_DIR), 
    name="static"
)
templates = Jinja2Templates(directory=paths.TEMPLATES_DIR)

@app.get("/api")
async def api():
    return {"API VERSION": "0.1.1"}


@app.get("/api/user")
async def get_api_user_info(name: str, q: Union[str, None] = None):
    return {"user": f"Hi {name.title()}", "q": q}



@app.get("/", response_class=HTMLResponse)
async def render_ui(request: Request, id: Optional[str]= None):
    if id:
        return templates.TemplateResponse(
            request=request, name="linked_page.html", context={"id": id}
        )
    return templates.TemplateResponse(
        request=request, name="index.html", context={"id": id}
    )
    
@app.get("/current_time")
async def get_current_time(request: Request):
    return {"Date & Time": f"{datetime.datetime.now().strftime('%Y %B %d, %H:%M:%S')}"}
    
# http://127.0.0.1:8000/api/user?name=santo

# from typing import Union

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


