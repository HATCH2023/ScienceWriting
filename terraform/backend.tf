terraform {
  backend "s3" {
    bucket = "hatch-tf"
    key = "terraform.tfstate"
    region = "us-east-1"
  }
}
