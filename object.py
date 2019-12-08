class Dataset(object):
    def __init__(self, data=None):
        self.data = data
class MRIDataset(Dataset):
    def __init__(self, data=None, parameters=None):
# here has the same effect as calling
# Dataset.__init__(self)
        super(MRIDataset, self).__init__(data)
        self.parameters = parameters


mri_data = MRIDataset(data=[1,2,3])
print(mri_data.data, mri_data.parameters)
