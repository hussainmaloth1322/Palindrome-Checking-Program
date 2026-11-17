# Q11 – Palindrome Program

**Question-paper requirements:** palindrome program, Git/GitHub, Kubernetes deployment and Selenium automation.

## A. Console program
```powershell
python palindrome.py
```
Try `MADAM` (palindrome) and `HELLO` (not palindrome).

## B. GitHub
Create an empty repository and push this folder using the general Git commands in the top-level README.

## C. Build the image for Kubernetes
```powershell
docker build -t palindrome-app:latest .
```
The Kubernetes cluster must be able to access this image.
- Docker Desktop Kubernetes: use the Docker Desktop engine/context that Kubernetes uses.
- Minikube: instead run `minikube image build -t palindrome-app:latest .`

## D. Deploy
Ensure Kubernetes is enabled/running:
```powershell
kubectl cluster-info
kubectl get nodes
kubectl apply -f deployment.yaml
kubectl get deployments
kubectl get pods
kubectl get services
```
Wait until both Deployment pods show `1/1 Running`.

For Docker Desktop Kubernetes, test:
- `http://localhost:30080/check?word=MADAM`
- `http://localhost:30080/check?word=HELLO`

If using Minikube, run:
```powershell
minikube service palindrome-service --url
```
Use the returned URL as the `PALINDROME_URL` environment variable before running Selenium. Example:
```powershell
$env:PALINDROME_URL = "http://127.0.0.1:XXXXX"
```
Replace `XXXXX` with the port returned by Minikube.

## E. Selenium
With the Kubernetes application still running:
```powershell
pip install -r requirements.txt
python -m unittest test_palindrome_selenium.py -v
```
Chrome must be installed. Selenium Manager normally manages the matching driver.

## F. Cleanup
```powershell
kubectl delete -f deployment.yaml
```
