file_name = input("Insert file name: ").lower().strip()

(".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip")

if file_name.endswith(".gif"):
    print(f"image/gif")
elif file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
    print(f"image/jpeg")
elif file_name.endswith(".png"):
    print(f"image/png")
elif file_name.endswith(".pdf"):
    print(f"application/pdf")
elif file_name.endswith(".txt"):
    print(f"text/plain")
elif file_name.endswith(".zip"):
    print(f"application/zip")
else:
    print("application/octet-stream")
