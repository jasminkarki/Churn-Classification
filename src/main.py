import os
import pickle
import warnings

import pandas as pd

warnings.filterwarnings('ignore')

MODELPATH = os.path.join('./src/checkpoints', 'model.pkl')
OUTPATH  = os.path.join('./out', 'predictions.csv')


MAPPER = {'yes': 1, 'no': 0}
MODEL  = pickle.load(open(MODELPATH, 'rb'))


def main(data_path):
    df = pd.read_csv(data_path)
    _df = df.copy()

    _df.drop(columns=['Voicemail_Plan', 'Day_Charge', 'Evening_Charge', 'Night_Charge','International_Charge', 'State', 'Phone'], inplace=True)

    _df['International_Plan'] = _df['International_Plan'].apply(lambda x: MAPPER.get(x, x))
    preds = MODEL.predict(_df)
    df['Churn'] = pd.Series(preds)
    df.to_csv(OUTPATH)
    print(f'Prediction saved on {OUTPATH}')



def test_pipeline(data):
    preds = MODEL.predict([data])    
    return "CHURNED" if preds[0] else "NOT CHURNED"


if __name__ == "__main__":
    out = test_pipeline([ 81. ,   0. , 166.2, 217.6, 220.2,  13.2,   4. ,   0. , 102. ,
        112. ,  68. ,   2. , 408. ])
    
    print(out)