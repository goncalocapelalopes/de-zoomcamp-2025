terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.17.0"
    }
  }
}

provider "google" {
  credentials = "/Users/goncalopes/Downloads/gcp_creds.json"
  project     = "extended-web-448520-b2"
  region      = "europe-west9-c"
}