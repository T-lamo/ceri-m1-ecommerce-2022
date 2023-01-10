
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

data "google_secret_manager_secret" "algolia_app_id" {
  secret_id = "algolia-greenfish-application-id"
}

data "google_secret_manager_secret" "algolia_app_key" {
  secret_id = "algolia-greenfish-api-key"
}
resource "google_cloud_run_service" "backend" {
  name     = "greenfish-backend"
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
        image = "europe-west1-docker.pkg.dev/ceri-m1-ecommerce-2022/greenfish/backend:1.0.0"
        env {
          name = "DATABASE_ADDRESS"
          value_from {
            secret_key_ref {
              name = data.google_secret_manager_secret.address.secret_id
              key  = "latest"

            }
          }
        }
        env {
          name = "DATABASE_USER"
          value_from {
            secret_key_ref {
              name = data.google_secret_manager_secret.user.secret_id
              key  = "latest"
            }
          }
        }

        env {
          name = "DATABASE_PASSWORD"
          value_from {
            secret_key_ref {
              name = data.google_secret_manager_secret.password.secret_id
              key  = "latest"

            }
          }
        }

        env {
          name = "ALGOLIA_KEY"
          value_from {
            secret_key_ref {
              name = data.google_secret_manager_secret.algolia_app_key.secret_id
              key  = "latest"

            }
          }
        }


        env {
          name = "ALGOLIA_APP_ID"
          value_from {
            secret_key_ref {
              name = data.google_secret_manager_secret.algolia_app_id.secret_id
              key  = "latest"

            }
          }
        }

      }
    }
  }
}


resource "google_cloud_run_service" "frontend" {
  name     = "greenfish-frontend"
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
        image = "europe-west1-docker.pkg.dev/ceri-m1-ecommerce-2022/greenfish/frontend:1.0.0"
        env {
          name  = "back_url"
          value = google_cloud_run_service.backend.status.0.url
        }
      }
    }
  }
}


resource "google_cloud_run_service_iam_member" "backend" {
  location = google_cloud_run_service.backend.location
  service  = google_cloud_run_service.backend.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}

resource "google_cloud_run_service_iam_member" "frontend" {
  location = google_cloud_run_service.frontend.location
  service  = google_cloud_run_service.frontend.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}
output "back_url" {
  value = google_cloud_run_service.backend.status[0].url
}

output "front_url" {
  value = google_cloud_run_service.frontend.status[0].url
}




