import GetRevisionTimestamps as gt
import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt




# Takes an article name, and returns a list of datetime objects
# representing datetimes of revisions

def get_stamps_as_dates(Search_Name):
    timestamps = gt.get_revision_timestamps(Search_Name)
    timestamps.reverse()

    dates = []
    for stamp in timestamps:
        d = datetime.strptime(stamp, '%Y-%m-%dT%H:%M:%SZ')
        dates.append(d)

    return dates


# takes an article name (Search_Name)
# and optional timeunit argument (options are "Y", "M", "W", "D"),
# and returns a numpy nd array grouped by specified timeunit.
# if no timeunit is specified, it defaults to year ("Y").

def group_timestamps(Search_Name, timeunit=None):
    dates = get_stamps_as_dates(Search_Name)

    dt_index = pd.DatetimeIndex(dates)
    df = pd.DataFrame(dt_index)
    if not timeunit:
        grouped_df = df.groupby([(df[0].dt.year.values)]).count().reset_index().values
    if timeunit == "D":
        grouped_df = df.groupby([(df[0].dt.year.values),
                                 (df[0].dt.month.values),
                                 (df[0].dt.week.values),
                                 (df[0].dt.day.values)]).count().reset_index().values
    if timeunit == "W":
        grouped_df = df.groupby([(df[0].dt.year.values),
                                 (df[0].dt.month.values),
                                 (df[0].dt.week.values)]).count().reset_index().values
    if timeunit == "M":
        grouped_df = df.groupby([(df[0].dt.year.values),
                                 (df[0].dt.month.values)]).count().reset_index().values

    if timeunit == "Y":
        grouped_df = df.groupby([(df[0].dt.year.values)]).count().reset_index().values

    return grouped_df




# Calculates the average number of revisions for an article over a given timeunit.
# Takes an article name (Search_Name)
# and optional timeunit argument (options are "Y", "M", "W", "D").

def avg_wiki_edits(Search_Name, timeunit=None):
    grouped_df = group_timestamps(Search_Name, timeunit)

    timeunit_count = 0
    sum_timeunit_edits = 0
    for val in grouped_df:
        timeunit_count += 1
        sum_timeunit_edits += val[-1]

    avg_timeunit_edits = sum_timeunit_edits/timeunit_count

    return avg_timeunit_edits


