variable "bq_dataset_name" {
    description = "Bigquery Dataset name"
    default = "example_dataset"
}

variable "gcp_storage_class" {
    description = "Bucket storage class"
    default = "STANDARD"
}

variable "gcs_bucket_name" {
    description = "Storage bucket name"
    default = "extended-web-448520-b2-terra-bucket"
}

variable "location" {
    default = "EUROPE-WEST9"
}