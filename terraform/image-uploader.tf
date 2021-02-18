resource "yandex_function" "image_uploader" {
  name = var.image_uploader_function.name
  runtime = "python38"
  entrypoint = "src.uploader.handler"
  memory = "128"
  description = "Function for uploading images to bucket (Deployed with Terraform)"
  execution_timeout = "10"
  environment = {
    "AWS_ACCESS_KEY_ID": var.s3_config.access_key,
    "AWS_SECRET_ACCESS_KEY": var.s3_config.secret_key,
    "BUCKET_ID": var.s3_config.bucket
  }
  user_hash = filesha256(data.archive_file.code_archive.output_path)
  content {
    zip_filename = data.archive_file.code_archive.output_path
  }
}

output "yandex_function_image_uploader_id" {
  value = yandex_function.image_uploader.id
}