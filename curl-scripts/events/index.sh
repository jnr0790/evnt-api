curl "http://localhost:8000/events/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
