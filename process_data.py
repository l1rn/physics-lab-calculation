import pandas as pd
import numpy as np

BETA = 0.51
TETA_TIME = 0.01
TETA_S = 0.002
TETA_ALPHA = 2.5
N_CONST = 5
G_CONST = 9.8
S_CONST = 0.522

class ProcessDataClass:
    def __init__(self, csv_path: 'duraliminiy.csv'):
        self.df = pd.read_csv(csv_path)

    def print_raw(self):
        print(self.df.head())
    
    def preprocess(self):
        df = self.df.copy()
        df['time_avg'] = (
            df.groupby('alpha')['time'].transform('sum') / 5
        )

        df['R_t'] = df.groupby('alpha')['time'].transform(lambda s: s.max() - s.min())
        df['delta_t'] = BETA * df['R_t']
        df['delta_t_avg'] = (
            np.sqrt(pow(df['delta_t'], 2) + pow(TETA_TIME, 2))
        )
        alpha_rad = np.radians(df['alpha'])
        delta_alpha_rad = np.radians(TETA_ALPHA)
        df['mu'] = (
            np.tan(alpha_rad)
            - (2 * S_CONST) / (G_CONST * df['time_avg']**2 * np.cos(alpha_rad))
        )

        term1 = (
                (1 - (2 * S_CONST * np.sin(alpha_rad)) 
                 / (G_CONST * df['time_avg']**2))
                * (delta_alpha_rad / np.cos(alpha_rad))
                )**2

        term2 = (
                (4 * S_CONST * df['delta_t_avg']) 
                / (G_CONST * df['time_avg']**3)
                )**2

        term3 = (
                (2 * TETA_S)
                / (G_CONST * df['time_avg']**2)
                )**2


        df['mu_err'] = (1 / np.cos(alpha_rad)) * np.sqrt(term1 + term2 + term3)
        print(df['mu_err'])

        self.df = df
    def print_preprocessed(self):
        print(self.df)

