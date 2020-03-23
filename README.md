You can do it with :
```
curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d "domain=google.com" http://localhost:8000/speed.json
```
and you obtain :
*{"domain": "google.com", "time": 94.423, "status": 200, "error": ""}*

but you can do it more 'html' in your browser0
```http://localhost:8000/```
or
```http://localhost:8000/speed.html```

(see the screnshot)

