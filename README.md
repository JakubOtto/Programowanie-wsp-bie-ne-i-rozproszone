# StockX Scraper with Django and Docker

## Description
This is a Django-based project designed to scrape data from StockX. Currently, the project includes a basic web scraping setup accessible via a single endpoint (`/scrape`). The application uses Docker for containerization to simplify deployment and environment management.

## Features (Current State)
- A single endpoint: `http://localhost:8000/scrape` that triggers the scraping process.
- Basic web scraping logic for retrieving data from StockX.
- Containerized with Docker for ease of setup.

## Technologies
- Django (backend)
- Docker (containerization)
- BeautifulSoup or requests (web scraping)
- SQLite (default database for development)

## Installation

### Prerequisites
- Docker and Docker Compose installed on your system.

### Steps
1. Clone the repository:
  git clone https://github.com/username/stockx-scraper.git

3. Navigate to the project folder:
  cd stockx-scraper

4. Build and run the Docker containers:
  docker-compose up --build

5. Access the application:
  Scraper endpoint: http://localhost:8000/scrape
