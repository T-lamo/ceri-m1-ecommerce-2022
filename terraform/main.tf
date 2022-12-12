
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


