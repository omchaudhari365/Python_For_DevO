cloud_services = {
    "EC2",
    "S3",
    "Lambda",
    "RDS",
    "EC2"  # Duplicate, will be ignored
}

print(cloud_services)

# Add a service
cloud_services.add("CloudFront")
print(cloud_services)

# Remove a service
cloud_services.remove("RDS")
print(cloud_services)

# Check if service exists
print("S3" in cloud_services)

# Number of services
print(len(cloud_services))

# Loop through the set
for service in cloud_services:
    print(service)