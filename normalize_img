import os
import random

import numpy as np
import torchvision.datasets as D
import torchvision.transforms as T
from torch.utils.data import DataLoader, Subset
import torch

data = 'AwA2'
data_dir = 'D:/data/'
save_dir = 'D:/cifar100_AwA2/'

def get_img_mean(Dataset):
    loader = DataLoader(
        Dataset,
        batch_size=1000, num_workers=0, shuffle=False
    )

    mean = torch.zeros(3)
    mean2 = torch.zeros(3)
    total = torch.zeros(1)
    print('--> get mean&stdv of images')
    for data, _ in loader:
        mean += torch.sum(data, dim=(0, 2, 3), keepdim=False)
        mean2 += torch.sum((data ** 2), dim=(0, 2, 3), keepdim=False)
        total += data.size(0)

    total *= (data.size(2) ** 2)
    mean /= total
    std = torch.sqrt((mean2 - total * (mean ** 2)) / (total - 1))

    mean = list(np.around(mean.numpy(), 4))
    std = list(np.around(std.numpy(), 4))
    return mean, std
