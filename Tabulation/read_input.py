from parameter import parameter
import re
parameter_dict=parameter.parameter_dict
def read_input():
    with open('input.txt','r') as f:
        count=len(f.readlines())
        f.seek(0)
        for i in range(1,count+1):
            line=f.readline()
            find_1=bool(re.match('[\s]*mechanism_file',line))
            find_2=bool(re.match('[\s]*fuel_component',line))
            find_3=bool(re.match('[\s]*oxidizer_component',line))
            find_4=bool(re.match('[\s]*fuel_temperature',line))
            find_5=bool(re.match('[\s]*oxidizer_temperature',line))
            find_6=bool(re.match('[\s]*fuel_mdot',line))
            find_7=bool(re.match('[\s]*oxidizer_mdot',line))
            find_8=bool(re.match('[\s]*operating_pressure',line))
            find_9=bool(re.match('[\s]*primitive_data_path',line))
            find_10=bool(re.match('[\s]*domain_length',line))
            find_11=bool(re.match('[\s]*processed_data_path',line))
            find_12=bool(re.match('[\s]*species_in_table',line))
            find_13=bool(re.match('[\s]*z_mean_resolution',line))
            find_14=bool(re.match('[\s]*c_mean_resolution',line))
            find_15=bool(re.match('[\s]*z_variance_resolution',line))
            find_16=bool(re.match('[\s]*intermediate_table',line))
            find_17=bool(re.match('[\s]*final_table',line))
            find_18=bool(re.match('[\s]*progress_variable',line))
            find_19=bool(re.match('[\s]*transport_model',line))
            # find_19=bool(re.match('[\s]*progress_variable_coef',line))
            if find_1 == True:
                mechanism_file=line.lstrip()
                mechanism_file=mechanism_file.replace('mechanism_file = ','')
                mechanism_file=mechanism_file.rstrip()
                parameter_dict['mechanism_file'] = mechanism_file
            if find_2 == True:
                fuel_component=line.lstrip()
                fuel_component=fuel_component.replace('fuel_component = ','')
                fuel_component=fuel_component.rstrip()
                parameter_dict['fuel_component'] = fuel_component
            if find_3 == True:
                oxidizer_component=line.lstrip()
                oxidizer_component=oxidizer_component.replace('oxidizer_component = ','')
                oxidizer_component=oxidizer_component.rstrip()
                parameter_dict['oxidizer_component'] = oxidizer_component
            if find_4 == True:
                fuel_temperature=line.lstrip()
                fuel_temperature=fuel_temperature.replace('fuel_temperature = ','')
                fuel_temperature=fuel_temperature.rstrip()
                parameter_dict['fuel_temperature'] = float(fuel_temperature)
            if find_5 == True:
                oxidizer_temperature=line.lstrip()
                oxidizer_temperature=oxidizer_temperature.replace('oxidizer_temperature = ','')
                oxidizer_temperature=oxidizer_temperature.rstrip()
                parameter_dict['oxidizer_temperature'] = float(oxidizer_temperature)
            if find_6 == True:
                fuel_mdot=line.lstrip()
                fuel_mdot=fuel_mdot.replace('fuel_mdot = ','')
                fuel_mdot=fuel_mdot.rstrip()
                parameter_dict['fuel_mdot'] = float(fuel_mdot)
            if find_7 == True:
                oxidizer_mdot=line.lstrip()
                oxidizer_mdot=oxidizer_mdot.replace('oxidizer_mdot = ','')
                oxidizer_mdot=oxidizer_mdot.rstrip()
                parameter_dict['oxidizer_mdot'] = float(oxidizer_mdot)
            if find_8 == True:
                operating_pressure=line.lstrip()
                operating_pressure=operating_pressure.replace('operating_pressure = ','')
                operating_pressure=operating_pressure.rstrip()
                parameter_dict['operating_pressure'] = float(operating_pressure)
            if find_9 == True:
                primitive_data_path=line.lstrip()
                primitive_data_path=primitive_data_path.replace('primitive_data_path = ','')
                primitive_data_path=primitive_data_path.rstrip()
                parameter_dict['primitive_data_path'] = primitive_data_path
            if find_10 == True:
                domain_length=line.lstrip()
                domain_length=domain_length.replace('domain_length = ','')
                domain_length=domain_length.rstrip()
                parameter_dict['domain_length'] = float(domain_length)
            if find_11 == True:
                processed_data_path=line.lstrip()
                processed_data_path=processed_data_path.replace('processed_data_path = ','')
                processed_data_path=processed_data_path.rstrip()
                parameter_dict['processed_data_path'] = processed_data_path
            if find_12 == True:
                species_in_table=line.lstrip()
                species_in_table=species_in_table.replace('species_in_table = ','')
                species_in_table=species_in_table.rstrip()
                parameter_dict['species_in_table'] = species_in_table
            if find_13 == True:
                z_mean_resolution=line.lstrip()
                z_mean_resolution=z_mean_resolution.replace('z_mean_resolution = ','')
                z_mean_resolution=z_mean_resolution.rstrip()
                parameter_dict['z_mean_resolution'] = int(z_mean_resolution)
            if find_14 == True:
                c_mean_resolution=line.lstrip()
                c_mean_resolution=c_mean_resolution.replace('c_mean_resolution = ','')
                c_mean_resolution=c_mean_resolution.rstrip()
                parameter_dict['c_mean_resolution'] = int(c_mean_resolution)
            if find_15 == True:
                z_variance_resolution=line.lstrip()
                z_variance_resolution=z_variance_resolution.replace('z_variance_resolution = ','')
                z_variance_resolution=z_variance_resolution.rstrip()
                parameter_dict['z_variance_resolution'] = int(z_variance_resolution)
            if find_16 == True:
                intermediate_table=line.lstrip()
                intermediate_table=intermediate_table.replace('intermediate_table = ','')
                intermediate_table=intermediate_table.rstrip()
                parameter_dict['intermediate_table'] = intermediate_table
            if find_17 == True:
                final_table=line.lstrip()
                final_table=final_table.replace('final_table = ','')
                final_table=final_table.rstrip()
                parameter_dict['final_table'] = final_table
            if find_18 == True:
                progress_variable=line.lstrip()
                progress_variable=progress_variable.replace('progress_variable = ','')
                progress_variable=progress_variable.rstrip()
                parameter_dict['progress_variable'] = progress_variable
            if find_19 == True:
                final_table=line.lstrip()
                final_table=final_table.replace('transport_model = ', '')
                final_table=final_table.rstrip()
                parameter_dict['transport_model'] = final_table
            # if find_19 == True:
            #     progress_variable_coef=line.lstrip()
            #     progress_variable_coef=progress_variable_coef.replace('progress_variable_coef = ','')
            #     progress_variable_coef=progress_variable_coef.rstrip()
            #     parameter_dict['progress_variable_coef'] = progress_variable_coef