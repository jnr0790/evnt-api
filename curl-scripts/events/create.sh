curl "http://localhost:8000/events/" \
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
