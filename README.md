# GridWatch

**GridWatch** is a machine learning-basedFastAPI app that predicts potential power grid instability based on real solar irradiance and energy load data. This end-to-end project was designed to demonstrate practical MLOps, climate-tech modeling, and containerized deployment.

> 🔗 Docker Hub: [nkchestnut/gridwatch-app](https://hub.docker.com/r/nkchestnut/gridwatch-app)
>
> Links to datasets used to create the merged data:
>
> California ISO Hourly Load Data for 2022, 2023, & 2024
>
>  https://www.caiso.com/library/historical-ems-hourly-load
>
>  National Solar Radiation Database for Sanfrancisco, California
>
> https://nsrdb.nrel.gov/data-viewer

---

## Features

- **Real-world energy + solar data** from NREL & CAISO (2022–2024)
- **ML model (Random Forest)** to classify risk of grid overload
- **FastAPI backend** with `/predict` endpoint
- **Dockerized** for easy reproducibility
- **CI/CD** using GitHub Actions
-  Designed for deployment on DockerHub

---

##  How to Run Locally with Docker

Make sure you have [Docker installed](https://docs.docker.com/get-docker/).

### Step 1: Pull from Docker Hub

```bash
docker pull nkchestnut/gridwatch-app:latest
```
### Step 2: Run the container

```bash
docker run -p 8000:8000 nkchestnut/gridwatch-app:latest
```
### Step 3: Access the app
- Open browser: http://localhost:8000

- Visit the built-in API docs: http://localhost:8000/docs

## API Usage
- Endpoint: POST /predict
- Example request (JSON):
{
  "GHI": 500,
  "Temperature": 30,
  "Relative Humidity": 50,
  "CAISO": 35000
}

## Tech Stack
Python, Pandas, Scikit-learn

FastAPI

Docker

GitHub Actions (CI/CD)

NREL + CAISO datasets

## Motivation
Following NOAA funding cuts, local grid resilience is more important than ever. This project shows how publicly available energy and weather data can power predictive tools to help cities and communities anticipate strain on infrastructure — all while demonstrating full-stack ML deployment.

## Citation
Sengupta, M., Habte, A., Xie, Y., Lopez, A., & Buster, G. (2018). National Solar Radiation Database (NSRDB). [Data set]. Open Energy Data Initiative (OEDI). National Renewable Energy Laboratory. https://doi.org/10.25984/1810289

California Independent System Operator (CAISO). 2017. California ISO—Historical hourly load data from EMS. 2022-2024. California ISO—Historical hourly load data from EMS.https://www.caiso.com/library/historical-ems-hourly-load
