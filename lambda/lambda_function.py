import json

def lambda_handler(event, context):

    print("===== S3 Event Received =====")

    try:

        # -----------------------------------------
        # Read Event Details
        # -----------------------------------------

        bucket_name = event["detail"]["bucket"]["name"]
        object_key = event["detail"]["object"]["key"]

        file_name = object_key.split("/")[-1]
        folder_name = object_key.split("/")[1]

        print(f"Bucket Name : {bucket_name}")
        print(f"Object Key  : {object_key}")
        print(f"Folder Name : {folder_name}")
        print(f"File Name   : {file_name}")

        # -----------------------------------------
        # Landing Folder Validation
        # -----------------------------------------

        if not object_key.startswith("landing/"):

            print("File is NOT inside landing folder.")
            print("Ignoring this event.")

            return {
                "statusCode": 200,
                "body": "Ignored - Invalid Folder"
            }

        print("Landing Folder Validation Successful")

        # -----------------------------------------
        # CSV File Validation
        # -----------------------------------------

        if not object_key.lower().endswith(".csv"):

            print("Uploaded file is NOT a CSV file.")
            print("Ignoring this event.")

            return {
                "statusCode": 200,
                "body": "Ignored - Invalid File Type"
            }

        print("CSV File Validation Successful")

        # -----------------------------------------
        # Dataset Validation
        # -----------------------------------------

        allowed_datasets = [
            "customers",
            "products",
            "orders",
            "order_items",
            "payments",
            "refunds",
            "delivery"
        ]

        if folder_name not in allowed_datasets:

            print(f"Invalid Dataset : {folder_name}")
            print("Ignoring this event.")

            return {
                "statusCode": 200,
                "body": "Ignored - Invalid Dataset"
            }

        print("Dataset Validation Successful")

        # -----------------------------------------
        # Processing Completed Successfully
        # -----------------------------------------

        return {
            "statusCode": 200,
            "body": json.dumps("Validation Successful")
        }

    except Exception as e:

        print(f"Error : {str(e)}")
        raise e