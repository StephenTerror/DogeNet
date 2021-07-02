from torchvision import datasets
from torchvision.transforms import transforms
from core.datasets.transformer.custom_transform import *


normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])


def classify_train_dataset(data_dir, transform=MNISTTrainTransform, **kwargs):
    return datasets.FashionMNIST(root=data_dir, train=True, transform=transform, **kwargs)


# val dataset example for tiny-image-net
def classify_val_dataset(data_dir, transform=MNISTValidationTransform, **kwargs):
    return datasets.FashionMNIST(root=data_dir, train=False, transform=transform, **kwargs)


# test dataset example for tiny-image-net
def classify_test_dataset(data_dir, transform=MNISTTestTransform, **kwargs):
    return datasets.FashionMNIST(root=data_dir, train=False, transform=transform, **kwargs)
