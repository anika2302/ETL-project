import boto3

# Create an S3 client
s3 = boto3.client('s3')

result = s3.get_bucket_acl(Bucket='redshiftzagdb')
print(result)

response = s3.list_buckets()

# Get a list of all bucket names from the response
buckets = [bucket['Name'] for bucket in response['Buckets']]

# Print out the bucket list
print("Bucket List: %s" % buckets)

filename = 'soldvia.csv'
bucket_name = 'redshiftzagdb'
s3name = 'soldvia.csv'

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
s3.upload_file(filename, bucket_name, s3name)