resource "yandex_function" "image-uploader" {
  name = var.image_uploader_function.name
  runtime = "python37-preview"
  entrypoint = "main"
  memory = "128"
  execution_timeout = "10"
  user_hash = filesha256("../image-uploader.zip")
  content {
    zip_filename = "../image-uploader.zip"
  }
}

output "yandex_function_test-function" {
  value = yandex_function.image-uploader.id
}