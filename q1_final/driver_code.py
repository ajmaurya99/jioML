# Importing all the required Libraries

import json
import pandas as pd
from flask import Flask, escape, request
app = Flask(__name__)


# Using Flask for displaying the output result

@app.route('/app/', defaults={'search_string': 'Please enter a string to search'})
@app.route('/app/<search_string>')
def search_string(search_string):

    df = main()
    result = auto_complete_results(df, search_string)
    if result:
        return str(result)
    else:
        return str("No Matching String Found, Please try another string")


def auto_complete_results(df, prefix):

    df1 = df[df['question'].str.contains(prefix)].sort_values(
        by='rank', ascending=False)
    return list(df1['question'])

# Function to read the json file


def main():
    with open('data/auto_fill_data.json') as json_file:
        jsonData = json.load(json_file)
        data = []
        for i in jsonData:
            data.append([i['question'], i['rank']])

        df = pd.DataFrame(data, columns=['question', 'rank'])
        return df


if __name__ == "__main__":
    app.run(debug=True)