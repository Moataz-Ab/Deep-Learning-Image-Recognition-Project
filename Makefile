docker_build:
  docker build -t ${GCR_REGION}/${GCP_PROJECT}/${GCR_IMAGE}:prod .

docker_push:
  docker push ${GCR_REGION}/${GCP_PROJECT}/${GCR_IMAGE}:prod

# docker_run:
#   docker run -e PORT=8000 -p 8000:8000 --env-file .env ${GCR_REGION}/${GCP_PROJECT}/${GCR_IMAGE}:prod

docker_interactive:
  docker run -it --env-file .env ${GCR_REGION}/${GCP_PROJECT}/${GCR_IMAGE}:prod /bin/bash

docker_deploy:
  gcloud run deploy --image ${GCR_REGION}/${GCP_PROJECT}/${GCR_IMAGE}:pred --memory ${GCR_MEMORY} --region ${GCP_REGION}

# for v2 only
docker_build_custom: ## <-- fixed
    docker build -t eu.gcr.io/lewagon-bootcamp-1341/aircraft_prediction:v2 .

docker_push_custom: ## <-- fixed
    docker push eu.gcr.io/lewagon-bootcamp-1341/aircraft_prediction:v2

docker_run_custom: ## <-- fixed
    docker run -e PORT=8000 -p 8000:8000 eu.gcr.io/lewagon-bootcamp-1341/aircraft_prediction:v2

docker_deploy_v2: ## <-- fixed
    gcloud run deploy --image eu.gcr.io/lewagon-bootcamp-1341/aircraft_prediction:v2 --memory ${GCR_MEMORY} --region ${GCP_REGION}
