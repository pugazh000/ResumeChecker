#!/bin/bash
aws s3 sync frontend/ s3://your-bucket-name --acl public-read
