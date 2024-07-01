#POST-type requests essentially mean "take this document"
import httpx 
response = httpx.post("http://httpbin.org/post", json={"question":"what is the meaning of life for an ant?"})
print(response.text)
