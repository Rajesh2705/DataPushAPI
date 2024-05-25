
# Data Push API

A simple webhook receiver API that pass data to user destinations. Task Queue with Producer / Consumer and Message Broker.




## Installation

Install DataPushAPI-Project

```git
  git clone git@github.com:Rajesh2705/DataPushAPI.git
  cd  DataPushAPI/base/
```

Before Proceeding Further Meke sure your in "DataPushAPI/base/" directory

#### create virtual environment

```bash
  python -m venv .venv
  source ./.venv/bin/activate
```

#### install project dependencies

```python
  pip install -r requirements.txt
```
___

**This Project use Redis and Celery for Task Queue**

**Setup Redis**
```shell
    sudo apt update
    sudo apt install redis
```

**Run Redis Server**
```shell
  redis-server
```
___


**DataPushAPI Database Migrations**
```shell
  python manage.py makemigrations
  python manage.py migrate
```

___

### Run Application
run the below command and start celery task queue server in backround
```shell
  python -m celery -A celery_app worker
```
**open new terminal** and run following command to start DataPushAPI application

```shell
  python manage.py runserver
```
## Django Admin UI
***URL - http://127.0.0.1:8000/admin/login/***

Default Admin Credentials
```bash
username : admin
password : QVKL67KNtROt02s
```
## API Reference
swagger-ui - ***http://127.0.0.1:8000/api/schema/swagger-ui/***
# WebHook Project API
a simple webhook receiver API that pass data to destinations

## Version: 1.0.0

### /api/accounts/

#### POST
##### Responses

| Code | Description |
| ---- | ----------- |
| 201 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| cookieAuth | |
| basicAuth | |

### /api/accounts/{id}/

#### PUT
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A UUID string identifying this custom user. | Yes | string (uuid) |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| cookieAuth | |
| basicAuth | |

#### PATCH
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A UUID string identifying this custom user. | Yes | string (uuid) |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| cookieAuth | |
| basicAuth | |

#### DELETE
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A UUID string identifying this custom user. | Yes | string (uuid) |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | No response body |

##### Security

| Security Schema | Scopes |
| --- | --- |
| cookieAuth | |
| basicAuth | |

### /api/accounts/login/

#### POST
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| cookieAuth | |
| basicAuth | |

### /api/accounts/logout/

#### POST
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| cookieAuth | |
| basicAuth | |

### /api/accounts/register/

#### POST
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| cookieAuth | |
| basicAuth | |

### /api/destinations/

#### GET
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| cookieAuth | |
| basicAuth | |

#### POST
##### Responses

| Code | Description |
| ---- | ----------- |
| 201 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| cookieAuth | |
| basicAuth | |

### /api/destinations/{id}/

#### GET
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this destination. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| cookieAuth | |
| basicAuth | |

#### PUT
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this destination. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| cookieAuth | |
| basicAuth | |

#### PATCH
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this destination. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| cookieAuth | |
| basicAuth | |

#### DELETE
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this destination. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | No response body |

##### Security

| Security Schema | Scopes |
| --- | --- |
| cookieAuth | |
| basicAuth | |

### /api/headers/

#### GET
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| cookieAuth | |
| basicAuth | |

#### POST
##### Responses

| Code | Description |
| ---- | ----------- |
| 201 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| cookieAuth | |
| basicAuth | |

### /api/headers/{id}/

#### GET
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this header. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| cookieAuth | |
| basicAuth | |

#### PUT
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this header. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| cookieAuth | |
| basicAuth | |

#### PATCH
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this header. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

##### Security

| Security Schema | Scopes |
| --- | --- |
| cookieAuth | |
| basicAuth | |

#### DELETE
##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this header. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | No response body |

##### Security

| Security Schema | Scopes |
| --- | --- |
| cookieAuth | |
| basicAuth | |

### /api/server/incoming_data/

#### POST
##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | No response body |

##### Security

| Security Schema | Scopes |
| --- | --- |
| cookieAuth | |
| basicAuth | |

