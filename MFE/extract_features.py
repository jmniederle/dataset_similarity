from pymfe.mfe import MFE
import pandas as pd
from MFE.dataset_preprocessing import dataset_OpenML


def extract_features_OpenML(data_id):
    dat = dataset_OpenML(data_id)
    X, y = dat.get_arrays()
    mfe = MFE()
    mfe.fit(X, y)
    ft = mfe.extract(cat_cols='auto', suppress_warnings=True)
    return dat.name, pd.DataFrame(data=[ft[1]], index=[dat.name], columns=ft[0])