import pandas as pd

  #general info dataframe 
def general_info(general_info_list):
    from pathlib import Path
    my_file=Path("../Project_3_Swapout/csv_data/general_info.csv")
    if my_file ==True:
        general_info_df=pd.read_csv(my_file)
        general_info_df.append(general_info_list)
    else:
      
        #create empty general_info_df
        general_info_df = pd.DataFrame(columns=[
            "first_name", 
            "last_name", 
            "email", 
            "year", 
            "make", 
            "model", 
            "miles", 
            "certificate"
            ])
        #set Path
        Path = ("../Project_3_Swapout/csv_data/general_info.csv")
        #creat empty general_info csv
        general_info_df.to_csv(Path)

#private info dataframe
def private_info(private_info_list):
    my_file="../Project_3_Swapout/csv_data/private_info.csv"
    if my_file.exist():
        private_info_df=pd.read_csv(my_file)
        private_info_df.append(private_info_list)
    else:
        #create empty private_info_df
        private_info_df = pd.DataFrame(columns=[
            "digital_address", 
            "account_password", 
            "mailing_address"
            ])
        #set Path
        Path = ("../Project_3_Swapout/csv_data/private_info.csv")
        private_info_df.to_csv(Path)

general_info([1,2,3,4,5,6,7,8,9])