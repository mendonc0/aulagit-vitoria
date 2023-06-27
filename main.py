from fastapi import FastAPI
from pydantic import BaseModel

books = []

class Book(BaseModel):
    ano: str
    titulo: str


app = FastAPI()

@app.get("/")
def root():
    if books == []:
        return {"message": "Nenhum livro encontrado"}
    else:
        return books
    
@app.post("/new")
async def creat_book(book: Book):
    books.append(book)
    return book    

@app.delete("/")
def delete_book(params: Title):
   for book in books:
      if book.titulo == params.titulo:
         index = books.index(book)
         books.pop(index)