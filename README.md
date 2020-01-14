# map_singapore_postal_codes_to_regions
Given Singapore postal codes, map them to one of five regions - North, Central, East, West and North-East

Inputs:
1) An excel sheet that contains the mapping between postal codes and regions. I used this website:
https://www.iproperty.com.sg/news/know-which-district-you-are-in-based-on-postal-code/

I converted this information to an excel sheet: 'postal_code_information.xlsx'

2) Data that contains a column with postal codes: This needs to be an excel worksheet. For CSVs, you may make the desired modifications to the code.

Outputs:
1) An extra column 'Regions', will be added to this data. This will be saved as an excel worksheet, in the same folder as your input data, with the same sheet_name. The only change is that a '_mapped_regions' is added to the name of the file.

To view sample input and output, please navigate to the 'sgo-satellite-offices' folder. This data was obtained from:
https://data.gov.sg/dataset/sgo-satellite-offices
