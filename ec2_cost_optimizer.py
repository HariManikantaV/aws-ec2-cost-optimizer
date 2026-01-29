import boto3

ec2 = boto3.client('ec2')
pricing = boto3.client('pricing', region_name='us-east-1')

def get_stopped_instances():
    response = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}]
    )
    instances = []
    for res in response['Reservations']:
        for inst in res['Instances']:
            instances.append(inst['InstanceId'])
    return instances

def get_unused_volumes():
    response = ec2.describe_volumes(
        Filters=[{'Name': 'status', 'Values': ['available']}]
    )
    return [vol['VolumeId'] for vol in response['Volumes']]

if __name__ == "__main__":
    print("Stopped EC2 Instances:", get_stopped_instances())
    print("Unused EBS Volumes:", get_unused_volumes())
