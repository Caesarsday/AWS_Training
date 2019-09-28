import boto3
from boto3.session import Session
import sys
import os
import time
##build connection through access_key_id, secret_access_key and region_name
def get_ec2_con_for_give_region(my_region,session):
    ec2_con_re=session.resource('ec2',region_name=my_region)
    return ec2_con_re
##list all instance ids
def list_instance_on_my_region(ec2_con_re):
    for each in ec2_con_re.instances.all():
        print(each.id)
##show selected instance statement
def get_instant_state(ec2_con_re, in_id):
    for each in ec2_con_re.instances.filter(Filters=[{'Name':'instance-id','Values':[in_id]}]):
        pr_st=each.state['Name']
        return pr_st
##launch instance
def start_instance(ec2_con_re,in_id):
    pr_st =get_instant_state(ec2_con_re,in_id)
    if pr_st =='running':
        print ("instance is already running")
    else:
        for each in ec2_con_re.instances.filter(Filters=[{'Name':'instance-id','Values':[in_id]}]):
            each.start()
            print("please wait, the instance is going to start, once it is started we will let you know")
            each.wait_until_running()
            print("now it is running")
    return

def thanks_you():
    print("\n\n*********Thank you for using this script*********")
    return None
##terminate instance
def stop_instance(ec2_con_re, in_id):
    pr_st =get_instant_state(ec2_con_re,in_id)
    if pr_st =='stopped':
        print("instance is already stopped")
    else:
        for each in ec2_con_re.instances.filter(Filters=[{'Name':'instance-id','Values':[in_id]}]):
            each.stop()
            print("please wait, the instance is going to stop, once it is stopped we will let you know")
            each.wait_until_stopped()
            print("now it is stopped")

def welcome():
    print("This script will show how to launch or terminate ec2 instance based on your required region and instance id")
    print("Enjoy using this script\n\n")
    time.sleep(3)

def main():
    welcome()
    my_region=input("Enter your region name:")
    print("Please wait ... connecting to your aws ec2 console ...")
    aws_key = "AKIAIWXAKHINHFMSA7ZQ"
    aws_secret = "uM+5dRcwltvlvw/1uGK3ERLdizQMSg4RLBfjbEyN"
    session = Session(aws_access_key_id=aws_key, aws_secret_access_key=aws_secret)
    ec2_con_re=get_ec2_con_for_give_region(my_region,session)
    print("Please wait listing all instance ids in your region{}".format(my_region))
    list_instance_on_my_region(ec2_con_re)
    in_id=input("Now choose your instance id to start or stop:")
    start_stop=input("Enter either stop or start command for your ec2 instance:")
    while True:
        if start_stop not in ['start',"stop"]:
            start_stop=input("Please Only enter start or stop:")
            continue
        else:
            break
    if start_stop=='start':
        start_instance(ec2_con_re, in_id)
    else:
        stop_instance(ec2_con_re,in_id)
    thanks_you()

if __name__=='__main__':
    os.system('cls')
    main()