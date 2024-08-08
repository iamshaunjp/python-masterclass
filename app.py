from bottle import run, route, response, template, static_file, request

# data
ninjas = [
  {
    "name": "Yoshi",
    "belt_color": "Black",
    "special_move": "Shadow Strike"
  },
  {
    "name": "Hattori",
    "belt_color": "Green",
    "special_move": "Tornado Blast"
  },
  {
    "name": "Momochi",
    "belt_color": "Blue",
    "special_move": "Rain Leap"
  }
]

@route("/public/<filename:path>")
def send_static(filename):
  return static_file(filename, root="./static")

@route("/")
def home():
  return template('home', ninjas=ninjas)

# api endpoints
@route("/api/ninjas")
def get_ninjas():
  response.content_type = "application/json"
  return {"data": ninjas}

@route("/api/ninjas", method="POST")
def add_ninja():
  new_ninja = request.json

  if isinstance(new_ninja, dict):
    ninjas.append(new_ninja)

  response.content_type = "application/json"
  return {"message": "Added a new ninja", "data": new_ninja}

if __name__ == '__main__':
  # use the run function to run the app
  run(host="localhost", port=8080, debug=True, reloader=True)