variable "aws_region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "db_password" {
  description = "Password for MySQL database"
  type        = string
  sensitive   = true
}

variable "db_username" {
  description = "Username for MySQL database"
  type        = string
  default     = "admin"
}
