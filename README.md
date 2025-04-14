# CyberOne PhantomPing

This Python script demonstrates how to send an HTTP request directly to a server's IP address while spoofing the `Host` header to simulate a request to a specific domain. It’s a stealthy technique used to explore virtual host responses — perfect for your cybersecurity learning journey.

## 🔍 What It Does

- Sends a GET request to a target IP address (`104.16.248.102`)
- Sets a custom `Host` header (`one.one.one.one`)
- Follows redirects automatically
- Prints:
  - The final URL after all redirects
  - The HTTP status code
  - The first 500 characters of the response body

## 💡 Use Case

This technique is handy for:

- Testing how a server responds when accessed by IP instead of domain
- Identifying whether a specific virtual host is running behind a shared IP
- Learning about HTTP headers and how servers process requests

## 📌 Notes

- This script is for educational and ethical testing purposes only.
- You can change the IP or Host header to explore other configurations (e.g., testing CDNs or server routing).
- Requires an internet connection.

## 🚀 Getting Started

1. Make sure Python is installed.
2. Install the `requests` library if you haven’t already:
   ```bash
   pip install requests
   ```
3. Run the script:
   ```bash
   python phantomping.py
   ```

## ⚠️ Disclaimer

This script is intended **only for learning and ethical testing**. Do not use it against any systems you do not have permission to interact with.

---
🔐 *Cyber One* stands for **Month One** of cybersecurity learning.  
Stay curious and keep exploring!
