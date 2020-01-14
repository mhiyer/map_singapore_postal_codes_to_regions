# map_singapore_postal_codes_to_regions
Given Singapore postal codes, map them to one of five regions - North, South, East, West and North-East

Inputs:
1) An excel sheet that contains the mapping between postal codes and regions. I used this website:
https://www.iproperty.com.sg/news/know-which-district-you-are-in-based-on-postal-code/

I converted this information to an excel sheet

2) Data that contains a column with postal codes: This needs to be an excel worksheet. For CSVs, you may make the desired modifications to the code.

Outputs:
1) An extra column 'Regions', will be added to this data. This will be saved as an excel worksheet, in the same folder as your input data, with the same sheet_name. The only change is that a '_mapped_regions' is added to the name of the file.
