resource "aws_dynamodb_table" "unique_pairs_request_logs" {
  name     = "${var.environment}-UniquePairsRequestLogs"
  hash_key = "RequestID"

  attribute {
    name = "RequestID"
    type = "S"
  }

  attribute {
    name = "Timestamp"
    type = "N"
  }

  attribute {
    name = "RequestData"
    type = "S"
  }

  tags = {
    Environment = var.environment
  }
}
