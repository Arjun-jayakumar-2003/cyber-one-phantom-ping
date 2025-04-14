import requests  # External library that makes HTTP requests easier

# Send a GET request directly to the IP, but include the real Host in the header
response = requests.get(
    "http://104.16.248.102",                      # IP address of the server
    headers={"Host": "one.one.one.one"},          # Simulate visiting the real domain
    allow_redirects=True                          # Follow 301/302 redirects automatically
)

# Print the final URL after following redirects (if any)
print(f"Final URL: {response.url}")

# Print the HTTP status code (e.g., 200 OK)
print(f"Status Code: {response.status_code}")

# Print first 500 characters of the page content (HTML)
print("\n--- Body (First 500 chars) ---")
print(response.text[:500])
