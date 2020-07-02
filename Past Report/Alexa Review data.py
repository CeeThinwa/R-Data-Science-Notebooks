import numpy as np
import pandas as pd

# Fetch dataset
AlexaReviews = pd.read_csv('https://s3-us-west-2.amazonaws.com/patchworks-coding-challenge/amazon_alexa.tsv', sep='\t')

# View datatypes within each dataset, the shape and the first 10 rows
AlexaReviews.shape
print(' ')
print('Alexa Reviews Dataset')
print(AlexaReviews.dtypes)
print(' ')

print(AlexaReviews.shape)
print(' ')
AlexaReviews.head(10)

# Change the format of the date column to date-time
AlexaReviews['date'] = pd.to_datetime(AlexaReviews['date'])

# Make the reviews lowercase
AlexaReviews['verified_reviews'] = AlexaReviews['verified_reviews'].str.lower()

# Remove all punctuation
AlexaReviews['verified_reviews'] = AlexaReviews['verified_reviews'].str.replace('[^\w\s]','')

# Based on earlier analysis the verbs to be dummified are:
# 1. Love          6. Good
# 2. Great         7. Doesnt
# 3. Like          8. Quality
# 4. Easy          9. Better
# 5. Works        10. Well

AlexaReviews.loc[:, 'love_dummy'] = AlexaReviews['verified_reviews'].str.contains('love', regex=True).astype(int)
AlexaReviews.loc[:, 'great_dummy'] = AlexaReviews['verified_reviews'].str.contains('great', regex=True).astype(int)
AlexaReviews.loc[:, 'like_dummy'] = AlexaReviews['verified_reviews'].str.contains('like', regex=True).astype(int)
AlexaReviews.loc[:, 'easy_dummy'] = AlexaReviews['verified_reviews'].str.contains('easy', regex=True).astype(int)
AlexaReviews.loc[:, 'works_dummy'] = AlexaReviews['verified_reviews'].str.contains('works', regex=True).astype(int)
AlexaReviews.loc[:, 'good_dummy'] = AlexaReviews['verified_reviews'].str.contains('good', regex=True).astype(int)
AlexaReviews.loc[:, 'doesnt_dummy'] = AlexaReviews['verified_reviews'].str.contains('doesnt', regex=True).astype(int)
AlexaReviews.loc[:, 'quality_dummy'] = AlexaReviews['verified_reviews'].str.contains('quality', regex=True).astype(int)
AlexaReviews.loc[:, 'better_dummy'] = AlexaReviews['verified_reviews'].str.contains('better', regex=True).astype(int)
AlexaReviews.loc[:, 'well_dummy'] = AlexaReviews['verified_reviews'].str.contains('well', regex=True).astype(int)

#Finally, delete unnecessary columns
AlexaReviews = AlexaReviews.drop(labels = ['feedback', 'verified_reviews'], axis = 1)

# Export this data as CSV
AlexaReviews.to_csv('C://Users//CT//Documents//AlexaReviews.csv', index=False)
