
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

data "google-secret-manager-secret" "address" {
  secret_id = "mysql-address"
}

data "google-secret-manager-secret" "user" {
  secret_id = "mysql-database-greenfish"
}

data "google-secret-manager-secret" "password" {
  secret_id = "mysql-user-greenfish"
}



resource "google-cloud" "backend" {
  template {
    spec {
      container {
        //...
        env {
          name = "DATABASE_ADDRESS"
          value_from {
            secret-key-ref {
              name = data.google.secret.address.mysql_database
            }
          }
        }
        env {
          name = "DATABASE_USER"
          value_from {
            secret-key-ref {
              name = data.google.secret.user.secret_id
            }
          }
        }

        env {
          name = "DATABASE_PASSWORD"
          value_from {
            secret-key-ref {
              name = data.google.secret.password.secret_id
            }
          }
        }
      }
    }
  }
}

