status = 400

match status:
  case 200:
    print("OK")
  case 404:
    print("Not found")
  case 500 | 501:
    print("Server error")
  case _:
     print("Unknown status")

  