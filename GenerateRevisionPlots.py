import GetRevisionTimestamps as gt
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import os
import matplotlib



def Generate_Plots(nominees, start=None, end=None):
    count = 0
    if start:
        start = datetime.strptime(start, "%Y-%m-%d")
    if end:
        end = datetime.strptime(end, "%Y-%m-%d")

    for name in nominees:
        Search_Name = name
        timestamps = gt.get_revision_timestamps(Search_Name)
        timestamps.reverse()

        print(timestamps)

        dates = []
        for stamp in timestamps:
            d = datetime.strptime(stamp, '%Y-%m-%dT%H:%M:%SZ')
            if not start:
                if end:
                    if d <= end:
                        dates.append(d)
                elif not end:
                    dates.append(d)
            else: #if start
                if end:
                    if start <= d <= end:
                        dates.append(d)
                elif not end:
                    if start <= d:
                        dates.append(d)

        print(dates)
        print(len(dates))

        matplotlib.rc('xtick', labelsize=5)
        fig, ax = plt.subplots()
        plt.plot_date(dates, range(len(dates)))
        plt.title(Search_Name)
        plt.xlabel('Time')
        plt.ylabel('Revision Count')
        ax.set_xlim([start, end])



        plt.ylim(top=150) # set this according to the largest size revision_list.
        count += 1
        plt.savefig(os.path.join("/Users/talzaken/PycharmProjects/WikipediaVisualizer/Projects/VPNomAnalyses/VP Plots/FixedDates", str(count)+Search_Name))
        plt.close()