terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.17.0"
    }
  }
}

provider "google" {
  credentials = "gcp_creds.json"
  project     = "my_project_123"
  region      = "europe-west9-c"
}