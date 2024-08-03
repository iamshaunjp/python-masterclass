# classes

class User:
  # constructor
  def __init__(self, username, email):
    self.username = username
    self.email = email
  
  def post_status(self, status):
    print(f"{self.username} posted: {status}")

def main():
  user_one = User("leo", "leo@netninja.dev")
  user_two = User("raph", "raph@netninja.dev")

  # print("user 1:")
  # print(user_one.username, user_one.email)
  # print("user 2:")
  # print(user_two.username, user_two.email)

  # user_one.email = "leo4eva@netninja.dev"
  # print(user_one.email)

  user_one.post_status("Hello ninjas! This is Leo!")
  user_two.post_status("Raph here, ready to rumble!")

if __name__ == "__main__":
  main()