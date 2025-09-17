# Ubuntu Image Fetcher

A mindful Python tool for downloading and organizing images from the web, following Ubuntu principles of community, respect, and practicality.

---

## 📌 Overview

The Ubuntu Image Fetcher is a command-line program that allows users to download images from the internet safely and store them in an organized manner. It handles errors gracefully, prevents duplicates, and ensures only valid image files are saved.

---

## 🛠 Features

- Prompt the user to input one or more image URLs.
- Creates a directory called `Fetched_Images` if it doesn’t exist.
- Downloads images using the `requests` library.
- Saves images in binary mode with unique filenames.
- Prevents downloading duplicate images using content hashing.
- Checks HTTP headers to ensure the content is an actual image.
- Handles network or invalid URL errors gracefully without crashing.

---

## ⚡ Ubuntu Principles Implemented

- **Community:** Connects to the wider web to fetch images.
- **Respect:** Handles errors gracefully without interrupting the user experience.
- **Sharing:** Organizes downloaded images in a dedicated folder for easy access and sharing.
- **Practicality:** Serves a real need by providing a simple, reliable tool to collect images.

---

## 📥 Installation

1. Make sure you have **Python 3** installed.
2. Install the `requests` library if not already installed:

```bash
pip install requests
