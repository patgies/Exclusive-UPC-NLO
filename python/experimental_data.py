import yaml
import os 
import matplotlib.pyplot as plt
import numpy as np

dir_path = os.path.dirname(os.path.realpath(__file__)) + r'/experimental_data/'



def err_plus(err_dict):
    if 'symerror' in err_dict:
        return err_dict['symerror']
    elif 'asymerror' in err_dict:
        return err_dict['asymerror']['plus']
    else:
        return 0

def err_minus(err_dict):
    if 'symerror' in err_dict:
        return err_dict['symerror']
    elif 'asymerror' in err_dict:
        return err_dict['asymerror']['minus']
    else:
        return 0


def R_Q2_ZEUS():
    """
    Data from Nucl.Phys.B 695 (2004) 3-37. 
    """
    file_yaml = dir_path + r'HEPData-ins647777-v1-Table_18.yaml'
    with open(file_yaml) as file:
        yaml_list = yaml.load(file, Loader=yaml.FullLoader)

    ind = yaml_list['independent_variables'][0]
    ind_values_list = ind['values']
    Q_values = np.array([x['value'] for x in ind_values_list])
    Q_values_high = np.array([x['high'] for x in ind_values_list])
    Q_values_low = np.array([x['low'] for x in ind_values_list])

    dep = yaml_list['dependent_variables'][2]
    dep_values_list = dep['values']
    y_values = np.array([x['value'] for x in dep_values_list] )
    y_values_stat = [x['errors'][0] for x in dep_values_list] 
    y_values_syst = [x['errors'][1] for x in dep_values_list] 
    y_errors_stat_plus = np.abs(np.array([err_plus(x) for x in y_values_stat]))
    y_errors_syst_plus = np.abs(np.array([err_plus(x) for x in y_values_syst]))
    y_errors_stat_minus = np.abs(np.array([err_minus(x) for x in y_values_stat]))
    y_errors_syst_minus = np.abs(np.array([err_minus(x) for x in y_values_syst]))

    return [Q_values, Q_values_low, Q_values_high], [y_values, y_errors_stat_minus, y_errors_syst_minus, y_errors_stat_plus, y_errors_syst_plus]



def R_Q2_H1():
    """
    Data from Eur.Phys.J.C 46 (2006) 585-603, 2006. 
    """
    file_yaml = dir_path + r'HEPData-ins694372-v1-Table_15.yaml'
    with open(file_yaml) as file:
        yaml_list = yaml.load(file, Loader=yaml.FullLoader)

    ind = yaml_list['independent_variables'][0]
    ind_values_list = ind['values']
    Q_values = np.array([x['value'] for x in ind_values_list])
    Q_values_high = np.array([x['high'] for x in ind_values_list])
    Q_values_low = np.array([x['low'] for x in ind_values_list])

    dep = yaml_list['dependent_variables'][2]
    dep_values_list = dep['values']
    y_values = np.array([x['value'] for x in dep_values_list])
    y_values_stat = [x['errors'][0] for x in dep_values_list] 
    y_values_syst = [x['errors'][1] for x in dep_values_list] 
    y_errors_stat_plus = np.abs(np.array([err_plus(x) for x in y_values_stat]))
    y_errors_syst_plus = np.abs(np.array([err_plus(x) for x in y_values_syst]))
    y_errors_stat_minus = np.abs(np.array([err_minus(x) for x in y_values_stat]))
    y_errors_syst_minus = np.abs(np.array([err_minus(x) for x in y_values_syst]))

    return [Q_values, Q_values_low, Q_values_high], [y_values, y_errors_stat_minus, y_errors_syst_minus, y_errors_stat_plus, y_errors_syst_plus]


