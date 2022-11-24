안녕하세요. AWS Secrets Manager에 DB Password를 정의하고, RDS에서 해당 Password를 참조하고 싶은데, 에러가 발생하고 있습니다 ㅠㅠ aws_db_instance.example.password에 작성한 data.aws_secretsmanager_secret_version.db_password.secret_id 이 부분이 잘못된 것 같은데 맞을까요 ? 코드는 아래와 같습니다. 

resource "random_password" "password" {
  length           = 16
  special          = true
  override_special = "_%@"
}

# Creating a AWS secret for database master account (Masteraccoundb)
resource "aws_secretsmanager_secret" "db_password" {
  name = "db-password"
}

# Creating a AWS secret versions for database master account (Masteraccoundb)
resource "aws_secretsmanager_secret_version" "db_password" {
  secret_id     = aws_secretsmanager_secret.db_password.id
  secret_string = random_password.password.result
}

# Importing the AWS secrets created previously using arn.
data "aws_secretsmanager_secret" "db_password" {
  arn = aws_secretsmanager_secret.db_password.arn
}

# Importing the AWS secret version created previously using arn.
data "aws_secretsmanager_secret_version" "db_password" {
  secret_id = data.aws_secretsmanager_secret.db_password.id
}


resource "aws_db_instance" "example" {
  identifier_prefix   = "example"
  engine              = "mysql"
  allocated_storage   = 10
  instance_class      = "db.t2.micro"
  skip_final_snapshot = true
  db_name             = var.db_name

  # Pass the secrets to the resource
  username = "admin"
  password = data.aws_secretsmanager_secret_version.db_password
}

variable "db_name" {
  description = "The name to use for the database"
  type        = string
  default     = "example"
}