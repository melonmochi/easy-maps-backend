# Offline solution for maps tools build with flask. <http://flask.pocoo.org/>

English | [Español](./README-es_ES.md)

[![Build Status](https://dev.azure.com/melonmochi3/easy-maps-backend/_apis/build/status/melonmochi3.easy-maps-backend?branchName=master)](https://dev.azure.com/melonmochi3/easy-maps-backend/_build/latest?definitionId=1?branchName=master)

## ⌨️ Development

```bash
git clone git@github.com:melonmochi/easy-maps-backend.git
cd easy-maps-backend
```

## 🏈 Install

Setup a virtual env to install the package (recommended):

```bash
python3 -m venv env
source ./env/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🏃 Run

```bash
python manage.py runserver
```

Open your browser and visit <http://127.0.0.1:5000>

## 🗺️ RoadMap

- Use Docker to build app container. <https://www.docker.com/>
- Use Kubernetes (K8s) as containers manager. <https://kubernetes.io/>
- Use Azure Pipelines as CI/CD solution. <https://azure.microsoft.com/en-us/services/devops/pipelines/>
- Use GraphQL as query language. <https://www.graphql.org/>
- Connect to postgresql. <https://www.postgresql.org/>
- Support offline map tiles rendering service.
- Support offline map routing service.

## 🤝 Contributing [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

We welcome all contributions.

## 🌍 License

[MIT](https://github.com/melonmochi/easy-maps-backend/blob/master/LICENSE)