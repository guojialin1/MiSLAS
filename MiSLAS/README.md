**Introduction**: This repository provides an implementation for the CVPR 2021 paper: "[Improving Calibration for Long-Tailed Recognition](https://arxiv.org/pdf/2104.00466.pdf)" based on [LDAM-DRW](https://github.com/kaidic/LDAM-DRW) and [Decoupling models](https://github.com/facebookresearch/classifier-balancing). *Our study shows, because of the extreme imbalanced composition ratio of each class, networks trained on long-tailed datasets are more miscalibrated and over-confident*. MiSLAS is a simple, and efficient two-stage framework for long-tailed recognition, which greatly improves recognition accuracy and markedly relieves over-confidence simultaneously.

## Installation

**Requirements**

* Python 3.7
* torchvision 0.4.0
* Pytorch 1.2.0
* yacs 0.1.8


## Training

**Stage-1**:

To train a model for Stage-1 with *mixup*, run:
python train_stage1.py --cfg /home/gjl/MiSLAS/config/cifar10/cifar10_imb01_stage1_mixup.yaml

**Stage-2**:

To train a model for Stage-2 with *one GPU* (all the above datasets), run:
python train_stage2.py --cfg /home/gjl/MiSLAS/config/cifar10/cifar10_imb01_stage2_mislas.yaml resume /home/gjl/MiSLAS/saved/cifar10_imb01_stage1_mixup_202203271742/ckps/model_best.pth.tar
