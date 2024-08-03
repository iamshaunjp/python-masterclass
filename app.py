# static methods

class User:
  def __init__(self, username, email):
    self.username = username
    self.email = email

  def post_status(self, status):
    print(f"{self.username} posted: {status}")

  @staticmethod
  def validate_email(email):
    return "@" in email and len(email) > 3
  
class SuperUser(User):
  def __init__(self, username, email, avatar):
    super().__init__(username, email)
    self.avatar = avatar

  # superuser-only method
  def post_announcement(self, message):
    print(f"Site announcement from {self.username}: {message}")

def main():
  user_one = User("leo", "leo@netninja.dev")
  user_two = User("raph", "raph@netninja.dev")
  super_user = SuperUser("splinter", "splinter@netninja.dev", "splinter.jpg")

  super_user.post_announcement("New site design coming soon!")

if __name__ == "__main__":
    main()
