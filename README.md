# Description
##### Yatube Api is project, which has systems of posts, comments and follows.
You can upload your photos from weekend or evening dinner with family and your frieds will see them and add some comments. Also they can reward your blog their follow.
# Install
##### You should follow this instructions to run Yatube on local server:
1. Clone yatube_api from my github (https://github.com/Starov-V/api_final_yatube) with command `git clone`
2. Install virtual environment (`$ python -m venv venv`)
3. Run virtual environment (`$ source venv/Scripts/activate`)
3. Install requirements (`$ pip install -r requirements.txt`)
4. Go to catalog with `manage.py`: `...api_final_yatube/yatube_api`
5. Run server (`$ python manage.py runserver`)
# Examples
`http://127.0.0.1:8000/api/v1/posts/:`
```
[
    {
        "id": 1,
        "author": "admin",
        "text": "first post",
        "pub_date": "2022-08-12T15:50:24.460002Z",
        "image": null,
        "group": null
    },
    {
        "id": 2,
        "author": "admin",
        "text": "second post",
        "pub_date": "2022-08-12T15:50:34.954593Z",
        "image": null,
        "group": null
    }
]
```
`http://127.0.0.1:8000/api/v1/posts/1/`
```
{
    "id": 1,
    "author": "admin",
    "text": "first post",
    "pub_date": "2022-08-12T15:50:24.460002Z",
    "image": null,
    "group": null
}
```
`http://127.0.0.1:8000/api/v1/posts/1/comments/`
POST method with body 
```
{
    "text": "first comment",
    "post": "1"
}
```
Result:
```
{
    "id": 1,
    "author": "admin1",
    "text": "first comment",
    "created": "2022-08-14T13:58:30.743060Z",
    "post": 1
}
```
`http://127.0.0.1:8000/api/v1/posts/1/comments/`
GET method
```
[
    {
        "id": 1,
        "author": "admin1",
        "text": "first comment",
        "created": "2022-08-14T13:58:30.743060Z",
        "post": 1
    }
]
```
# Technologies
- ##### Django _2.2.16_
- ##### pytest _6.2.4_
- ##### pytest-pythonpath _0.7.3_
- ##### pytest-django _4.4.0_
- ##### djangorestframewor _3.12.4_
- ##### djangorestframework-simplejwt _4.7.2_
- ##### Pillow _8.3.1_
- ##### PyJWT _2.1.0_
- ##### requests _2.26.0_
- ##### djoser _2.1.0_

### Some words from author
##### I'm beginner developer and it was my first api project. It was so hard and it failed without my training team in slack and my code reviewer, who gave me lots of useful tips for my code. In the end, I hope, that I can become professional developer and Yatube api is just the beginning.