def sigma_tot_W_H1_v1():
    """
    Data from Eur.Phys.J.C 46 (2006) 585-603, 2006. 
    """
    file_yaml = dir_path + r'HEPData-ins694372-v1-Table_2.yaml'
    with open(file_yaml) as file:
        yaml_list = yaml.load(file, Loader=yaml.FullLoader)

    ind = yaml_list['independent_variables'][0]
    ind_values_list = ind['values']
    W_values_high = np.array([x['high'] for x in ind_values_list])
    W_values_low = np.array([x['low'] for x in ind_values_list])
    W_values = np.zeros(  len(W_values_high) )
    for idx, ind_value in enumerate(ind_values_list):
        try:
            W_values[idx] = ind_value['value']
        except KeyError:
            W_values[idx] = (W_values_high[idx] + W_values_low[idx])/2 # half-point if there is no value given


    dep = yaml_list['dependent_variables'][0]
    dep_values_list = dep['values']
    y_values = np.array([x['value'] for x in dep_values_list])
    y_values_stat = [x['errors'][0] for x in dep_values_list] 
    y_values_syst = [x['errors'][1] for x in dep_values_list] 
    y_errors_stat_plus = np.abs(np.array([err_plus(x) for x in y_values_stat]))
    y_errors_syst_plus = np.abs(np.array([err_plus(x) for x in y_values_syst]))
    y_errors_stat_minus = np.abs(np.array([err_minus(x) for x in y_values_stat]))
    y_errors_syst_minus = np.abs(np.array([err_minus(x) for x in y_values_syst]))

    Q2s = dep['qualifiers'][1]['value']

    return [W_values, W_values_low, W_values_high], [y_values, y_errors_stat_minus, y_errors_syst_minus, y_errors_stat_plus, y_errors_syst_plus], Q2s


def sigma_tot_Q2_H1():
    file_yaml = dir_path + r'HEPData-ins694372-v1-Table_1.yaml'
    with open(file_yaml) as file:
        yaml_list = yaml.load(file, Loader=yaml.FullLoader)

    ind = yaml_list['independent_variables'][0]
    ind_values_list = ind['values']
    Q_values = np.array([x['value'] for x in ind_values_list])
    Q_values_high = np.array([x['high'] for x in ind_values_list])
    Q_values_low = np.array([x['low'] for x in ind_values_list])

    dep = yaml_list['dependent_variables'][0]
    dep_values_list = dep['values']
    y_values = np.array([x['value'] for x in dep_values_list])
    y_values_stat = [x['errors'][0] for x in dep_values_list] 
    y_values_syst = [x['errors'][1] for x in dep_values_list] 
    y_errors_stat_plus = np.abs(np.array([err_plus(x) for x in y_values_stat]))
    y_errors_syst_plus = np.abs(np.array([err_plus(x) for x in y_values_syst]))
    y_errors_stat_minus = np.abs(np.array([err_minus(x) for x in y_values_stat]))
    y_errors_syst_minus = np.abs(np.array([err_minus(x) for x in y_values_syst]))

    return [Q_values, Q_values_low, Q_values_high], [y_values, y_errors_stat_minus, y_errors_syst_minus, y_errors_stat_plus, y_errors_syst_plus]

def sigma_tot_Q2_ZEUS():
    file_yaml = dir_path + r'HEPData-ins647777-v1-Table_10.yaml'
    with open(file_yaml) as file:
        yaml_list = yaml.load(file, Loader=yaml.FullLoader)

    ind = yaml_list['independent_variables'][0]
    ind_values_list = ind['values']
    Q_values = np.array([x['value'] for x in ind_values_list])
    Q_values_high = np.array([x['high'] for x in ind_values_list])
    Q_values_low = np.array([x['low'] for x in ind_values_list])

    dep = yaml_list['dependent_variables'][0]
    dep_values_list = dep['values']
    y_values = np.array([x['value'] for x in dep_values_list])
    y_values_stat = [x['errors'][0] for x in dep_values_list] 
    y_values_syst = [x['errors'][1] for x in dep_values_list] 
    y_errors_stat_plus = np.abs(np.array([err_plus(x) for x in y_values_stat]))
    y_errors_syst_plus = np.abs(np.array([err_plus(x) for x in y_values_syst]))
    y_errors_stat_minus = np.abs(np.array([err_minus(x) for x in y_values_stat]))
    y_errors_syst_minus = np.abs(np.array([err_minus(x) for x in y_values_syst]))

    return [Q_values, Q_values_low, Q_values_high], [y_values, y_errors_stat_minus, y_errors_syst_minus, y_errors_stat_plus, y_errors_syst_plus]





