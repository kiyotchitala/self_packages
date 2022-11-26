import torch
import glob

def data_sampler(path_1, path_2):
    #path_2 = r'C:\Users\wtana\Desktop\LiDAR_cm\syoumen\kaneko\200cm\txt\*'
    true_files = glob.glob(path_1)
    false_files = glob.glob(path_2)
    
    len_true = len(true_files)
    len_false = len(false_files)
    if len_true == 0 or len_false == 0:
        print('No data available')
        return 0,0

    true_list = []
    false_list = []

    for idx in range(64*2):
        s_num = []
        with open(true_files[idx],'r') as f:
            data = f.read().split('\n')
            for i in range(len(data)-1):
                s = data[i].split(' ')
                s_num.append([float(s[0]),float(s[1]),float(s[2])])
        true_list.append([s_num])

    for idx in range(64*2):
        s_num = []
        with open(false_files[idx],'r') as f:
            data = f.read().split('\n')
            for i in range(len(data)-1):
                s = data[i].split(' ')
                s_num.append([float(s[0]),float(s[1]),float(s[2])])
        false_list.append([s_num])
    #len_true = len(true_list)
    #len_false = len(false_list)

    true_labels = torch.ones(32*2)
    false_labels = torch.zeros(32*2)

    input_data = torch.cat((torch.Tensor(true_list),torch.Tensor(false_list)),dim=0)
    labels = torch.cat((torch.Tensor(true_labels), torch.Tensor(false_labels)),dim=0)
    return input_data.view(-1,3), labels.view(-1, 1)