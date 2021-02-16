variable "yc_token" {
  type = string
  sensitive = true
  description = "Token for Yandex Cloud accessing"
}

variable "yc_cloud_id" {
  type = string
  sensitive = true
  description = "Cloud id for deploying"
}

variable "yc_folder_id" {
  type = string
  sensitive = true
  description = "Folder id for deploying"
}

variable "image_uploader_function" {
  type = object({
    name = string
  })

  description = "Properties for image uploader cloud function"
}

//variable "s3_backend_props" {
//  type = object({
//    endpoint = string
//    bucket = string
//    region = string
//    key = string
//    access_key = string
//    secret_key = string
//  })
//}