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
    """
    Data from Eur.Phys.J.C 46 (2006) 585-603, 2006. 
    """
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
    """
    Data from Nucl.Phys.B 695 (2004) 3-37. 
    """
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

def sigma_tot_Upsilon_H1():
    """
    Data from Phys.Lett.B 483 (2000) 23-35, 2000
    """
    W_values = np.array([143])
    W_values_low = np.array([70])
    W_values_high = np.array([250])
    y_values = np.array([0.55])
    y_errors_stat_minus = np.array([0.28])
    y_errors_stat_plus =  np.array([0.28])
    y_errors_syst_minus = np.array([0.14])
    y_errors_syst_plus =  np.array([0.14])

    return [W_values, W_values_low, W_values_high], [y_values, y_errors_stat_minus, y_errors_syst_minus, y_errors_stat_plus, y_errors_syst_plus]

def sigma_tot_Upsilon_ZEUS_v1():
    """
    Data from Phys.Lett.B 437 (1998) 432-444, 1998
    """
    W_values = np.array([120])
    W_values_low = np.array([80])
    W_values_high =np.array( [160])
    y_values = np.array([0.375])
    y_errors_stat_minus = np.array([0.170])
    y_errors_stat_plus =  np.array([0.170])
    y_errors_syst_plus =  np.array([0.075])
    y_errors_syst_minus = np.array( [0.064])

    return [W_values, W_values_low, W_values_high], [y_values, y_errors_stat_minus, y_errors_syst_minus, y_errors_stat_plus, y_errors_syst_plus]

def sigma_tot_Upsilon_ZEUS_v2():
    """
    Data from Phys.Lett.B 680 (2009) 4-12
    """
    W_values_low = np.array([60, 130])
    W_values_high =np.array( [130, 220])
    W_values = (W_values_high + W_values_low)/2
    y_values = np.array([160, 321])
    y_errors_stat_minus = np.array([51, 88])
    y_errors_stat_plus =  np.array([51, 88])
    y_errors_syst_plus =  np.array([48,46])
    y_errors_syst_minus = np.array( [21,114])

    return [W_values, W_values_low, W_values_high], [y_values, y_errors_stat_minus, y_errors_syst_minus, y_errors_stat_plus, y_errors_syst_plus]

def sigma_tot_Upsilon_CMS():
    """
    Data from Eur.Phys.J.C 79 (2019) 3, 277
    """
    W_values_low = np.array([91, 194, 275, 390])
    W_values_high =np.array( [194, 275, 390, 826])
    W_values = np.array([133, 231, 328, 568])
    y_values = np.array([0.208, 0.343, 0.663, 0.956])
    y_errors_stat_minus = np.array([0.96, 0.180, 0.260, 0.376])
    y_errors_stat_plus =  np.array([0.96, 0.180, 0.260, 0.376])
    y_errors_syst_plus =  np.array([0.37, 0.51, 0.93, 0.162])
    y_errors_syst_minus = np.array([0.37, 0.51, 0.93, 0.162])

    return [W_values, W_values_low, W_values_high], [y_values, y_errors_stat_minus, y_errors_syst_minus, y_errors_stat_plus, y_errors_syst_plus]

