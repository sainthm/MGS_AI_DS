# Bloeck-external-ip

{
    "Version": "2012-10-17",
    "Statement": {
        "Effect": "Deny",
        "Action": "*",
        "Resource": "*",
        "Condition": {
            "IpAddress": {
                "Notaws:SourceIp": [
                    "10.xxx.xxx.xxx/16",
                    "10.xxx.xx.xx/16",
                    "52.xxx.xxx.xxx/xx",
                    "13.xxx.xxx.xxx/xx"
                ]
            },
            "StringEqualsIfExists": {
                "Notaws:SourceVpc": [
                    "vpc-xxxxxx",
                    "vpc-xxxxxx"
                ]
            }
        }
    }
}