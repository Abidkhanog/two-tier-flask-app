# Two-Tier Flask App — CI/CD Deployment

A fully automated CI/CD pipeline to deploy a two-tier Flask application (Flask + MySQL) on AWS EC2 using Jenkins, Docker, and Docker Compose. Integrates GitHub for version control and ensures seamless, reliable, hands-free deployments.

## Architecture

- **App tier**: Python Flask app serving a simple message board
- **Data tier**: MySQL database (containerized)
- **CI/CD**: Jenkins pipeline builds the Docker image, pushes to Docker Hub, and redeploys via Docker Compose on every push to `main`
- **Hosting**: AWS EC2 instance running Docker + Jenkins

## Tech Stack

`Flask` `MySQL` `Docker` `Docker Compose` `Jenkins` `AWS EC2` `GitHub`

## Project Structure

```
.
├── app.py                 # Flask application
├── templates/
│   └── index.html         # Frontend template
├── requirement.txt        # Python dependencies
├── message.sql            # DB schema + seed data
├── Dockerfile              # Container build for the Flask app
├── docker-compose.yml     # Multi-container orchestration (app + db)
├── Jenkinsfile             # CI/CD pipeline definition
└── diagrams/               # Architecture diagrams
```

## Local Setup

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/two-tier-flask-app.git
cd two-tier-flask-app
docker-compose up -d --build
```

App will be available at `http://localhost:5000`

## CI/CD Pipeline

1. Developer pushes code to `main` branch on GitHub
2. Jenkins (via webhook or polling) triggers the pipeline
3. Jenkins builds a new Docker image of the Flask app
4. Image is pushed to Docker Hub
5. Jenkins redeploys the updated containers using Docker Compose on the EC2 instance

## Environment Variables

| Variable | Description | Default |
|---|---|---|
| `MYSQL_HOST` | MySQL container hostname | `mysql` |
| `MYSQL_USER` | MySQL username | `root` |
| `MYSQL_PASSWORD` | MySQL password | `password` |
| `MYSQL_DATABASE` | Database name | `messagedb` |

## Author

Built by Abid Khan as a hands-on DevOps project covering containerization, CI/CD, and cloud deployment.
