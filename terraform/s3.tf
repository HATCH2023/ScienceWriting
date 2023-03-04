resource "aws_s3_bucket" "website" {
  bucket = "science-writing-site"
}

resource "aws_s3_bucket_acl" "website" {
  bucket = aws_s3_bucket.website.id
  acl = "public-read"
}

resource "aws_s3_bucket_versioning" "website" {
  bucket = aws_s3_bucket.website.id
  versioning_configuration {
    status = "Disabled"
  }
}

resource "aws_s3_bucket_website_configuration" "website" {
  bucket = aws_s3_bucket.website.id

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "error.html"
  }
}

module "template_files" {
  source = "hashicorp/dir/template"
  base_dir = var.website_root
}

resource "aws_s3_bucket_object" "file" {
  for_each = module.template_files.files

  bucket = aws_s3_bucket.website.id
  key = each.key
  content_type = each.value.content_type
  content_disposition = "inline"
  source      = "${var.website_root}/${each.key}"
  source_hash = filemd5("${var.website_root}/${each.key}")
  acl = "public-read"
}

resource "aws_s3_bucket_public_access_block" "website" {
  bucket = aws_s3_bucket.website.id

  block_public_acls = false
  block_public_policy = false
}

output "bucket_name" {
  value = aws_s3_bucket.website.id
}
