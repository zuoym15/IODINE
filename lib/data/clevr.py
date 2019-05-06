from torch.utils.data import Dataset
from torchvision import transforms
from skimage import io
import os
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

class CLEVR(Dataset):
    def __init__(self, root, mode):
        path = os.path.join(root, mode)
        assert os.path.exists(path), 'Path {} does not exist'.format(self.path)
        
        self.img_paths = []
        for file in os.scandir(path):
            path = file.path
            self.img_paths.append(path)
        
    def __getitem__(self, index):
        path = self.img_paths[index]
        img = io.imread(path)[:, :, :3]
        transform = transforms.Compose([
            transforms.ToPILImage(),
            transforms.CenterCrop(192),
            transforms.Resize(32),
            transforms.ToTensor()
        ])
        
        return transform(img)
        
        
    def __len__(self):
        return len(self.img_paths)
    
    
    