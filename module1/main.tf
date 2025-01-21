resource "google_storage_bucket" "demo-bucket" {
  name          = "extended-web-448520-b2-terra-bucket"
  location      = "EUROPE-WEST9"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}