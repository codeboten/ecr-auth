import base64
import docker
import boto3

region = 'PREFERRED REGION' # us-east-1, us-west-1
image = 'REPO:TAG'

boto_cli = boto3.client('ecr', region_name=region)
docker_cli = docker.from_env()

token = boto_cli.get_authorization_token()
auth_string = base64.b64decode(token['authorizationData'][0]['authorizationToken'])
user = auth_string.split(':')[0]
password = auth_string.split(':')[1]
docker_cli.login(username=user, password=password, registry=token['authorizationData'][0]['proxyEndpoint'])
docker_cli.pull(image)
