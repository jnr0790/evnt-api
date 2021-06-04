# EVNT
An application where you can post an event you plan on going to (i.e concert, sporting event, cookout) on a map. When an event is created the location will be pinned on a map which you can click to view the information, delete, or update the event.

## Links
- [EVNT API](https://evnt-api.herokuapp.com/)
- [EVNT Client](https://jnr0790.github.io/evnt-client/)
- [EVNT Client Repository](https://github.com/jnr0790/evnt-client)


## User Stories
- As a user I want to sign in/up
- As a user I want to change my password
- As a user I want to sign out
- As a user I want to add a new event
- As a user I want to see multiple events I own
- As a user I want to see a single event I own
- As a user I want to edit a event I own
- As a user I want to remove a event I own

## Planning Story
I plan to work on a specific functionality at a time beginning with the backend API. Problem solving issues will be solved with research or reaching out through the issues thread.

## Technologies Used
- PostgreSQL
- Django
- Python
- JavaScript
- HTML/CSS

## Unsolved Problems
Getting the Django API to communicate with Mapbox API.

## Wireframe
#### V1
![EVNT V1](https://i.imgur.com/mCWqjIp.png)

#### V2
![EVNT V2](https://i.imgur.com/DMl7L3C.png)

## ERD
![EVNT ERD](https://i.imgur.com/y4IQCu6.png)

## Instructions

## Routes
### Authentication

| Verb   | URI Pattern            | Controller#Action |
|--------|------------------------|-------------------|
| POST   | `/sign-up`             | `users#signup`    |
| POST   | `/sign-in`             | `users#signin`    |
| PATCH  | `/change-password/`    | `users#changepw`  |
| DELETE | `/sign-out/`           | `users#signout`   |

#### POST /sign-up

Request:

```sh
curl "https://evnt-api.herokuapp.com/sign-up/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
    "credentials": {
      "email": "'"${EMAIL}"'",
      "password": "'"${PASSWORD}"'",
      "password_confirmation": "'"${PASSWORD}"'"
    }
  }'

echo
```

```sh
curl-scripts/sign-up.sh
```

Response:

```md
HTTP/1.1 201 Created
Content-Type: application/json; charset=utf-8

{
  "user": {
    "id": 1,
    "email": "an@example.email"
  }
}
```

#### POST /sign-in

Request:

```sh
curl "http://localhost:8000/sign-in/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
    "credentials": {
      "email": "'"${EMAIL}"'",
      "password": "'"${PASSWORD}"'"
    }
  }'

echo
```

```sh
curl-scripts/sign-in.sh
```

Response:

```md
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
  "user": {
    "id": 1,
    "email": "an@example.email",
    "token": "33ad6372f795694b333ec5f329ebeaaa"
  }
}
```

#### PATCH /change-password/

Request:

```sh
curl "http://localhost:8000/change-pw/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "passwords": {
      "old": "'"${OLDPW}"'",
      "new": "'"${NEWPW}"'"
    }
  }'

echo
```

```sh
TOKEN=33ad6372f795694b333ec5f329ebeaaa curl-scripts/change-password.sh
```

Response:

```md
HTTP/1.1 204 No Content
```

#### DELETE /sign-out/

Request:

```sh
curl "http://localhost:8000/sign-out/" \
  --include \
  --request DELETE \
  --header "X-CSRFToken: ${CSRF}" \
  --header "Authorization: Token ${TOKEN}" \

echo
```

```sh
TOKEN=33ad6372f795694b333ec5f329ebeaaa curl-scripts/sign-out.sh
```

Response:

```md
HTTP/1.1 204 No Content
```

### Posts

| Verb   | URI Pattern          | Controller#Action              |
|--------|----------------------|--------------------------------|
| POST   | `/posts`             | `users#Create Post`            |
| GET    | `/posts`             | `users#View All Posts`         |
| GET    | `/users/:userId`     | `users#View Posts By One User` |
| GET    | `/posts/:postId`     | `users#View One Post`          |
| PATCH  | `/posts/:id`         | `users#Update Post`            |
| DELETE | `/posts/:id`         | `users#Destroy Post`           |

#### POST /posts

Request:

```sh
curl "https://evnt-api.herokuapp.com" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer $TOKEN" \
  --data '{
    "post": {
      "text": "Text Of The Post"
    }
  }'
```

```sh
TOKEN=33ad6372f795694b333ec5f329ebeaaa curl-scripts/posts/create.sh
```

Response:

```md
TP/1.1 201 Created
Content-Type: application/json; charset=utf-8

{"post":
  {
    "_id":"60988d0f7e39ba00153ea5d6",
    "text":"Text Of The Post",
    "owner":"60988ca97e39ba00153ea5d5",
    "ownerEmail":"an@example.email",
    "comments":[],
    "createdAt":"2021-05-10T01:31:59.280Z",
    "updatedAt":"2021-05-10T01:31:59.280Z",
    "__v":0
  }
}
```

#### GET /posts

Request:

```sh
curl "https://evnt-api.herokuapp.com" \
  --include \
  --request GET
  --header "Authorization: Bearer $TOKEN"
```

```sh
TOKEN=33ad6372f795694b333ec5f329ebeaaa curl-scripts/posts/index.sh
```

Response:

```md
TP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{"posts":
  [
    {
      "_id":"609bdcd2c23acd1c3c28ac8c",
      "text":"r",
      "owner":"60997e719523eb36eca8bce9",
      "ownerEmail":"cat@dog",
      "comments":[],
      "createdAt":"2021-05-12T13:49:06.426Z",
      "updatedAt":"2021-05-12T13:49:06.426Z",
      "__v":0
    },
    {
      "_id":"609bdcd8c23acd1c3c28ac8d",
      "text":"t",
      "owner":"60997e719523eb36eca7c9b1",
      "ownerEmail":"user@email",
      "comments":[],
      "createdAt":"2021-05-12T13:49:12.278Z",
      "updatedAt":"2021-05-12T13:49:12.278Z",
      "__v":0
    }
  ]
}
```

#### GET /users/:userId

Request:

```sh
curl "https://evnt-api.herokuapp.com/users/$USER_ID" \
  --include \
  --request GET
  --header "Authorization: Bearer $TOKEN"
```

```sh
TOKEN=33ad6372f795694b333ec5f329ebeaaa USER_ID=609be624c23acd1c3c28ac8f curl-scripts/users/show.sh
```

Response:

```md
TP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{"posts":
  {
    [
      {
        "_id":"609be62bc23acd1c3c28ac90",
        "text":"hi",
        "owner":"609be624c23acd1c3c28ac8f",
        "ownerEmail":"blue@green",
        "comments":[],
        "createdAt":"2021-05-12T14:28:59.115Z",
        "updatedAt":"2021-05-12T14:28:59.115Z",
        "__v":0
      },
      {
        "_id":"609be62ec23acd1c3c28ac91",
        "text":"hello",
        "owner":"609be624c23acd1c3c28ac8f",
        "ownerEmail":"blue@green",
        "comments":[],
        "createdAt":"2021-05-12T14:29:02.857Z",
        "updatedAt":"2021-05-12T14:29:02.857Z",
        "__v":0
      }
    ]
  }
}
```

#### GET /posts/:postId

Request:

```sh
curl "https://evnt-api.herokuapp.com/$POST_ID" \
  --include \
  --request GET
  --header "Authorization: Bearer $TOKEN"
```

```sh
TOKEN=33ad6372f795694b333ec5f329ebeaaa POST_ID=609be62ec23acd1c3c28ac91 curl-scripts/posts/show.sh
```

Response:

```md
TP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
  "post":{
    "_id":"609be62ec23acd1c3c28ac91",
    "text":"hello",
    "owner":"609be624c23acd1c3c28ac8f",
    "ownerEmail":"blue@green",
    "comments":[],
    "createdAt":"2021-05-12T14:29:02.857Z",
    "updatedAt":"2021-05-12T14:29:02.857Z",
    "__v":0
  }
}
```

#### PATCH /posts/:postId

Request:

```sh
curl "https://evnt-api.herokuapp.com/$POST_ID" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer $TOKEN" \
  --data '{
      "post": {
        "text": "New Text"
      }
    }'
```

```sh
TOKEN=33ad6372f795694b333ec5f329ebeaaa POST_ID=609be62ec23acd1c3c28ac91 curl-scripts/posts/update.sh
```

Response:

```md
TP/1.1 204 No Content
```

#### DELETE /posts/:id

Request:

```sh
curl "https://evnt-api.herokuapp.com/$POST_ID" \
  --include \
  --request DELETE
  --header "Authorization: Bearer $TOKEN"
```

```sh
TOKEN=33ad6372f795694b333ec5f329ebeaaa POST_ID=609be62ec23acd1c3c28ac91 curl-scripts/posts/destroy.sh
```

Response:

```md
TP/1.1 204 No Content
```

## [License](LICENSE)

1. All content is licensed under a CC­BY­NC­SA 4.0 license.
1. All software code is licensed under GNU GPLv3. For commercial use or
    alternative licensing, please contact legal@ga.co.
