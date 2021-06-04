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
- To make requests to the API go to the [EVNT](https://jnr0790.github.io/evnt-client/) website
- Sign Up for an account to make the `POST` call to `/sign-up/`.
- Sign In using your existing account to make the `POST` call to `/sign-in/`.
- Click the New Event option on the menu to create and event to make the `POST` call to `/events/`.
- Click the View Events to see all events you've created to make the `GET` call to `/events/`.
- On the events click the View button to view a single event to make the `GET` call to `/events/id/`.
- In single event view you can click delete to remove the event from your list of events to make the `DELETE` call to `/events/id/`.
- Also, in single event view you can click update to update the event using the ID which is seen in the single event view to make the `PATCH` call to `/events/id/`.
- To change password you click the Change Password option on the menu to make the `PATCH` call to `/change-pw/`.
- To sign out simply click the Sign Out option on the menu to make the `DELETE` call to `/sign-out/`.

## Routes
### Authentication

| Verb   | URI Pattern            | Controller#Action |
|--------|------------------------|-------------------|
| POST   | `/sign-up/`            | `users#signup`    |
| POST   | `/sign-in/`            | `users#signin`    |
| PATCH  | `/change-pw/`          | `users#changepw`  |
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
EMAIL=example@q.com PASSWORD=example sh curl-scripts/auth/sign-up.sh
```

Response:

```md
HTTP/1.1 201 Created

{"user":
  {"id":6,
  "email":"example@q.com"
  }
}
```

#### POST /sign-in

Request:

```sh
curl "https://evnt-api.herokuapp.com/sign-in/" \
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
EMAIL=example@q.com PASSWORD=example sh curl-scripts/auth/sign-in.sh
```

Response:

```md
HTTP/1.1 200 OK

{"user":
  {"id":6,
  "email":"example@q.com",
  "token":"c0c983a1199c5c3cc4ed319da6e7c41609c7e6dc"
  }
}
```

#### PATCH /change-password/

Request:

```sh
curl "https://evnt-api.herokuapp.com/change-pw/" \
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
TOKEN=c0c983a1199c5c3cc4ed319da6e7c41609c7e6dc OLDPW=example NEWPW=newpw sh curl-scripts/auth/change-pw.sh
```

Response:

```md
HTTP/1.1 204 No Content
```

#### DELETE /sign-out/

Request:

```sh
curl "https://evnt-api.herokuapp.com/sign-out/" \
  --include \
  --request DELETE \
  --header "X-CSRFToken: ${CSRF}" \
  --header "Authorization: Token ${TOKEN}" \

echo
```

```sh
TOKEN=c0c983a1199c5c3cc4ed319da6e7c41609c7e6dc sh curl-scripts/auth/sign-out.sh
```

Response:

```md
HTTP/1.1 204 No Content
```

### Events

| Verb   | URI Pattern          | Controller#Action              |
|--------|----------------------|--------------------------------|
| POST   | `/events/`           | `users#Create Event`           |
| GET    | `/events/`           | `users#View All Events`        |
| GET    | `/events/id/`        | `users#View One Event`         |
| PATCH  | `/events/id/`        | `users#Update Event`           |
| DELETE | `/events/id/`        | `users#Destroy Event`          |

#### POST /events

Request:

```sh
curl "https://evnt-api.herokuapp.com/events/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "event": {
      "name": "'"${NAME}"'",
      "location": "'"${LOCATION}"'",
      "date": "'"${DATE}"'",
      "time": "'"${TIME}"'"
    }
  }'

echo
```

```sh
TOKEN=c0c983a1199c5c3cc4ed319da6e7c41609c7e6dc NAME="Event" LOCATION="Somewhere" DATE="9/5/2021" TIME="4pm" sh curl-scripts/events/create.sh
```

Response:

```md
HTTP/1.1 201 Created

{"event":
  {"id":12,
  "name":"Event",
  "location":"Somewhere",
  "date":"9/5/2021",
  "time":"4pm",
  "owner":6
  }
}
```

#### GET /events

Request:

```sh
curl "https://evnt-api.herokuapp.com/events/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
```

```sh
TOKEN=c0c983a1199c5c3cc4ed319da6e7c41609c7e6dc sh curl-scripts/events/index.sh
```

Response:

```md
HTTP/1.1 200 OK

{"events":
  [
    {"id":12,
    "name":"Event",
    "location":"Somewhere",
    "date":"9/5/2021",
    "time":"4pm",
    "owner":6
    },
    {"id":13,
    "name":"Event 2",
    "location":"Here",
    "date":"2/6/22",
    "time":"8pm",
    "owner":6
    }
  ]
}
```

#### GET /events/:eventId

Request:

```sh
curl "https://evnt-api.herokuapp.com/events/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
```

```sh
TOKEN=c0c983a1199c5c3cc4ed319da6e7c41609c7e6dc ID=13 sh curl-scripts/events/show.sh
```

Response:

```md
HTTP/1.1 200 OK

{"event":
  {"id":13,
  "name":"Event 2",
  "location":"Here",
  "date":"2/6/22",
  "time":"8pm",
  "owner":6
  }
}
```

#### PATCH /events/:eventId

Request:

```sh
curl "https://evnt-api.herokuapp.com/events/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "event": {
      "name": "'"${NAME}"'",
      "location": "'"${LOCATION}"'",
      "date": "'"${DATE}"'",
      "time": "'"${TIME}"'"
    }
  }'

echo
```

```sh
TOKEN=c0c983a1199c5c3cc4ed319da6e7c41609c7e6dc ID=13 NAME="Updated Event" LOCATION="Remote" DATE="10/12/21" TIME="9pm" sh curl-scripts/events/update.sh
```

Response:

```md
HTTP/1.1 204 No Content
```

#### DELETE /events/:id

Request:

```sh
curl "https://evnt-api.herokuapp.com/events/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
```

```sh
TOKEN=c0c983a1199c5c3cc4ed319da6e7c41609c7e6dc ID=13 sh curl-scripts/events/delete.sh
```

Response:

```md
HTTP/1.1 204 No Content
```
