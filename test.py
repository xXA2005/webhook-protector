import requests

r = requests.post("http://127.0.0.1:5000",json={"content":"ase"})
# working
print(r.text)
print(r.status_code)

# protected from deletion
r = requests.delete("http://127.0.0.1:5000")
print(r.status_code)
print(r.text)