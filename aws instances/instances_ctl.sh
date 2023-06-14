#!/bin/bash

# make sure to change to your instances region
region="your_region"
action=$1

if [[ "$action" != "--stop" && "$action" != "--start" && "$action" != "--destroy" ]]; then
  echo "Invalid action parameter. Please use --stop, --start, or --destroy."
  exit 1
fi

if [ "$action" == "--destroy" ]; then
  read -p "Are you sure you want to destroy all instances? This action cannot be undone. (y/n): " confirm
  if [ "$confirm" != "y" ]; then
    echo "Action aborted."
    exit 0
  fi
fi

# Get instance IDs based on their current state
if [ "$action" == "--stop" ]; then
  instance_ids=$(aws ec2 describe-instances --region $region --filters Name=instance-state-name,Values=running --query 'Reservations[].Instances[].InstanceId' --output text)
elif [ "$action" == "--start" ]; then
  instance_ids=$(aws ec2 describe-instances --region $region --filters Name=instance-state-name,Values=stopped --query 'Reservations[].Instances[].InstanceId' --output text)
else
  instance_ids=$(aws ec2 describe-instances --region $region --query 'Reservations[].Instances[].InstanceId' --output text)
fi

if [ -z "$instance_ids" ]; then
  echo "No instances found in the region: $region"
  exit 0
fi

case "$action" in
  "--stop")
    aws ec2 stop-instances --region $region --instance-ids $instance_ids
    echo "Stopping instances: $instance_ids"
    ;;
  "--start")
    aws ec2 start-instances --region $region --instance-ids $instance_ids
    echo "Starting instances: $instance_ids"
    ;;
  "--destroy")
    aws ec2 terminate-instances --region $region --instance-ids $instance_ids
    echo "Destroying instances: $instance_ids"
    ;;
esac
