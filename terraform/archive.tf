provider "archive" {}

data "archive_file" "code_archive" {
  type        = "zip"
  source_dir = "../"
  output_path = "serverless-image-handler.zip"
  excludes = [
    "venv",
    ".git",
    ".DS_Store",
    ".env",
    ".idea",
    "__pycache__",
    "serverless-image-handler.zip",
    "terraform",
    "ui"
  ]
}

resource "yandex_storage_object" "code_archive_object" {
  bucket = var.s3_config.bucket
  key    = "terraform/code.zip"
  source = data.archive_file.code_archive.output_path
  access_key = var.s3_config.access_key
  secret_key = var.s3_config.secret_key
}