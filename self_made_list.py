import torch

def data_sampler(true_list, false_list):

    true_labels = torch.ones(32)
    false_labels = torch.zeros(32)

    input_data = torch.cat((torch.Tensor(true_list),torch.Tensor(false_list)),dim=0)
    labels = torch.cat((torch.Tensor(true_labels), torch.Tensor(false_labels)),dim=0)
    return input_data.view(-1,3), labels.view(-1, 1)