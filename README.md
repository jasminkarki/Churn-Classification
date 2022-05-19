# Churn Prediction

## Important Guidelines

1. Always run the app from project root directory
2. Store test datasets on `data` directory (Note: Should be in `.csv` format)

## Run

```
pip install -r requirements.txt
```

```bash

python run.py --data "path_to_dataset.csv"
```

example:

```bash
python run.py --data "./data/data.csv"
```

## Output

Given features

```
Account_Length, Voicemail_Message, Day_Minutes, Evening_Minutes, Night_Minutes,International_Minutes,CustomerService_Calls, International_Plan, Voicemail_Plan,Day_Calls,Day_Charge,Evening_Calls,Evening_Charge,Night_Calls,Night_Charge,International_Calls,International_Charge,State,Area_Code,Phone

```

our model will append a `Churn` column with the predictions and save it in the `out` directory.
