import requests
import os
from urllib.parse import urlparse
import hashlib

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Ask user for multiple URLs (comma-separated)
    urls = input("Please enter one or more image URLs (separate by commas): ").split(",")
    
    # Create directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)
    
    for url in urls:
        url = url.strip()  # remove spaces
        if not url:
            continue
        
        try:
            # Fetch the image
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise exception for bad status codes
            
            # Check if response is an image
            content_type = response.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                print(f"✗ Skipped (not an image): {url}")
                continue
            
            # Extract filename from URL or generate one
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            
            if not filename:
                # Fallback filename
                filename = "downloaded_image.jpg"
            
            # Prevent duplicates by hashing content
            file_hash = hashlib.md5(response.content).hexdigest()
            name, ext = os.path.splitext(filename)
            filename = f"{name}_{file_hash[:6]}{ext if ext else '.jpg'}"
            
            filepath = os.path.join("Fetched_Images", filename)
            
            # Save the image in binary mode
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")
        
        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error: {e}")
        except Exception as e:
            print(f"✗ An error occurred: {e}")
    
    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
