# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 09:29:51 2020

@author: mhiyer

Given Singapore postal codes, map them to one of five regions- North, South, East, West and North-East
This code uses pandas to read in data, and uses a mapping datafile that maps postal codes to regions

"""

import pandas as pd

# get a dictionary that contains the relationship between region and postal codes
# input is a pandas dataframe, and the names of the columns containing the 
# first 'n' digits of the postal codes and the region, respectively

def get_region_dict(df, postal_code_column_name, region_column_name):
    # initialize dictionary
    r_dict={}
    
    # loop through the postal_code_column and map them to the appropriate region
    postal_code_column = df[postal_code_column_name].astype('str')
    region_column = df[region_column_name]
    
    for i,code in enumerate(postal_code_column):
        # split codes based on delimiter
        split_codes = [x.strip() for x in code.split(',')]
        # get current region
        region = region_column[i]
        # update dictionary
        if region not in r_dict.keys():
            r_dict[region]=split_codes
        else:
            r_dict[region]+=split_codes
    return r_dict
    
# main routine
if __name__ == "__main__":
    
    # input parameters
    
    # data containing mapped zip codes and regions
    zip_code_map_data_pathname = r'postal_code_information.xlsx'
    zip_code_sheet_name = 'Sheet1'

    # original data- which requires the postal codes to be mapped to a region
    input_data_pathname = r'sgo-satellite-offices\sgo-satellite-offices.xlsx'
    input_data_sheet_name = 'sgo-satellite-offices'

    # read postal code to region data- change the input file accordingly
    df_zip = pd.read_excel(zip_code_map_data_pathname, sheet_name = zip_code_sheet_name)
    
    # create a dictionary that maps postal code to regions (regions are the keys)
    # input df_zip and the column names that contain the postal codes and regions respectively
    region_dict = get_region_dict(df_zip, 'Postal Code', 'Region')
 
    # read in input data containing a column with postal code
    df_orig_data = pd.read_excel(input_data_pathname, sheet_name = input_data_sheet_name)
    
    # specify the names of the column containing the postal code information
    postal_code_column_name = 'postal_code'
    
    # extract pandas series containing the postal code data- convert to 'str'
    df_postal_codes = df_orig_data[postal_code_column_name].astype('str')
    
    # get the first two digits of the postal codes
    df_trimmed_postal_codes = [x[0:2] for x in df_postal_codes]
    
    # loop through the column, and get regions
    regions = []
    for tpc in df_trimmed_postal_codes:
        region = ''
        for key in region_dict.keys():
            if tpc in region_dict[key]:
                region = key
        regions.append(region)
    
    # add a new column to the original data containing the regions derived
    df_orig_data['Region'] = regions
    
    # save as excel
    df_orig_data.to_excel(input_data_pathname.split('.')[0]+'_mapped_regions.xlsx', sheet_name = input_data_sheet_name, index=False)
 
  