
terraform {
  cloud {
    organization = "ecom_project"

    workspaces {
      name = "ceri-m1-ecommerce-2022"
    }
  }
}

provider "google" {
  project = "ceri-m1-ecommerce-2022"
  region  = "europe-west1"
}

data "google_secret_manager_secret" "address" {
  secret_id = "mysql-address"
}

data "google_secret_manager_secret" "user" {
  secret_id = "mysql-database-greenfish"
}

data "google_secret_manager_secret" "password" {
  secret_id = "mysql-user-greenfish"
}



resource "google_cloud_run_service" "backend" {
  name="backend"
  location = "europe-west1"

  template {
     metadata {
        annotations = {
          "autoscaling.knative.dev/maxScale" = "1"
        }
      }
    spec {
      service_account_name = "terraform-greenfish@ceri-m1-ecommerce-2022.iam.gserviceaccount.com"
     
      containers {
        image = "europe-west1-docker.pkg.dev/ceri-m1-ecommerce-2022/greenfish/backend:0.0.1"
        env {
          name = "DATABASE_ADDRESS"
          value_from {
            secret_key_ref {
              name = data.google_secret_manager_secret.address.secret_id
              key = "latest"

            }
          }
        }
        env {
          name = "DATABASE_USER"
          value_from {
            secret_key_ref {
              name = data.google_secret_manager_secret.user.secret_id
              key = "latest"
            }
          }
        }

        env {
          name = "DATABASE_PASSWORD"
          value_from {
            secret_key_ref {
              name = data.google_secret_manager_secret.password.secret_id
              key = "latest"

            }
          }
        }
      }
    }
  }
}


resource "google_cloud_run_service" "frontend" {
  name="frontend"
  location = "europe-west1"
  template {

     metadata {
        annotations = {
          "autoscaling.knative.dev/maxScale" = "1"
        }
      }
    spec {
      service_account_name = "terraform-greenfish@ceri-m1-ecommerce-2022.iam.gserviceaccount.com"
     
      containers {
        image = "europe-west1-docker.pkg.dev/ceri-m1-ecommerce-2022/greenfish/frontend:0.0.1"
        env {
          name  = "back_url"
          value = google_cloud_run_service.backend.status.0.url
        }
      }
    }
  }
}

output "back_url" {
  value = google_cloud_run_service.backend.status[0].url
}

output "front_url" {
  value = google_cloud_run_service.frontend.status[0].url
}



