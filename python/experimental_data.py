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