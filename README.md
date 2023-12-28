# FastAPI Hello World App

This is a simple FastAPI application that exposes a REST API endpoint `/hello`, printing "Hello world" plus a `SERVICE_VERSION` environment variable.

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Python](https://www.python.org/)
- [Poetry](https://python-poetry.org/)

## Getting Started

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Change into the project directory:

    ```bash
    cd hello-world-api
    ```

### Running with Docker

3. Build the Docker image:

    ```bash
    docker build -t hello-world-api .
    ```

4. Run the Docker container:

    ```bash
    docker run -p 8000:8000 -e SERVICE_VERSION=1.0 hello-world-api
    ```

### Running without Docker

3. Install dependencies with [Poetry](https://python-poetry.org/):

    ```bash
    poetry shell
    poetry install
    ```

4. Run the FastAPI application:

    ```bash
    cd app
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    ```

## API Endpoint

- **Endpoint:** `/hello`
- **Method:** GET
- **Response:**
  - Body: `{"content": "Hello world <SERVICE_VERSION>"}`

## Testing

To run tests, use the following command:

```bash
poetry run pytest
```

## Deployment in Azure

This API has been deployed on Azure.

The follwing steps were taken:

- An Azure Kubernetes Cluster and an Azure Container Register were created using the Azure Portal.
- The app was tagged and pushed the to the ACR as follows
```
docker tag hello-world-api helloworldtask2024.azurecr.io/hello-world-api
docker push  helloworldtask2024.azurecr.io/hello-world-api 
```
- Two versions of the app were deployed on the cluster and the incoming traffic was routed with an 80/20 split using Istio as an ingress gateway, taking advantage of Destination Rules and Virtual Services.
The following is a quick summary of the steps to achieve this:



    -  Set ENV Vars for help later on
        ```
        export CLUSTER=helloworld
        export RESOURCE_GROUP=hello-world
        export LOCATION=uksouth
        ```


    - Enable Istio in cluster

        ```
        az aks mesh enable --resource-group ${RESOURCE_GROUP} --name ${CLUSTER}
        ```

    - Verify istio installation
        ```
        az aks show --resource-group ${RESOURCE_GROUP} --name ${CLUSTER}  --query 'serviceMeshProfile.mode'
        ```

    - Get cluster credentials
        ```
        az aks get-credentials --resource-group ${RESOURCE_GROUP} --name ${CLUSTER}
        ```

    - Verify that istio is running
        ```
        kubectl get pods -n aks-istio-system
        ```

    - Enable sidecar injection
        ```
        kubectl label namespace default istio.io/rev=asm-1-17
        ```

    - Deploy the API on the cluster
        ```
        kubectl apply -f deployments.yaml
        ```

    - Enable an externally accessible Istio ingress
        ```
        az aks mesh enable-ingress-gateway --resource-group $RESOURCE_GROUP --name $CLUSTER --ingress-gateway-type external
        ```

    - Check the service mapped to the ingress gateway
        ```
        kubectl get svc aks-istio-ingressgateway-external -n aks-istio-ingress
        ```

    - Make application accessible from gateway using Gateway and Virtual Service. Also apply routing weights

        ```
        kubectl apply -f gateway.yaml
        ```

    - Set environment variables for external ingress host and ports:
        ```
        export INGRESS_HOST_EXTERNAL=$(kubectl -n aks-istio-ingress get service aks-istio-ingressgateway-external -o jsonpath='{.status.loadBalancer.ingress[0].ip}')

        export INGRESS_PORT_EXTERNAL=$(kubectl -n aks-istio-ingress get service aks-istio-ingressgateway-external -o jsonpath='{.spec.ports[?(@.name=="http2")].port}')

        export GATEWAY_URL_EXTERNAL=$INGRESS_HOST_EXTERNAL:$INGRESS_PORT_EXTERNAL```
        ```
    - Retrieve the external address of the sample application:
        ```
        echo "http://$GATEWAY_URL_EXTERNAL/productpage"
        ```
- :)