def sigma_tot_W_H1_v2():
    """
    Data from Eur.Phys.J.C 73 (2013) 2466, 2013.
    """
    file_yaml = dir_path + r'HEPData-ins1228913-v1-Table_1.yaml'
    with open(file_yaml) as file:
        yaml_list = yaml.load(file, Loader=yaml.FullLoader)

    ind = yaml_list['independent_variables'][0]
    ind_values_list = ind['values']
    W_values_high = np.array([x['high'] for x in ind_values_list])
    W_values_low = np.array([x['low'] for x in ind_values_list])
    W_values = np.zeros( len(W_values_high) )
    for idx, ind_value in enumerate(ind_values_list):
        try:
            W_values[idx] = ind_value['value']
        except KeyError:
            W_values[idx] = (W_values_high[idx] + W_values_low[idx])/2 # half-point if there is no value given


    dep = yaml_list['dependent_variables'][0]
    dep_values_list = dep['values']
    y_values = np.array([x['value'] for x in dep_values_list])
    y_errors = [x['errors'][0] for x in dep_values_list] 
    y_errors_plus = np.abs(np.array([err_plus(x) for x in y_errors]))
    y_errors_minus = np.abs(np.array([err_minus(x) for x in y_errors]))

    return [W_values, W_values_low, W_values_high], [y_values, y_errors_minus, y_errors_plus]



def sigma_tot_W_ALICE_v1():
    """
    Data from Phys.Rev.Lett. 113 (2014) 232504, 2014.
    """
    file_yaml = dir_path + r'HEPData-ins1303903-v1-Table_1.yaml'
    with open(file_yaml) as file:
        yaml_list = yaml.load(file, Loader=yaml.FullLoader)

    ind = yaml_list['independent_variables'][1]
    ind_values_list = ind['values']
    W_values = np.array([x['value'] for x in ind_values_list])
    W_values_high = np.array([x['high'] for x in ind_values_list])
    W_values_low = np.array([x['low'] for x in ind_values_list])

    dep = yaml_list['dependent_variables'][2]
    dep_values_list = dep['values']
    y_values = np.array([x['value'] for x in dep_values_list])
    y_values_stat = [x['errors'][0] for x in dep_values_list] 
    y_values_syst = [x['errors'][1] for x in dep_values_list] 
    y_values_theo = [x['errors'][2] for x in dep_values_list] 
    y_errors_stat_plus = np.abs(np.array([err_plus(x) for x in y_values_stat]))
    y_errors_syst_plus = np.abs(np.array([err_plus(x) for x in y_values_syst]))
    y_errors_theo_plus = np.abs(np.array([err_plus(x) for x in y_values_theo]))
    y_errors_stat_minus = np.abs(np.array([err_minus(x) for x in y_values_stat]))
    y_errors_syst_minus = np.abs(np.array([err_minus(x) for x in y_values_syst]))
    y_errors_theo_minus = np.abs(np.array([err_minus(x) for x in y_values_theo]))

    return [W_values, W_values_low, W_values_high], [y_values, y_errors_stat_minus, y_errors_syst_minus, y_errors_theo_minus, y_errors_stat_plus, y_errors_syst_plus, y_errors_theo_plus]



def sigma_tot_W_ALICE_v2():
    """
    Data from Phys.Rev.Lett. 113 (2014) 232504, 2014.
    """
    file_yaml = dir_path + r'HEPData-ins1303903-v1-Table_2.yaml'
    with open(file_yaml) as file:
        yaml_list = yaml.load(file, Loader=yaml.FullLoader)

    ind = yaml_list['independent_variables'][1]
    ind_values_list = ind['values']
    W_values = np.array([x['value'] for x in ind_values_list])
    W_values_high = np.array([x['high'] for x in ind_values_list])
    W_values_low = np.array([x['low'] for x in ind_values_list])

    dep = yaml_list['dependent_variables'][2]
    dep_values_list = dep['values']
    y_values = np.array([x['value'] for x in dep_values_list])
    y_values_stat = [x['errors'][0] for x in dep_values_list] 
    y_values_syst = [x['errors'][1] for x in dep_values_list] 
    y_values_theo = [x['errors'][2] for x in dep_values_list] 
    y_errors_stat_plus = np.abs(np.array([err_plus(x) for x in y_values_stat]))
    y_errors_syst_plus = np.abs(np.array([err_plus(x) for x in y_values_syst]))
    y_errors_theo_plus = np.abs(np.array([err_plus(x) for x in y_values_theo]))
    y_errors_stat_minus = np.abs(np.array([err_minus(x) for x in y_values_stat]))
    y_errors_syst_minus = np.abs(np.array([err_minus(x) for x in y_values_syst]))
    y_errors_theo_minus = np.abs(np.array([err_minus(x) for x in y_values_theo]))

    return [W_values, W_values_low, W_values_high], [y_values, y_errors_stat_minus, y_errors_syst_minus, y_errors_theo_minus, y_errors_stat_plus, y_errors_syst_plus, y_errors_theo_plus]



