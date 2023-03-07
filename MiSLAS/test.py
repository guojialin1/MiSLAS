# import logging
# logging.basicConfig(filename='/home/gjl/LOG.log',level = logging.DEBUG,filemode='a',
#                     format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# a = 1
# logging.error(a)
# logging.info("这是一条info信息的打印")
# logging.warning("这是一条warn信息的打印")
# logging.debug("这是一条debug信息的打印")

# import argparse

# parser = argparse.ArgumentParser(description='test')

# parser.add_argument('--sparse', action='store_true', default=False, help='GAT with sparse version or not.')
# parser.add_argument('--seed', type=int, default=72, help='Random seed.')
# parser.add_argument('--epochs', type=int, default=10000, help='Number of epochs to train.')

# args = parser.parse_args()
# print(args.sparse)
# print(args.seed)
# print(args.epochs)

# import torch
# flag = torch.cuda.is_available()
# print(flag)
# ngpu= 1
# # Decide which device we want to run on
# device = torch.device("cuda:0" if (torch.cuda.is_available() and ngpu > 0) else "cpu")
# print(device)
# print(torch.cuda.get_device_name(0))
# print(torch.rand(3,3).cuda())

# import torch
# import time
# import os
# os.environ['CUDA_VISIBLE_DEVICES']='0'
# print(torch.__version__)
# print(torch.version.cuda)
# print(torch.cuda.is_available())



# dsets = []
# config = {}
# print(type(config))
# config['a'] = 1
# config["a"]["b"] = 1
# print(config["a"]["b"])
# print(config['a'])s
# config['a']['b'] = 2
# print(config['a']['b'])
# config = {}
# config["prep"] = {"test_10crop":True, 'params':{"resize_size":256, "crop_size":224, 'alexnet':False}}
# print(config["prep"]['params']['crop_size'])
# print(type(config["prep"]))
# print(type(config["prep"]['params']))
# print(type(config["prep"]['params']['crop_size']))