# Grafana Loki

Studies based in day 61-62 of 100 Days System Design for DevOps and Cloud Engineers.

https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f

Days 61–70: Advanced Observability and Analytics

Day 61–62: Set up and configure Grafana Loki for log aggregation and analysis.

## How to Use:


Execute docker compose:
```
docker compose up --build
```

You can see basic FastAPI in ```localhost:8000``` or:
```
curl http://localhost:8000
```

### Configure FastAPI logs inside Grafana:

* Browse to ```localhost:3000```, log as admin/admin.

* Click ```Add Your First Data Source```.

* Change HTTP url to ```http://loki:3100```.

* Save, go to homepage and search for ```Create Dashboard```.

* Click ```Add a new panel```, select ```application``` ```=``` ```fastapi```

* Click ```Run queries```

* Browse fastapi application to see logs grow every time you run the query again.

## Author
This project was implemented by [Lucas de Queiroz dos Reis][2]. It is based on the Day 23–24: Automate multi-environment setups using Terraform and Ansible dynamic inventories from the [100 Days System Design for DevOps and Cloud Engineers][1].

[1]: https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f "Medium - Deo Shankar 100 Days"
[2]: https://www.linkedin.com/in/lucas-de-queiroz/ "LinkedIn - Lucas de Queiroz"