def sigma_tot_W_ALICE_v3():
    """
    Data from Eur.Phys.J.C 79 (2019) 402, 2019. 
    """
    file_yaml = dir_path + r'HEPData-ins1693305-v1-Table_1.yaml'
    with open(file_yaml) as file:
        yaml_list = yaml.load(file, Loader=yaml.FullLoader)

    ind = yaml_list['independent_variables'][1]
    ind_values_list = ind['values']
    W_values = np.array([x['value'] for x in ind_values_list])
    W_values_high = np.array([x['high'] for x in ind_values_list])
    W_values_low = np.array([x['low'] for x in ind_values_list])

    dep = yaml_list['dependent_variables'][2]
    dep_values_list = dep['values']
    y_values = np.array([x['value'] for x in dep_values_list])
    y_values_stat = [x['errors'][0] for x in dep_values_list] 
    y_values_syst = [x['errors'][1] for x in dep_values_list] 
    y_values_theo = [x['errors'][2] for x in dep_values_list] 
    y_errors_stat_plus = np.abs(np.array([err_plus(x) for x in y_values_stat]))
    y_errors_syst_plus = np.abs(np.array([err_plus(x) for x in y_values_syst]))
    y_errors_theo_plus = np.abs(np.array([err_plus(x) for x in y_values_theo]))
    y_errors_stat_minus = np.abs(np.array([err_minus(x) for x in y_values_stat]))
    y_errors_syst_minus = np.abs(np.array([err_minus(x) for x in y_values_syst]))
    y_errors_theo_minus = np.abs(np.array([err_minus(x) for x in y_values_theo]))

    return [W_values, W_values_low, W_values_high], [y_values, y_errors_stat_minus, y_errors_syst_minus, y_errors_theo_minus, y_errors_stat_plus, y_errors_syst_plus, y_errors_theo_plus]




def sigma_tot_W_ZEUS():
    """
    Data from Eur.Phys.J.C 24 (2002) 345-360, 2002. 
    """
    file_yaml = dir_path + r'HEPData-ins582237-v1-Table_2.yaml'
    with open(file_yaml) as file:
        yaml_list = yaml.load(file, Loader=yaml.FullLoader)

    ind = yaml_list['independent_variables'][0]
    ind_values_list = ind['values']
    W_values_high = np.array([x['high'] for x in ind_values_list])
    W_values_low = np.array([x['low'] for x in ind_values_list])
    W_values = np.zeros(  len(W_values_high) )
    for idx, ind_value in enumerate(ind_values_list):
        try:
            W_values[idx] = ind_value['value']
        except KeyError:
            W_values[idx] = (W_values_high[idx] + W_values_low[idx])/2 # half-point if there is no value given


    dep = yaml_list['dependent_variables'][0]
    dep_values_list = dep['values']
    y_values = np.array([x['value'] for x in dep_values_list])
    # y_errors = [x['errors'][0] for x in dep_values_list] 
    # y_errors_plus = np.abs(np.array([err_plus(x) for x in y_errors]))
    # y_errors_minus = np.abs(np.array([err_minus(x) for x in y_errors]))
    y_values_stat = [x['errors'][0] for x in dep_values_list] 
    y_values_syst = [x['errors'][1] for x in dep_values_list] 
    y_errors_stat_plus = np.abs(np.array([err_plus(x) for x in y_values_stat]))
    y_errors_syst_plus = np.abs(np.array([err_plus(x) for x in y_values_syst]))
    y_errors_stat_minus = np.abs(np.array([err_minus(x) for x in y_values_stat]))
    y_errors_syst_minus = np.abs(np.array([err_minus(x) for x in y_values_syst]))

    # return [W_values, W_values_low, W_values_high], [y_values, y_errors_minus, y_errors_plus]
    return [W_values, W_values_low, W_values_high], [y_values, y_errors_stat_minus, y_errors_syst_minus, y_errors_stat_plus, y_errors_syst_plus]

