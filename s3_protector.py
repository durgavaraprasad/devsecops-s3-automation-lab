import boto3

# 1. Connect to AWS
s3 = boto3.client('s3', region_name='ap-south-1')

def debug_s3():
    print("🔎 Starting Audit...")
    response = s3.list_buckets()
    
    for bucket in response['Buckets']:
        name = bucket['Name']
        print(f"📦 Found Bucket: {name}")
        
        # 2. Check the Public Access Block
        try:
            config = s3.get_public_access_block(Bucket=name)
            status = config['PublicAccessBlockConfiguration']
            print(f"   🛡️ Current Config: {status}")
            
            # 3. If any are False, it's public. Let's fix it!
            if not status['BlockPublicAcls']:
                print(f"   🚨 ALERT: {name} is LEAKY! Fixing...")
                s3.put_public_access_block(
                    Bucket=name,
                    PublicAccessBlockConfiguration={
                        'BlockPublicAcls': True,
                        'BlockPublicPolicy': True,
                        'IgnorePublicAcls': True,
                        'RestrictPublicBuckets': True
                    }
                )
                print(f"   ✅ SUCCESS: {name} is now SECURE.")
        except Exception as e:
            print(f"   ⚠️ Could not read config for {name}: {e}")

if __name__ == "__main__":
    debug_s3()