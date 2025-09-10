import requests
import os
from urllib.parse import urlparse
import hashlib

def get_filename_from_url(url, content):
    """Extract filename from URL or generate a unique one using hash."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    
    if not filename or "." not in filename:  
        # If no filename or no extension, generate one
        file_hash = hashlib.md5(content).hexdigest()[:8]  # Unique hash for content
        filename = f"image_{file_hash}.jpg"
    
    return filename

def fetch_image(url):
    """Download a single image and save it."""
    try:
        # Make directory if it doesn’t exist
        os.makedirs("Fetched_Images", exist_ok=True)

        # Fetch image with respectful timeout
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises error for 4xx/5xx codes

        # Check content-type header before saving
        content_type = response.headers.get("Content-Type", "")
        if "image" not in content_type:
            print(f"✗ Skipped (not an image): {url}")
            return

        # Generate filename
        filename = get_filename_from_url(url, response.content)
        filepath = os.path.join("Fetched_Images", filename)

        # Prevent duplicates by checking existing file content
        if os.path.exists(filepath):
            with open(filepath, "rb") as f:
                if f.read() == response.content:
                    print(f"✓ Duplicate skipped: {filename}")
                    return

        # Save image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # User can provide multiple URLs separated by commas
    urls = input("Please enter image URL(s), separated by commas: ").split(",")

    for url in [u.strip() for u in urls if u.strip()]:
        fetch_image(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
