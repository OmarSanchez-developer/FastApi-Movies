from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()
app.title = "Mi aplicación con FastApi"
app.version = "0.0.1"

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=4, max_length=50)
    year: int = Field(le=2022)
    rating: float
    category: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi pelicula",
                "overview": "Descripción de la pelicula",
                "year": 2022,
                "rating": 9.8,
                "category": "Acción"
            }
        }

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un momento planeta llamado Pandora viven los Nav",
        "year": "2009",
        "rating": 7.8,
        "category": "Accion"
    },
     {
        "id": 2,
        "title": "Avatar",
        "overview": "En un momento planeta llamado Pandora viven los Nav",
        "year": "2009",
        "rating": 7.8,
        "category": "Accion"
    }
]

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')

@app.get('/movies', tags=['movies'])
def get_movies():
    return movies

@app.get('/movies/{id}')
def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return []

@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str, year: int):
    return [item for item in movies if item['category'] == category]

@app.post('/movies', tags=['movies'])
def create_movie(movie: Movie):
    movies.append(movie)
    return movies

@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie):
     for item in movies:
       if item["id"] == id:
            item['title'] = movie.title,
            item['overview'] = movie.overview,
            item['year'] = movie.year,
            item['raiting'] = movie.aiting,
            item['category'] = movie.category
            return movies
       
@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for item in movies:
         if item["id"] == id:
            movies.remove(item)
            return movies
       


     