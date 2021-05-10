terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
      version = "0.57.0"
    }
  }
}

provider "yandex" {
  token = var.yc_token
  cloud_id = var.yc_cloud_id
  folder_id = var.yc_folder_id
}

//terraform {
//  backend "s3" {
//    endpoint = var.s3_backend_props.endpoint
//    bucket = var.s3_backend_props.bucket
//    region = var.s3_backend_props.region
//    key = var.s3_backend_props.key
//    access_key = var.s3_backend_props.access_key
//    secret_key = var.s3_backend_props.secret_key
//
//    skip_region_validation = true
//    skip_credentials_validation = true
//  }
//}
