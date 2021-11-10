# The similarity function will be placed here to determine which cars will be conisdered when generating
# aggregate data
from numpy.linalg import norm
import numpy as np


def cos_sim_function(a, b):
    """simple cos similarity function"""

    cos_sim = np.dot(a, b) / (norm(a) * norm(b))
    return cos_sim


def pipeline_model(df, obs):
    """Model to generate on the spot """
    df_c = df.copy()
    for x in obs.columns:
        df_c = df_c.loc[df_c[x] == obs[x][0]]

    return df_c
