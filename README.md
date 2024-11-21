# CSV file Manger

This project is a web application built using Flask, Vue, PostgreSQL, and Docker Compose. It allows users to upload CSV files to the file system, save metadata to a PostgreSQL database, and retrieve file details through APIs.

## Features

- Upload CSV files and save metadata to PostgreSQL
- View the uploaded files and metadata
- Display file contents with column details

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

Ensure you have Docker and Docker Compose installed on your system before proceeding.

## Getting Started

Follow the steps below to run the application locally using Docker Compose.

### Clone the Repository

Clone this repository to your local machine:

```bash
git clone git@github.com:dxb2306/task.git
cd task
```

## Build and Start the Application
Now you can start the application using Docker Compose.

Run the following command to build and start the application:

```bash
docker-compose up --build
```

## Run Vue
```bash
http://localhost:8081/
```
