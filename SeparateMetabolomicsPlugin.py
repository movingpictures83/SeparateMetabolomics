# Objective:
#   To separate "Users" vs "Non-Users" in Mash-Cohort data (metabolomics data)
import pandas as pd

import PyPluMA
import PyIO

class SeparateMetabolomicsPlugin:
    def input(self, inputfile):
       self.parameters = PyIO.readParameters(inputfile)
    def run(self):
       pass
    def output(self, outputfile):
       abundance_file = PyPluMA.prefix()+"/"+self.parameters["abundance_file"]
       metadata_file = PyPluMA.prefix()+"/"+self.parameters["metadata"]

       #abundance_file = "metabolon_transposed.csv"
       #metadata_file = "metadata.txt"

       out_users = outputfile+"_users.csv"
       out_NonUsers = outputfile+"_nonUsers.csv"
       #out_users = "metabolon_transposed_users.csv"
       #out_NonUsers = "metabolon_transposed_nonUsers.csv"

       metadata_df = pd.read_csv(metadata_file, sep="\t")
       #metadata_df["group"] = metadata_df["COCAINE USE"].apply(lambda x: 1 if x=="Non-User" else 2)
       metadata_df["group"] = metadata_df["COCAINE USE"]

       metadata_df["ClientID"] = metadata_df["CLIENT IDENTIFIER"]
       metadata_df = metadata_df[["group", "ClientID"]]

       df = pd.read_csv(abundance_file, index_col=0)

       df["ClientID"] = df.index
       #  transform sample to match metadata

       df = df.merge(metadata_df, how="left", on="ClientID")
       df.index = df["ClientID"]

       df_users = df[df["group"]=="User"]
       del df_users["group"]
       del df_users["ClientID"]
       df_users.index.names = [""]
       df_users.to_csv(out_users)

       df_non_users = df[df["group"]=="Non-User"]
       del df_non_users["group"]
       del df_non_users["ClientID"]
       df_non_users.index.names = [""]
       df_non_users.to_csv(out_NonUsers)
